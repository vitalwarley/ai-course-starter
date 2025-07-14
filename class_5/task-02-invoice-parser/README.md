# Invoice Parser

An AI-powered tool that uses advanced prompt engineering techniques to parse unstructured invoice text into structured JSON format. This tool demonstrates few-shot prompting, structured output generation, and constrained generation techniques to reliably extract key information from various invoice formats.

## Features

- **Structured JSON Output**: Converts unstructured invoice text into consistent JSON format
- **Few-Shot Prompting**: Uses examples to guide the model toward consistent parsing patterns
- **Constrained Generation**: Ensures output follows predefined JSON schema
- **Field Extraction**: Extracts key fields including:
  - Vendor name
  - Invoice date
  - Total amount
  - Line items (description, quantity, price)
  - Invoice number
  - Customer information
- **Error Handling**: Gracefully handles malformed or incomplete invoices
- **Confidence Scoring**: Provides reliability assessment for extracted data
- **Interactive Interface**: Gradio web interface for testing invoice parsing
- **Multiple Format Support**: Handles various invoice layouts and formats

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

or run directly with uv:

```bash
uv run app.py
```

The interface will be available at `http://localhost:7860` where you can:
1. Paste invoice text in the input field
2. Click "Parse Invoice" to extract structured data
3. View the parsed JSON output and confidence score

### Command Line Demo

Run the demonstration script to see the parsing process in action:

```bash
source .venv/bin/activate  # If not already activated
python main.py
```

or run directly with uv:

```bash
uv run python main.py
```

### Programmatic Usage

You can use the parsing function directly in your Python code:

```python
from solution import parse_invoice

# Parse an invoice text
invoice_text = """
INVOICE #12345
Date: 2024-01-15
From: TechCorp Solutions
To: Client Company

Item: Software License - 2 units @ $500.00 each
Item: Support Services - 1 unit @ $200.00 each

Total: $1,200.00
"""

result = parse_invoice(invoice_text)
print(result)
```

## API Reference

### `parse_invoice(invoice_text: str) -> dict`

Parses unstructured invoice text into structured JSON format.

**Parameters:**
- `invoice_text` (str): The raw invoice text to parse

**Returns:**
- `dict`: A structured dictionary containing:
  - `"vendor_name"` (str): Name of the vendor/company
  - `"invoice_number"` (str): Invoice number or ID
  - `"date"` (str): Invoice date
  - `"total_amount"` (float): Total amount due
  - `"line_items"` (list): List of items with description, quantity, price
  - `"customer_info"` (str): Customer/client information
  - `"confidence"` (float): Confidence score (0.0 to 1.0)

**Example:**
```python
result = parse_invoice(invoice_text)
# Returns: {
#     "vendor_name": "TechCorp Solutions",
#     "invoice_number": "12345",
#     "date": "2024-01-15",
#     "total_amount": 1200.00,
#     "line_items": [
#         {"description": "Software License", "quantity": 2, "price": 500.00},
#         {"description": "Support Services", "quantity": 1, "price": 200.00}
#     ],
#     "customer_info": "Client Company",
#     "confidence": 0.95
# }
```

## Parsing Process

The invoice parser implements systematic extraction using prompt engineering:

### Step 1: Text Preprocessing
- Cleans and normalizes input text
- Handles various formatting inconsistencies
- Identifies key sections and patterns

### Step 2: Few-Shot Parsing
- Uses examples to guide extraction patterns
- Demonstrates proper JSON structure
- Shows handling of edge cases

### Step 3: Structured Extraction
- Extracts each field systematically
- Validates data types and formats
- Ensures JSON schema compliance

### Step 4: Quality Assessment
- Calculates confidence scores
- Identifies potential parsing issues
- Provides extraction reliability metrics

## Evaluation

The solution includes comprehensive evaluation combining output accuracy, process quality, and LLM-as-Judge assessment:

### Basic Field Accuracy Evaluation
```python
from solution import evaluate_invoice_parsing

# Prepare test data
test_invoices = [
    {
        "invoice_text": "INVOICE #12345\nDate: 2024-01-15\nFrom: TechCorp...",
        "expected_vendor_name": "TechCorp",
        "expected_invoice_number": "12345",
        "expected_date": "2024-01-15",
        "expected_total_amount": 1200.00,
        "expected_line_items": [
            {"description": "Software License", "quantity": 2, "price": 500.00}
        ]
    }
]

# Run basic field accuracy evaluation
results = evaluate_invoice_parsing(test_invoices)
print(f"Overall Accuracy: {results['overall_accuracy']:.2%}")
print(f"Vendor Name Accuracy: {results['vendor_name_accuracy']:.2%}")
print(f"Total Amount Accuracy: {results['total_amount_accuracy']:.2%}")
```

