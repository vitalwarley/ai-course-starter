# Hallucination Verifier

An AI-powered tool that implements a multi-step verification process to detect and assess hallucinations in AI-generated responses using advanced prompt engineering techniques including Chain of Thought (CoT) reasoning and systematic verification workflows.

## Features

- **Multi-Step Verification Process**: Implements a 3-step verification workflow:
  1. Get initial answer from LLM
  2. Request sources for the answer
  3. Verify answer against sources
- **Chain of Thought (CoT) Reasoning**: Uses step-by-step reasoning to break down complex verification tasks
- **Few-Shot Prompting**: Includes examples to guide the model toward consistent verification patterns
- **Hallucination Detection**: Identifies when AI responses contain false, nonsensical, or unverifiable information
- **Confidence Scoring**: Provides reliability assessment for each verification result
- **Interactive Interface**: Gradio web interface for testing verification workflows
- **Systematic Evaluation**: Measures hallucination detection accuracy on test questions

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
1. Enter a question to verify
2. Click "Verify" to run the hallucination detection process
3. View the verification results, sources, and confidence score

### Command Line Demo

Run the demonstration script to see the verification process in action:

```bash
source .venv/bin/activate  # If not already activated
python main.py
```

or run directly with uv:

```bash
uv run python main.py
```

### Programmatic Usage

You can use the verification function directly in your Python code:

```python
from solution import verify_hallucination

# Verify a question for potential hallucinations
question = "What is the capital of the fictional country Wakanda?"
result = verify_hallucination(question)

print(f"Answer: {result['answer']}")
print(f"Sources: {result['sources']}")
print(f"Is Hallucination: {result['is_hallucination']}")
print(f"Confidence: {result['confidence']:.2f}")
print(f"Reasoning: {result['reasoning']}")
```

## API Reference

### `verify_hallucination(question: str) -> dict`

Implements a multi-step verification process to detect hallucinations in AI responses.

**Parameters:**
- `question` (str): The question to verify for potential hallucinations

**Returns:**
- `dict`: A dictionary containing:
  - `"answer"` (str): The initial AI response
  - `"sources"` (list): List of sources provided by the AI
  - `"is_hallucination"` (bool): Whether the response is likely a hallucination
  - `"confidence"` (float): Confidence score (0.0 to 1.0)
  - `"reasoning"` (str): Detailed explanation of the verification process

**Example:**
```python
result = verify_hallucination("Who invented the computer mouse?")
# Returns: {
#     "answer": "Douglas Engelbart invented the computer mouse in 1964.",
#     "sources": ["Patent documents", "Stanford Research Institute records"],
#     "is_hallucination": False,
#     "confidence": 0.95,
#     "reasoning": "The answer is well-documented and verifiable through multiple sources."
# }
```

## Verification Process

The hallucination verifier implements a systematic 3-step process:

### Step 1: Initial Answer
- Uses Chain of Thought prompting to get a detailed answer
- Includes few-shot examples to guide response format
- Requests the AI to provide reasoning for its answer

### Step 2: Source Verification
- Asks the AI to provide specific sources for its claims
- Uses structured prompting to ensure source quality
- Evaluates the specificity and verifiability of sources

### Step 3: Cross-Verification
- Compares the initial answer against provided sources
- Uses verification prompts to assess consistency
- Calculates confidence score based on source reliability

## Evaluation

The solution includes comprehensive evaluation combining output accuracy, process quality, and LLM-as-Judge assessment:

### Basic Accuracy Evaluation
```python
from solution import evaluate_hallucination_detection

# Prepare test data
test_questions = [
    {
        "question": "Who was the first person to walk on Mars?",
        "expected_hallucination": True
    },
    {
        "question": "What is the capital of France?", 
        "expected_hallucination": False
    }
]

# Run basic accuracy evaluation
results = evaluate_hallucination_detection(test_questions)
print(f"Accuracy: {results['accuracy']:.2%}")
print(f"Correct: {results['correct']}/{results['total']}")
```

