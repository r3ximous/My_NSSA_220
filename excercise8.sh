#!/bin/bash

# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <directory_path>"
  exit 1
fi 

# Check if the provided argument is a valid directory
if [ ! -d "$1" ]; then
  echo "Error: $1 is not a valid directory."
  exit 1
fi

# Count the number of files and directories
num_files=$(find "$1" -type f | wc -l)
num_dirs=$(find "$1" -type d | wc -l)

# Print the counts
echo "Number of files: $num_files"
echo "Number of directories: $num_dirs"