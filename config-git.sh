#!/bin/sh 
echo "::configure-defaults ofac-action::"
git config --global http.postBuffer 2048M
git config --global http.maxRequestBuffer 1024M
git config --global core.compression 9

git config --global ssh.postBuffer 2048M
git config --global ssh.maxRequestBuffer 1024M

git config --global pack.windowMemory 256m 
git config --global pack.packSizeLimit 256m

git config user.name "${GITHUB_ACTOR}"
git config user.email "${GITHUB_ACTOR}@users.noreply.github.com"
git config --global --add safe.directory /github/workspace