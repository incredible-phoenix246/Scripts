#!/bin/bash

# Check if there is at least one argument provided
if [ $# -lt 1 ]; then
  echo "Usage: $0 <commit_message>"
  exit 1
fi

# Commit message provided as the first argument
commit_message="$1"

# Add all changes
git add .

# Commit changes with the provided message
git commit -m "$commit_message"

# Push changes to the remote repository
git push
