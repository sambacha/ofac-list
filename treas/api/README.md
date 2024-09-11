### OFAC Sanctions List Service - API Documentation

> [!IMPORTANT]
> Information sourced from the [Official OFAC Guidance Production Submission Standard](https://ofac.treasury.gov/media/932996/download?inline)

#### Overview
The OFAC Sanctions List Service (SLS) provides an API that enables users to retrieve data from the Office of Foreign Assets Control (OFAC) sanctions lists directly from its backend databases. The service facilitates automated or scripted interaction with the sanctions list, particularly benefiting users in compliance-related industries who need to automate sanctions screening. Prior to the API, users had to manually download the entire list, but the new system allows for targeted data retrieval.

#### API Features
- **Entities:** The API supports various GET requests to retrieve metadata for entities based on their IDs, sanction lists, or programs. Users can pull data as frequently as desired.
- **Files:** The API also supports requests for downloading specific sanctions lists in various formats (ZIP, XML, CSV, etc.).
- **List Information:** Users can retrieve changes to the sanctions lists, including historical data and delta updates.
- **Customized Sanction Dataset:** This endpoint allows users to customize their sanctions list dataset by specifying the list type (SDN or Consolidated) and date of publication.

#### Supported API Commands

1. **Entity Metadata Retrieval**
   - Retrieve entity metadata based on ID, sanction list, or program:
     - `GET https://sanctionslistservice.ofac.treas.gov/entities`
     - `GET https://sanctionslistservice.ofac.treas.gov/entities/{entity-id}`
     - Filters by list or program can be added to the queries.
   - Example:
     ```bash
     curl -X 'GET' 'https://sanctionslistservice.ofac.treas.gov/entities/30629' -H 'accept: */*'
     ```

2. **File Download**
   - Download specific sanctions files using the file name:
     - `GET https://sanctionslistservice.ofac.treas.gov/api/download/{filename}`
     - Available files include SDN_ENHANCED.ZIP, SDN.XML, CONS_ADVANCED.ZIP, etc.

3. **List Changes**
   - Retrieve the latest sanctions list delta file:
     - `GET https://sanctionslistservice.ofac.treas.gov/changes/latest`
   - Retrieve historical list publications:
     - `GET https://sanctionslistservice.ofac.treas.gov/changes/history/{year}`
     - `GET https://sanctionslistservice.ofac.treas.gov/changes/history/{year}/{month}/{day}`

4. **Sanction Programs and Lists**
   - Retrieve the names of all sanction lists:
     - `GET https://sanctionslistservice.ofac.treas.gov/sanctions-lists`
   - Retrieve the names of all sanction programs:
     - `GET https://sanctionslistservice.ofac.treas.gov/sanctions-programs`

5. **Customized Sanction Dataset**
   - Generate a customized sanctions list dataset based on list type and publication date:
     - `GET https://sanctionslistservice.ofac.treas.gov/api/Customize/GetCustomizeList`

6. **Health Check**
   - Verify the API's health and availability:
     - `GET https://sanctionslistservice.ofac.treas.gov/alive`
     - Example response:
     ```bash
     curl -X 'GET' 'https://sanctionslistservice.ofac.treas.gov/alive' -H 'accept: */*'
     ```

#### File Formats
The API supports several file formats for sanctions lists, including:
- **ZIP** files (e.g., `SDN_ENHANCED.ZIP`, `CONS_ADVANCED.ZIP`)
- **XML** files (e.g., `SDN.XML`, `CONSOLIDATED.XML`)
- **CSV** files (e.g., `SDN.CSV`, `CONS_PRIM.CSV`)
- **Flat Files (FF)** (e.g., `SDN.FF`, `CONS_PRIM.FF`)

#### Example Curl Requests
The documentation provides multiple examples of how to retrieve data using `curl` commands. Below is an example of retrieving the latest sanctions list changes:
```bash
curl -X 'GET' 'https://sanctionslistservice.ofac.treas.gov/changes/latest' -H 'accept: */*'
```

#### Additional Information
- **OFAC’s API supports automation of data pulls**, which is particularly useful for large organizations that regularly require up-to-date sanctions data for compliance.
- **Historical data retrieval** allows for in-depth analysis of sanctions list updates over specific periods, including daily, monthly, and yearly.

---

### OFAC Sanctions List Service - API Documentation (GitHub-Flavored Markdown)

```markdown
# OFAC Sanctions List Service - API Documentation

## Overview
The OFAC Sanctions List Service (SLS) provides an API that allows users to retrieve data from the OFAC sanctions lists directly from its backend databases. The API supports automated or scripted interaction, which is useful for compliance-related tasks. Users can select which parts of the sanctions lists they wish to download and at what frequency.

## API Commands

### 1. Entity Metadata Retrieval

Retrieve entity metadata based on ID, sanction list, or program:

- **Endpoint:**
  - `GET https://sanctionslistservice.ofac.treas.gov/entities`
  - `GET https://sanctionslistservice.ofac.treas.gov/entities/{entity-id}`

- **Query Parameters:**
  - `list={list-name}`
  - `program={program-name}`

- **Example Curl Request:**
  ```bash
  curl -X 'GET' 'https://sanctionslistservice.ofac.treas.gov/entities/30629' -H 'accept: */*'
  ```

### 2. File Download

Download specific sanctions list files:

- **Endpoint:**
  - `GET https://sanctionslistservice.ofac.treas.gov/api/download/{filename}`

- **Available Files:**
  - `SDN_ENHANCED.ZIP`
  - `SDN.XML`
  - `CONS_ADVANCED.ZIP`
  - `CONS_ENHANCED.CSV`

### 3. List Changes

Retrieve the latest sanctions list delta file or historical list changes:

- **Endpoints:**
  - `GET https://sanctionslistservice.ofac.treas.gov/changes/latest`
  - `GET https://sanctionslistservice.ofac.treas.gov/changes/history/{year}`
  - `GET https://sanctionslistservice.ofac.treas.gov/changes/history/{year}/{month}/{day}`

- **Example Curl Request:**
  ```bash
  curl -X 'GET' 'https://sanctionslistservice.ofac.treas.gov/changes/latest' -H 'accept: */*'
  ```

### 4. Sanction Programs and Lists

Retrieve all sanction list or program names:

- **Endpoints:**
  - `GET https://sanctionslistservice.ofac.treas.gov/sanctions-lists`
  - `GET https://sanctionslistservice.ofac.treas.gov/sanctions-programs`

- **Example Curl Request:**
  ```bash
  curl -X 'GET' 'https://sanctionslistservice.ofac.treas.gov/sanctions-lists' -H 'accept: */*'
  ```

### 5. Customized Sanction Dataset

Retrieve a customized sanctions list dataset based on list type and publication date:

- **Endpoint:**
  - `GET https://sanctionslistservice.ofac.treas.gov/api/Customize/GetCustomizeList`

### 6. Health Check

Check the health status of the API:

- **Endpoint:**
  - `GET https://sanctionslistservice.ofac.treas.gov/alive`

- **Example Curl Request:**
  ```bash
  curl -X 'GET' 'https://sanctionslistservice.ofac.treas.gov/alive' -H 'accept: */*'
  ```

## File Formats

The API supports several file formats for sanctions lists:

- ZIP (e.g., `SDN_ENHANCED.ZIP`, `CONS_ADVANCED.ZIP`)
- XML (e.g., `SDN.XML`, `CONSOLIDATED.XML`)
- CSV (e.g., `SDN.CSV`, `CONS_PRIM.CSV`)
- Flat Files (FF) (e.g., `SDN.FF`, `CONS_PRIM.FF`)

### Example Curl Requests

Here is an example of retrieving the latest sanctions list changes:

```bash
curl -X 'GET' 'https://sanctionslistservice.ofac.treas.gov/changes/latest' -H 'accept: */*'
```

**Office of Foreign Assets Control – List Management Division**
```

This is a detailed breakdown and the GitHub-flavored Markdown conversion of the OFAC Sanctions List Service API documentation.

## API Spec

```yaml
openapi: 3.0.0
info:
  title: OFAC Sanctions List Service API
  description: This API allows users to retrieve and download OFAC sanctions list data, including entities, lists, files, and customized datasets.
  version: 1.0.0
servers:
  - url: https://sanctionslistservice.ofac.treas.gov

paths:
  /entities:
    get:
      summary: Retrieve metadata for entities
      description: Retrieve metadata related to a collection of entities. Optionally filter by list or program.
      parameters:
        - name: list
          in: query
          description: Sanctions list name to filter entities.
          required: false
          schema:
            type: string
        - name: program
          in: query
          description: Program name to filter entities.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A collection of entities.
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Entity'
  /entities/{entity-id}:
    get:
      summary: Retrieve metadata for a specific entity
      description: Retrieve metadata related to a specific entity by ID.
      parameters:
        - name: entity-id
          in: path
          required: true
          description: The ID of the entity to retrieve.
          schema:
            type: string
      responses:
        '200':
          description: An entity's metadata.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Entity'
  
  /api/download/{filename}:
    get:
      summary: Download sanctions files
      description: Download sanctions list files based on the provided filename.
      parameters:
        - name: filename
          in: path
          required: true
          description: The name of the file to download.
          schema:
            type: string
      responses:
        '200':
          description: File downloaded.
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary

  /changes/latest:
    get:
      summary: Retrieve the latest sanctions list delta file
      description: Retrieve the latest published sanctions list delta file in XML format.
      responses:
        '200':
          description: Latest sanctions list delta file.
          content:
            application/xml:
              schema:
                type: string

  /changes/{publication-id}:
    get:
      summary: Retrieve sanctions list delta file by publication ID
      description: Retrieve a sanctions list delta file based on a unique publication ID.
      parameters:
        - name: publication-id
          in: path
          required: true
          description: The unique ID of the publication.
          schema:
            type: string
      responses:
        '200':
          description: Sanctions list delta file.
          content:
            application/xml:
              schema:
                type: string

  /changes/history/{year}:
    get:
      summary: Retrieve sanctions list changes by year
      description: Retrieve a list of publications based on the specified year.
      parameters:
        - name: year
          in: path
          required: true
          description: The year of the sanctions list changes.
          schema:
            type: string
      responses:
        '200':
          description: Sanctions list changes for the specified year.
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Publication'

  /changes/history/{year}/{month}/{day}:
    get:
      summary: Retrieve sanctions list changes by year, month, and day
      description: Retrieve a list of publications based on the specified year, month, and day.
      parameters:
        - name: year
          in: path
          required: true
          description: The year of the sanctions list changes.
          schema:
            type: string
        - name: month
          in: path
          required: true
          description: The month of the sanctions list changes.
          schema:
            type: string
        - name: day
          in: path
          required: true
          description: The day of the sanctions list changes.
          schema:
            type: string
      responses:
        '200':
          description: Sanctions list changes for the specified year, month, and day.
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Publication'

  /sanctions-lists:
    get:
      summary: Retrieve all sanctions lists
      description: Retrieve a list of all available sanctions lists.
      responses:
        '200':
          description: A list of sanctions lists.
          content:
            application/json:
              schema:
                type: array
                items:
                  type: string

  /sanctions-programs:
    get:
      summary: Retrieve all sanctions programs
      description: Retrieve a list of all available sanctions programs.
      responses:
        '200':
          description: A list of sanctions programs.
          content:
            application/json:
              schema:
                type: array
                items:
                  type: string

  /api/Customize/GetCustomizeList:
    get:
      summary: Retrieve customized sanctions list
      description: Retrieve a customized sanctions list based on the provided parameters of publication date and list type.
      parameters:
        - name: publicationDate
          in: query
          description: The date of the publication.
          schema:
            type: string
            format: date
        - name: listType
          in: query
          description: The type of sanctions list (SDN or CONS).
          schema:
            type: string
      responses:
        '200':
          description: A customized sanctions list.
          content:
            application/xml:
              schema:
                type: string

  /alive:
    get:
      summary: API health check
      description: Provides a health status check of the Sanctions List API.
      responses:
        '200':
          description: Health status.
          content:
            text/plain:
              schema:
                type: string

components:
  schemas:
    Entity:
      type: object
      properties:
        entityId:
          type: string
        identityId:
          type: string
        entityType:
          type: string
        sanctionsLists:
          type: array
          items:
            type: object
            properties:
              refId:
                type: string
              id:
                type: string
              datePublished:
                type: string
                format: date
        sanctionsPrograms:
          type: array
          items:
            type: object
            properties:
              refId:
                type: string
              id:
                type: string
        sanctionsTypes:
          type: array
          items:
            type: object
            properties:
              refId:
                type: string
              id:
                type: string
        legalAuthorities:
          type: array
          items:
            type: object
            properties:
              refId:
                type: string
              id:
                type: string
        names:
          type: array
          items:
            type: object
            properties:
              isPrimary:
                type: boolean
              formattedFullName:
                type: string
        addresses:
          type: array
          items:
            type: object
            properties:
              country:
                type: string
        features:
          type: array
          items:
            type: object
            properties:
              type:
                type: string
              value:
                type: string
              valueDate:
                type: object
                properties:
                  fromDateBegin:
                    type: string
                    format: date
                  toDateEnd:
                    type: string
                    format: date

    Publication:
      type: object
      properties:
        publicationID:
          type: string
        datePublished:
          type: string
          format: date-time
```

This OpenAPI v3 document captures all the endpoints mentioned in the OFAC Sanctions List Service API documentation, including paths for retrieving entity metadata, downloading files, checking list changes, fetching customized datasets, and utility/health check functionality.