### LLM-as-Judge Comprehensive Evaluation
```python
from solution import llm_as_judge_evaluation

# Run comprehensive LLM-as-Judge evaluation
llm_results = llm_as_judge_evaluation(test_invoices)

print(f"Performance Level: {llm_results['performance_level']}")
print(f"Average Field Accuracy: {llm_results['avg_field_accuracy']:.2%}")
print(f"Average Extraction Accuracy: {llm_results['avg_extraction_accuracy']:.1f}/10")
print(f"Average Data Completeness: {llm_results['avg_data_completeness']:.1f}/10")
print(f"Average Format Consistency: {llm_results['avg_format_consistency']:.1f}/10")
print(f"Average Process Methodology: {llm_results['avg_process_methodology']:.1f}/10")
print(f"Average Overall Assessment: {llm_results['avg_overall_assessment']:.1f}/10")
```

### Evaluation Dimensions

The LLM-as-Judge evaluation assesses multiple dimensions:

1. **Extraction Accuracy (0-10)**: Correctness of field extraction from invoice text
2. **Data Completeness (0-10)**: How complete the extracted information is
3. **Format Consistency (0-10)**: JSON structure and data type consistency
4. **Process Methodology (0-10)**: Effectiveness of few-shot prompting approach
5. **Error Handling (0-10)**: Robustness with edge cases and malformed input
6. **Overall Assessment (0-10)**: Holistic system performance

### Performance Levels

Based on the overall assessment score:
- **Excellent** (8.0-10.0): Superior performance across all dimensions
- **Good** (6.5-7.9): Strong performance with minor areas for improvement
- **Adequate** (5.0-6.4): Acceptable performance meeting basic requirements
- **Needs Improvement** (<5.0): Significant issues requiring attention

## Example Usage

### Sample Invoices

```python
# Example 1: Standard invoice
invoice1 = """
INVOICE #INV-2024-001
Date: March 15, 2024
ABC Company
123 Main Street

Bill To: XYZ Corp
456 Oak Avenue

Description: Web Development Services
Quantity: 40 hours
Rate: $100/hour
Amount: $4,000.00

Total: $4,000.00
"""

result1 = parse_invoice(invoice1)
print(f"Vendor: {result1['vendor_name']}")
print(f"Total: ${result1['total_amount']:.2f}")

# Example 2: Multiple line items
invoice2 = """
TechSupport Pro
Invoice: TSP-2024-0123
Date: 2024-02-20

To: StartupCorp

1. Server Setup - 1 x $500.00 = $500.00
2. Domain Registration - 1 x $15.00 = $15.00
3. SSL Certificate - 1 x $89.00 = $89.00

TOTAL: $604.00
"""

result2 = parse_invoice(invoice2)
print(f"Line items: {len(result2['line_items'])}")
print(f"Confidence: {result2['confidence']:.2f}")
```

## Project Structure

```
task-06-invoice-parser/
├── app.py                # Gradio web interface
├── solution.py          # Core parsing logic
├── main.py              # Command-line demonstration
├── sample_invoices.jsonl # Test invoices for evaluation
├── pyproject.toml       # Project configuration
├── setup.sh             # Automated setup script
└── README.md           # This file
```

## Development

### Core Algorithm

The parsing process uses multiple prompt engineering techniques:

1. **Few-Shot Prompting**: Provides examples of proper parsing patterns
2. **Structured Output**: Ensures consistent JSON schema compliance
3. **Field Validation**: Validates extracted data types and formats
4. **Confidence Assessment**: Evaluates extraction reliability

### Prompt Engineering Techniques

- **Parsing Prompt**: Uses few-shot examples to guide extraction
- **Schema Validation**: Ensures JSON structure compliance
- **Error Handling**: Gracefully handles malformed inputs
- **Confidence Scoring**: Assesses extraction reliability

### Sample Data Format

Input invoices should be in JSONL format for testing:
```json
{"invoice_text": "INVOICE #12345...", "expected_vendor": "TechCorp", "expected_total": 1200.00}
```

## Performance Metrics

- **Field Extraction Accuracy**: Measures correct extraction of key fields
- **JSON Schema Compliance**: Ensures output format consistency
- **Processing Time**: Typical parsing completes in 2-3 seconds per invoice
- **Confidence Calibration**: Assesses reliability of confidence scores

## Field Extraction Details

### Required Fields
- **vendor_name**: Company or individual issuing the invoice
- **invoice_number**: Unique identifier for the invoice
- **date**: Invoice date (normalized to YYYY-MM-DD format)
- **total_amount**: Total amount due (as float)
- **line_items**: Array of items with description, quantity, and price

### Optional Fields
- **customer_info**: Client or customer information
- **due_date**: Payment due date
- **tax_amount**: Tax amounts if specified
- **payment_terms**: Payment terms and conditions

## Prompt Engineering Focus

This task demonstrates key prompt engineering concepts:
- **Few-shot learning** with invoice parsing examples
- **Structured output generation** with JSON schema
- **Constrained generation** techniques
- **Error handling** and robustness

## Troubleshooting

### Common Issues

1. **OpenAI API Key not set**: Ensure your `OPENAI_API_KEY` environment variable is configured
2. **Parsing errors**: Some invoices may have unusual formats that require manual review
3. **Confidence scores**: Low confidence may indicate unclear or incomplete invoice text

### Tips for Best Results

- Use clear, well-formatted invoice text
- Ensure key information (vendor, total, date) is present
- Test with various invoice formats
- Review confidence scores for quality assessment

## License

This project is part of the TIC43 AI Course and is intended for educational purposes. 