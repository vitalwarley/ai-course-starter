#!/bin/bash
set -e

# Install uv if not already installed
if ! command -v uv &> /dev/null; then
    echo "Installing uv package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # Check if .local/bin is in PATH and add it if not
    if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
        echo "Adding ~/.local/bin to PATH..."
        export PATH="$HOME/.local/bin:$PATH"
    fi
fi

# Create virtual environment with Python 3.11
echo "Creating virtual environment with Python 3.12..."
uv venv --python=python3.12 .venv

# Source the virtual environment
echo "Sourcing the virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
uv pip install --requirement pyproject.toml


echo "Setup complete! Activate the environment with: source .venv/bin/activate" 

# Download example video for testing
echo "Downloading example video..."
./download_and_extract.sh https://www.youtube.com/watch?v=183tAr8imcU ./downloads 
