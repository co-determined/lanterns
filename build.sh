#!/bin/bash
# Build the upload bundle: index.html at the zip root, nothing else (SDK loads from CrazyGames' CDN).
set -e; cd "$(dirname "$0")"; V=${1:-1.0}; mkdir -p dist; rm -f "dist/lanterns_v$V.zip"
zip -q -j "dist/lanterns_v$V.zip" index.html && ls -la "dist/lanterns_v$V.zip" && unzip -l "dist/lanterns_v$V.zip"
