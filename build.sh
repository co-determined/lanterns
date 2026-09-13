#!/bin/bash
# Build the upload bundle: index.html at the zip root, nothing else (SDK loads from CrazyGames' CDN).
# Refuses to build if the script doesn't parse — a zip must never be made from a broken file.
set -e; cd "$(dirname "$0")"; V=${1:-1.0}
node -e "const s=require('fs').readFileSync('index.html','utf8');const js=s.split('<script>')[1].split('</script>')[0];new Function(js);" || { echo "index.html does not parse — not building"; exit 1; }
mkdir -p dist; rm -f "dist/lanterns_v$V.zip"
zip -q -j "dist/lanterns_v$V.zip" index.html && ls -la "dist/lanterns_v$V.zip" && unzip -l "dist/lanterns_v$V.zip" | tail -3
