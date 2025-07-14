# AI Code Refactorer

An AI-powered Python code refactoring tool that uses OpenAI's GPT-4 to analyze and improve Python code quality by reducing cyclomatic complexity, eliminating duplication, and improving readability.

## Features

- **Automated Code Analysis**: Uses OpenAI's GPT-4 to analyze Python code structure and identify improvement opportunities
- **Smart Refactoring**: Reduces cyclomatic complexity, eliminates code duplication, and improves nesting patterns
- **Type Hints**: Automatically adds type hints to improve code clarity and maintainability
- **Web Interface**: User-friendly Gradio interface for easy code input and output
- **Detailed Explanations**: Provides clear explanations of why changes improve readability, testability, and performance

## Requirements

- Python 3.12 or higher
- OpenAI API key
- UV package manager (will be installed automatically if not present)

## Installation

### Quick Setup

Run the provided setup script to automatically install all dependencies:

```bash
./setup.sh
```

This script will:
1. Install the UV package manager if not already present
2. Create a Python 3.12 virtual environment
3. Install all required dependencies
4. Set up the project for immediate use

### Manual Setup

If you prefer to set up manually:

1. **Install UV package manager**:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Create virtual environment**:
   ```bash
   uv venv --python=python3.12 .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   uv pip install --requirement pyproject.toml
   ```

## Configuration

Before using the tool, you need to set up your OpenAI API key:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Or add it to your shell profile:
```bash
echo 'export OPENAI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

## Usage

### Web Interface

Launch the Gradio web interface:

```bash
source .venv/bin/activate  # If not already activated
python app.py
```

or run the following command:

```bash
uv run app.py
```

The interface will be available at `http://localhost:7860` where you can:
1. Paste your Python code in the input field
2. Click "Submit" to get refactored code
3. View the improved code and detailed explanation

### Programmatic Usage

You can also use the refactoring function directly in your Python code:

```python
from solution import refactor_code

# Your original code as a string
original_code = """
def calculate_total(items):
    total = 0
    for item in items:
        if item['active']:
            if item['price'] > 0:
                total += item['price']
    return total
"""

# Refactor the code
result = refactor_code(original_code)

print("Refactored Code:")
print(result["refactored"])
print("\nExplanation:")
print(result["explanation"])
```

## API Reference

### `refactor_code(code: str) -> dict`

Refactors the provided Python code and returns improvements with explanations.

**Parameters:**
- `code` (str): The Python code to refactor

**Returns:**
- `dict`: A dictionary containing:
  - `"refactored"` (str): The improved code
  - `"explanation"` (str): Detailed explanation of changes and improvements

## Example

### Input Code:
```python
def add(x, y):
    return x + y
```

### Output:
```python
def add(x: int, y: int) -> int:
    return x + y
```

### Explanation:
- **Type Hints**: Adding type hints improves readability by making it clear what types of arguments the function expects and what type it returns
- **Maintainability**: Type hints aid in maintaining the code and can be used by static type checkers
- **Documentation**: The type hints serve as a form of documentation

## Project Structure

```
task-03-code-refactorer/
├── app.py              # Gradio web interface
├── solution.py         # Core refactoring logic
├── pyproject.toml      # Project configuration
├── uv.lock            # Dependency lock file
├── setup.sh           # Automated setup script
└── README.md          # This file
```

## Development

### Code Structure

- **`solution.py`**: Contains the main `refactor_code()` function and OpenAI API integration
- **`app.py`**: Gradio web interface that provides a user-friendly way to interact with the refactoring tool
- **`setup.sh`**: Automated setup script for easy installation

### Dependencies

- **gradio**: Web interface framework
- **openai**: OpenAI API client for GPT-4 integration
- **Standard library**: `os`, `re` for environment variables and regex processing

## License

This project is part of the TIC43 AI Course and is intended for educational purposes.

## Troubleshooting

### Common Issues

1. **OpenAI API Key not set**: Make sure your `OPENAI_API_KEY` environment variable is properly configured
2. **Python version**: Ensure you're using Python 3.12 or higher
3. **Virtual environment**: Always activate the virtual environment before running the application

### Support

For issues and questions, please refer to the course materials or contact the course instructor. 