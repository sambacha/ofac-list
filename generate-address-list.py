#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# @Author: 0xB10C
# Modified 

import xml.etree.ElementTree as ET
import argparse
import pathlib
import json
import logging

FEATURE_TYPE_TEXT = "Digital Currency Address - "
NAMESPACE = {'sdn': 'https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/ADVANCED_XML'}
POSSIBLE_ASSETS = ["XBT", "ETH", "XMR", "LTC", "ZEC", "DASH", "BTG", "ETC",
                   "BSV", "BCH", "XVG", "USDT", "XRP", "ARB", "BSC", "USDC",
                   "TRX"]
OUTPUT_FORMATS = ["TXT", "JSON"]


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Tool to extract sanctioned digital currency addresses from the OFAC special designated nationals XML file (sdn_advanced.xml)')
    parser.add_argument('assets', choices=POSSIBLE_ASSETS, nargs='*',
                        default=POSSIBLE_ASSETS[0], help='the asset for which the sanctioned addresses should be extracted (default: XBT (Bitcoin))')
    parser.add_argument('-sdn', '--special-designated-nationals-list', dest='sdn', type=argparse.FileType('rb'),
                        help='the path to the sdn_advanced.xml file (can be downloaded from https://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xml)', default="./sdn_advanced.xml")
    parser.add_argument('-f', '--output-format',  dest='format', nargs='*', choices=OUTPUT_FORMATS,
                        default=OUTPUT_FORMATS[0], help='the output file format of the address list (default: TXT)')
    parser.add_argument('-path', '--output-path', dest='outpath',  type=pathlib.Path, default=pathlib.Path(
        "./"), help='the path where the lists should be written to (default: current working directory ("./")')
    return parser.parse_args()


def feature_type_text(asset):
    """Returns the expected text for a given asset's feature type."""
    return "Digital Currency Address - " + asset


def get_address_id(root, asset):
    """Returns the feature ID for a given asset in the XML root."""
    feature_type = root.find(
        "sdn:ReferenceValueSets/sdn:FeatureTypeValues/*[.='{}']".format(feature_type_text(asset)), NAMESPACE)
    if feature_type is None:
        raise LookupError("No FeatureType with the name {} found".format(
            feature_type_text(asset)))
    address_id = feature_type.attrib["ID"]
    return address_id


def get_sanctioned_addresses(root, address_id):
    """Returns a list of sanctioned addresses for the given address_id."""
    addresses = []
    for feature in root.findall("sdn:DistinctParties//*[@FeatureTypeID='{}']".format(address_id), NAMESPACE):
        for version_detail in feature.findall(".//sdn:VersionDetail", NAMESPACE):
            addresses.append(version_detail.text)
    return addresses


def write_addresses(addresses, asset, output_formats, outpath):
    """Writes the addresses to files based on the specified output formats."""
    if "TXT" in output_formats:
        write_addresses_txt(addresses, asset, outpath)
    if "JSON" in output_formats:
        write_addresses_json(addresses, asset, outpath)


def write_addresses_txt(addresses, asset, outpath):
    """Writes the addresses to a text file."""
    with open("{}/sanctioned_addresses_{}.txt".format(outpath, asset), 'w') as out:
        for address in addresses:
            out.write(address + "\n")


def write_addresses_json(addresses, asset, outpath):
    """Writes the addresses to a JSON file."""
    with open("{}/sanctioned_addresses_{}.json".format(outpath, asset), 'w') as out:
        out.write(json.dumps(addresses, indent=2) + "\n")


def main():
    logging.basicConfig(level=logging.INFO)

    try:
        args = parse_arguments()

        tree = ET.parse(args.sdn)
        root = tree.getroot()

        assets = args.assets if isinstance(args.assets, list) else [args.assets]
        output_formats = args.format if isinstance(args.format, list) else [args.format]

        for asset in assets:
            try:
                address_id = get_address_id(root, asset)
                addresses = get_sanctioned_addresses(root, address_id)

                # Deduplicate and sort addresses
                addresses = sorted(set(addresses))

                write_addresses(addresses, asset, output_formats, args.outpath)
                logging.info(f"Processed asset: {asset}")
            except LookupError as e:
                logging.warning(f"Skipping asset {asset}: {str(e)}")

    except FileNotFoundError as e:
        logging.error(f"Error: {str(e)}")
        exit(1)
    except ET.ParseError as e:
        logging.error(f"Error parsing XML file: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
