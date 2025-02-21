#!/usr/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Use this command to run the file :bash ./run.sh '<query>' <json_file>"
    exit 1
fi

python3 Backend.py "$1" "$2"
