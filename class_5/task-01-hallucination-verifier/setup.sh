#!/bin/bash
set -e

echo "Setting up Hallucination Verifier..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Installing uv package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # Add uv to PATH for current session
    export PATH="$HOME/.local/bin:$PATH"
fi

# Create virtual environment
echo "Creating virtual environment..."
uv venv --python=python3.12 .venv

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
uv pip install --requirement pyproject.toml

echo "Setup complete!"
echo "To activate the virtual environment, run:"
echo "source .venv/bin/activate"
echo ""
echo "Then you can run:"
echo "python main.py    # For command line demo"
echo "python app.py     # For web interface" 