#!/bin/bash

# Script to zip Python files, README files, pyproject.toml, and shell scripts from a given directory
# Usage: ./zip_task.sh <directory_path>

# Check if directory argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <directory_path>"
    echo "Example: $0 task-01-tech-extract"
    exit 1
fi

DIRECTORY="$1"

# Check if directory exists
if [ ! -d "$DIRECTORY" ]; then
    echo "Error: Directory '$DIRECTORY' does not exist."
    exit 1
fi

# Get the base name of the directory for the zip file name
BASE_NAME=$(basename "$DIRECTORY")
ZIP_NAME="${BASE_NAME}.zip"

# Remove existing zip file if it exists
if [ -f "$ZIP_NAME" ]; then
    echo "Removing existing zip file: $ZIP_NAME"
    rm "$ZIP_NAME"
fi

echo "Creating zip file: $ZIP_NAME"
echo "Searching for files in directory: $DIRECTORY"

# Create temporary file list
TEMP_FILE=$(mktemp)

# Change to the target directory
cd "$DIRECTORY" || exit 1

# Find files and add them to temp file, excluding unwanted directories
find . -type f \( -name "*.py" -o -name "README*" -o -name "pyproject.toml" -o -name "*.sh" \) | \
    grep -E -v "^\./(\.venv|__pycache__|\.git|node_modules|\.pytest_cache|\.tox)/" > "$TEMP_FILE"

# Check if any files were found
if [ ! -s "$TEMP_FILE" ]; then
    echo "No files found matching the criteria."
    rm "$TEMP_FILE"
    cd - > /dev/null
    exit 1
fi

echo "Files to be zipped:"
cat "$TEMP_FILE"

# Create zip file from the file list
zip "../$ZIP_NAME" -@ < "$TEMP_FILE"

# Clean up
rm "$TEMP_FILE"

# Go back to original directory
cd - > /dev/null

# Check if zip was created successfully
if [ -f "$ZIP_NAME" ]; then
    echo "Successfully created: $ZIP_NAME"
    echo "Contents:"
    unzip -l "$ZIP_NAME"
else
    echo "Error: Failed to create zip file."
    exit 1
fi 