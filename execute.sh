#!/bin/bash

# Check if the directory path is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <directory_path>"
  exit 1
fi

# Store the directory path provided as an argument
directory="$1"

# Check if the directory exists
if [ ! -d "$directory" ]; then
  echo "Error: Directory '$directory' does not exist."
  exit 1
fi

# Add execute permission to all files in the directory
find "$directory" -type f -exec chmod +x {} \;

echo "Execute permission added to all files in '$directory'."