### LLM-as-Judge Comprehensive Evaluation
```python
from solution import llm_as_judge_evaluation

# Run comprehensive LLM-as-Judge evaluation
llm_results = llm_as_judge_evaluation(test_questions)

print(f"Performance Level: {llm_results['performance_level']}")
print(f"Binary Accuracy: {llm_results['binary_accuracy']:.2%}")
print(f"Average Output Accuracy: {llm_results['avg_output_accuracy']:.1f}/10")
print(f"Average Reasoning Quality: {llm_results['avg_reasoning_quality']:.1f}/10")
print(f"Average Source Quality: {llm_results['avg_source_quality']:.1f}/10")
print(f"Average Process Methodology: {llm_results['avg_process_methodology']:.1f}/10")
print(f"Average Overall Assessment: {llm_results['avg_overall_assessment']:.1f}/10")
```

### Evaluation Dimensions

The LLM-as-Judge evaluation assesses multiple dimensions:

1. **Output Accuracy (0-10)**: Correctness of hallucination detection
2. **Reasoning Quality (0-10)**: Clarity and logic of Chain of Thought reasoning
3. **Source Quality (0-10)**: Specificity and credibility of provided sources
4. **Process Methodology (0-10)**: Effectiveness of multi-step verification
5. **Confidence Calibration (0-10)**: Appropriateness of confidence scores
6. **Overall Assessment (0-10)**: Holistic system performance

### Performance Levels

Based on the overall assessment score:
- **Excellent** (8.0-10.0): Superior performance across all dimensions
- **Good** (6.5-7.9): Strong performance with minor areas for improvement
- **Adequate** (5.0-6.4): Acceptable performance meeting basic requirements
- **Needs Improvement** (<5.0): Significant issues requiring attention

## Example Usage

### Sample Questions

```python
# Example 1: Factual question
question1 = "What is the largest planet in our solar system?"
result1 = verify_hallucination(question1)
print(f"Is hallucination: {result1['is_hallucination']}")  # Expected: False

# Example 2: Fictional/false information
question2 = "Who was the first person to walk on Mars?"
result2 = verify_hallucination(question2)
print(f"Is hallucination: {result2['is_hallucination']}")  # Expected: True

# Example 3: Ambiguous question
question3 = "What is the best programming language?"
result3 = verify_hallucination(question3)
print(f"Confidence: {result3['confidence']:.2f}")  # Expected: Lower confidence
```

## Project Structure

```
task-05-hallucination-verifier/
├── app.py                    # Gradio web interface
├── solution.py              # Core verification logic
├── main.py                  # Command-line demonstration
├── sample_questions.jsonl   # Test questions for evaluation
├── pyproject.toml          # Project configuration
├── setup.sh                # Automated setup script
└── README.md              # This file
```

## Development

### Core Algorithm

The verification process uses multiple prompt engineering techniques:

1. **Few-Shot Prompting**: Provides examples of good verification patterns
2. **Chain of Thought**: Breaks down verification into logical steps
3. **Systematic Verification**: Cross-references answers with sources
4. **Confidence Assessment**: Evaluates reliability of information

### Prompt Engineering Techniques

- **Initial Answer Prompt**: Uses CoT to get reasoned responses
- **Source Request Prompt**: Asks for specific, verifiable sources
- **Verification Prompt**: Compares answers against sources
- **Few-Shot Examples**: Includes verification examples in prompts

### Sample Data Format

Input questions should be in JSONL format:
```json
{"question": "What is the capital of France?", "expected_hallucination": false}
{"question": "Who was the first person to walk on Mars?", "expected_hallucination": true}
```

## Performance Metrics

- **Hallucination Detection Accuracy**: Measures correct identification of hallucinations
- **Confidence Calibration**: Assesses reliability of confidence scores
- **Processing Time**: Typical verification completes in 3-5 seconds per question

## Prompt Engineering Focus

This task demonstrates key prompt engineering concepts:
- **Multi-step reasoning** with Chain of Thought
- **Few-shot learning** with verification examples
- **Systematic verification** workflows
- **Confidence assessment** techniques

## Troubleshooting

### Common Issues

1. **OpenAI API Key not set**: Ensure your `OPENAI_API_KEY` environment variable is configured
2. **Rate limiting**: The tool may be slower due to OpenAI API rate limits
3. **Model responses**: Results may vary based on the specific model and prompt variations

### Tips for Best Results

- Use specific, factual questions for testing
- Include questions with varying difficulty levels
- Test with both true and false information
- Consider the model's knowledge cutoff date

## License

This project is part of the TIC43 AI Course and is intended for educational purposes. 