#!/bin/bash
mkdir -p /home/user/gta-sa-research/raw
while IFS= read -r p; do
  [ -z "$p" ] && continue
  f="/home/user/gta-sa-research/raw/$(echo "$p" | tr ' /:' '___').txt"
  if [ ! -s "$f" ]; then
    python3 /home/user/gta-sa-research/fetch.py page "$p" > "$f" 2>/dev/null
    echo "$p -> $(wc -c < "$f") bytes"
  else
    echo "$p -> cached $(wc -c < "$f")"
  fi
done
