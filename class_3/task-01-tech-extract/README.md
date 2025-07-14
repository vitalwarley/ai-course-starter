# Technology Extraction from Job Postings

An intelligent text processing tool that automatically extracts technology terms (programming languages, frameworks, databases, and cloud platforms) from job posting descriptions using advanced Named Entity Recognition (NER) and comprehensive technology databases.

## Features

- **Comprehensive Technology Database**: Covers 200+ technology terms including programming languages, web frameworks, databases, cloud platforms, DevOps tools, and ML/AI libraries
- **spaCy NER Integration**: Uses advanced Named Entity Recognition to identify technology-related entities in natural language text
- **Intelligent Entity Filtering**: Focuses on relevant entity types (ORG, PRODUCT, WORK_OF_ART, EVENT) that commonly represent technologies
- **Variation Handling**: Recognizes common variations like "node.js" → "nodejs", "C#" → "csharp", etc.
- **Case Insensitive**: Handles mixed case inputs and normalizes to lowercase output
- **Fallback Matching**: Provides simple string matching when spaCy is not available
- **Demo Interface**: Simple command-line demonstration with sample job postings
- **High Precision**: Designed to achieve macro-averaged F1 score ≥ 0.70

## Requirements

- Python 3.12 or higher
- spaCy library with English language model (en_core_web_sm)
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
4. Download the spaCy English language model
5. Set up the project for immediate use

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

4. **Download spaCy language model**:
   ```bash
   uv run python -m spacy download en_core_web_sm
   ```

## Usage

### Command Line Demo

Run the demonstration script to see the technology extraction in action:

```bash
source .venv/bin/activate  # If not already activated
python main.py
```

or run directly with uv:

```bash
uv run python main.py
```

### Programmatic Usage

You can use the extraction function directly in your Python code:

```python
from solution import extract_tech

# Extract technologies from job posting text
job_text = "We need a React & TypeScript engineer familiar with AWS and Docker."
technologies = extract_tech(job_text)
print(technologies)
# Output: {'react', 'typescript', 'aws', 'docker'}
```

## API Reference

### `extract_tech(text: str) -> Set[str]`

Extracts technology terms from the provided text and returns them as a set.

**Parameters:**
- `text` (str): The job posting text to analyze

**Returns:**
- `Set[str]`: A set of lowercase technology terms found in the text

**Example:**
```python
result = extract_tech("Python developer with Django and PostgreSQL experience")
# Returns: {'python', 'django', 'postgresql'}
```

## Technology Coverage

The system recognizes technologies across multiple categories:

### Programming Languages
- **Popular**: Python, JavaScript, TypeScript, Java, C#, Go, Rust
- **Specialized**: R, MATLAB, Scala, Kotlin, Swift, Dart
- **Legacy**: COBOL, FORTRAN, Perl, PHP

### Web Frameworks & Libraries
- **Frontend**: React, Angular, Vue.js, Next.js, Svelte
- **Backend**: Django, Flask, Express.js, Spring, Laravel
- **CSS**: Bootstrap, Tailwind, Bulma, Foundation

### Databases
- **SQL**: PostgreSQL, MySQL, SQLite, Oracle, SQL Server
- **NoSQL**: MongoDB, Redis, Cassandra, DynamoDB
- **Search**: Elasticsearch, Solr

### Cloud Platforms
- **Major**: AWS, Azure, Google Cloud Platform (GCP)
- **Specialized**: Heroku, Vercel, Netlify, Firebase

### DevOps & Tools
- **Containers**: Docker, Kubernetes
- **CI/CD**: Jenkins, GitHub Actions, GitLab CI
- **Monitoring**: Prometheus, Grafana, DataDog

## Example Usage

### Sample Job Postings

```python
# Example 1: Full-stack role
text1 = "We are looking for a Python developer with experience in Django and PostgreSQL."
print(extract_tech(text1))
# Output: {'python', 'django', 'postgresql'}

# Example 2: Frontend position
text2 = "Frontend engineer skilled in React, TypeScript, and GraphQL; familiarity with AWS is a plus."
print(extract_tech(text2))
# Output: {'react', 'typescript', 'graphql', 'aws'}

# Example 3: Data science role
text3 = "Seeking data scientist proficient in PyTorch, TensorFlow, and cloud platforms like GCP."
print(extract_tech(text3))
# Output: {'pytorch', 'tensorflow', 'gcp'}
```

## Project Structure

```
task-01-tech-extract/
├── main.py            # Command-line demonstration
├── solution.py        # Core extraction logic
├── pyproject.toml     # Project configuration
├── setup.sh          # Automated setup script
└── README.md         # This file
```

## Development

### Core Algorithm

The extraction process uses multiple techniques:

1. **Named Entity Recognition**: spaCy NER to identify technology entities in natural language
2. **Entity Filtering**: Focuses on relevant entity types (ORG, PRODUCT, WORK_OF_ART, EVENT)
3. **Technology Matching**: Cross-references identified entities with comprehensive technology database
4. **Variation Handling**: Maps common variations to standard terms
5. **Fallback Matching**: Simple string matching when spaCy is not available
6. **Normalization**: Case-insensitive processing with lowercase output

The system leverages spaCy's advanced NLP capabilities to understand context and identify technology mentions that might be missed by simple keyword matching. When spaCy is unavailable, it gracefully falls back to basic string matching with word boundary checks.

### Sample Data Format

Input data should be in JSONL format:
```json
{"text": "We are looking for a Python developer with experience in Django and PostgreSQL."}
{"text": "Frontend engineer skilled in React, TypeScript, and GraphQL; familiarity with AWS is a plus."}
```

## Performance

- **Target F1 Score**: ≥ 0.70 (macro-averaged)
- **Processing Speed**: Handles typical job postings in milliseconds
- **Memory Usage**: Lightweight with minimal memory footprint
- **Accuracy**: High precision with comprehensive technology coverage
- **NER Enhancement**: Improved context understanding through spaCy integration

## License

This project is part of the TIC43 AI Course and is intended for educational purposes.

## Troubleshooting

### Common Issues

1. **Missing dependencies**: Run `./setup.sh` to install all required packages
2. **spaCy model not found**: Download the English model with `python -m spacy download en_core_web_sm`
3. **Python version**: Ensure you're using Python 3.12 or higher
4. **Virtual environment**: Always activate the virtual environment before running
5. **Empty results**: Check that technology terms are spelled correctly in the input text

### Support

For issues and questions, please refer to the course materials or contact the course instructor.
