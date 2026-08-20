#!/bin/bash

# Outputs a file appended with the current date and time.

# Get current date, hour, and minute
mydate=$(date +"%Y-%m-%d")
Hour=$(date +"%H")
Minute=$(date +"%M")

# Go to the code_combiner directory
cd code_combiner || exit 1

# Run the Python script
python3 code_combiner_tool.py /path/to/code/directory -o "combined_code_${mydate}_${Hour}_${Minute}.txt"