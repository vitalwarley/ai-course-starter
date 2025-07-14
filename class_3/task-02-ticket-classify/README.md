# Support Ticket Entity Extraction & Classification

An intelligent support ticket processing system that automatically extracts user information (user, OS, version) and classifies tickets by priority and category using advanced pattern matching and spaCy NLP capabilities.

## Features

- **Entity Extraction**: Automatically identifies user names, operating systems, and software versions from ticket text
- **Priority Classification**: Categorizes tickets as low, medium, or high priority based on urgency indicators
- **Category Classification**: Classifies tickets into bug reports, feature requests, or questions
- **spaCy Integration**: Uses advanced NLP for named entity recognition when pattern matching fails
- **Robust Pattern Matching**: Handles various text formats and structures commonly found in support tickets
- **Demo Interface**: Command-line demonstration with realistic sample tickets
- **High Accuracy**: Designed to achieve entity macro-F1 ≥ 0.85 and joint accuracy ≥ 0.80

## Requirements

- Python 3.12 or higher
- spaCy library with English language model
- OpenAI API key (optional, for future enhancements)
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
3. Install all required dependencies (spaCy, OpenAI)
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

4. **Download spaCy model** (optional, for enhanced NER):
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage

### Command Line Demo

Run the demonstration script to see the entity extraction and classification in action:

```bash
source .venv/bin/activate  # If not already activated
python main.py
```

or run directly with uv:

```bash
uv run python main.py
```

### Programmatic Usage

You can use the extraction and classification functions directly in your Python code:

```python
from solution import extract_entities, classify

# Extract entities from ticket text
ticket_text = "The application crashes when I click Export. This is blocking my work! - User: bob, OS: Ubuntu 22.04, Version: v2.0.0"

# Extract user, OS, and version information
entities = extract_entities(ticket_text)
print(entities)
# Output: {'user': 'bob', 'os': 'ubuntu 22.04', 'version': 'v2.0.0'}

# Classify priority and category
priority, category = classify(ticket_text)
print(f"Priority: {priority}, Category: {category}")
# Output: Priority: high, Category: bug
```

## API Reference

### `extract_entities(text: str) -> Entities`

Extracts user, operating system, and version information from ticket text.

**Parameters:**
- `text` (str): The support ticket text to analyze

**Returns:**
- `Entities`: A TypedDict containing:
  - `"user"` (str): The username or person reporting the issue
  - `"os"` (str): The operating system information
  - `"version"` (str): The software version information

### `classify(text: str) -> Tuple[Priority, Category]`

Classifies the ticket by priority and category.

**Parameters:**
- `text` (str): The support ticket text to analyze

**Returns:**
- `Tuple[Priority, Category]`: A tuple containing:
  - `Priority`: One of `"low"`, `"medium"`, `"high"`
  - `Category`: One of `"bug"`, `"question"`, `"feature"`

## Classification Logic

### Priority Classification

**High Priority** - Urgent issues requiring immediate attention:
- Keywords: critical, urgent, emergency, blocking, crash, down, broken, error, production, outage

**Medium Priority** - Standard issues (default):
- Issues that don't clearly fall into high or low priority categories

**Low Priority** - Non-urgent requests:
- Keywords: question, enhancement, feature, nice to have, minor, suggestion, cosmetic

### Category Classification

**Bug** - Issues with existing functionality:
- Keywords: crash, error, broken, not working, problem, issue, malfunction, defect

**Question** - Help requests and inquiries:
- Keywords: how, what, why, help, explain, question, does, can, should
- Contains question marks (?)

**Feature** - New functionality requests:
- Keywords: feature, add, new, request, enhancement, improvement, implement

## Example Usage

### Sample Support Tickets

```python
# Example 1: Bug report
text1 = "The application crashes when I click Export. This is blocking my work! - User: bob, OS: Ubuntu 22.04, Version: v2.0.0"
entities1 = extract_entities(text1)
priority1, category1 = classify(text1)
print(f"User: {entities1['user']}, Priority: {priority1}, Category: {category1}")
# Output: User: bob, Priority: high, Category: bug

# Example 2: Question
text2 = "Is there a way to change the theme? - User: alice, OS: Windows 11, Version: v2.0.1"
entities2 = extract_entities(text2)
priority2, category2 = classify(text2)
print(f"User: {entities2['user']}, Priority: {priority2}, Category: {category2}")
# Output: User: alice, Priority: low, Category: question

# Example 3: Feature request
text3 = "Could you add support for dark mode? That would be great! - User: diana, OS: Windows 10, Version: v2.1.0"
entities3 = extract_entities(text3)
priority3, category3 = classify(text3)
print(f"User: {entities3['user']}, Priority: {priority3}, Category: {category3}")
# Output: User: diana, Priority: low, Category: feature
```

## Project Structure

```
task-02-ticket-classify/
├── main.py            # Command-line demonstration
├── solution.py        # Core extraction and classification logic
├── pyproject.toml     # Project configuration
├── setup.sh          # Automated setup script
├── tickets_sample.jsonl  # Sample data
└── README.md         # This file
```

## Development

### Entity Extraction Algorithm

The entity extraction process uses multiple techniques:

1. **Pattern Matching**: Regex patterns for structured data (User: bob, OS: Ubuntu, etc.)
2. **spaCy NER**: Named entity recognition for person names when patterns fail
3. **Normalization**: Consistent formatting of extracted entities
4. **Fallback Handling**: Graceful handling of missing or malformed data

### Classification Algorithm

The classification system employs:

1. **Keyword-based Classification**: Comprehensive lists of indicator words
2. **Priority Assessment**: Urgency-based scoring using contextual clues
3. **Category Detection**: Content analysis to determine issue type
4. **Default Fallbacks**: Sensible defaults when classification is uncertain

### Sample Data Format

Input data should be in JSONL format:
```json
{"user": "bob", "os": "Ubuntu 22.04", "version": "v2.0.0", "body": "The application crashes when I click Export. This is blocking my work!"}
{"user": "alice", "os": "Windows 11", "version": "v2.0.1", "body": "Is there a way to change the theme?"}
```

## Performance Targets

- **Entity Macro-F1**: ≥ 0.85
- **Joint Accuracy**: ≥ 0.80 (priority + category combined)
- **Processing Speed**: Handles typical support tickets in milliseconds
- **Memory Usage**: Lightweight with minimal memory footprint

## Supported Entity Formats

### User Extraction
- "User: bob", "user bob", "reported by alice"
- "from charlie", "by diana"
- Named entity recognition for person names

### OS Extraction
- "OS: Ubuntu 22.04", "Operating System: Windows 11"
- "Platform: macOS 13.2", "os linux"
- Supports Ubuntu, Windows, macOS, Linux variations

### Version Extraction
- "Version: v2.0.0", "Ver: 1.9.5"
- "v2.1.0", "version 2.0.1"
- Automatic "v" prefix addition for numeric versions

## License

This project is part of the TIC43 AI Course and is intended for educational purposes.

## Troubleshooting

### Common Issues

1. **Missing spaCy model**: Run `python -m spacy download en_core_web_sm` to install
2. **Empty entities**: Check that entity information is present in the expected format
3. **Incorrect classification**: Verify that priority/category keywords are present in the text
4. **Python version**: Ensure you're using Python 3.12 or higher
5. **Virtual environment**: Always activate the virtual environment before running

### Support

For issues and questions, please refer to the course materials or contact the course instructor.
