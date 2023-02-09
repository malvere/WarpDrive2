#!/bin/bash
echo "Generating .toml, key: $1"
./wgc register --accept-tos --config cert/$1_Warp.toml
python3 toml_edit.py $1 
./wgc update --config cert/$1_Warp.toml
./wgc generate -p cert/$1_Warp.conf --config cert/$1_Warp.toml
python3 conf_edit.py $1
