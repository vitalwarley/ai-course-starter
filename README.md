# AI Course Starter - TIC43 Course

A comprehensive collection of AI and prompt engineering tasks designed for students learning practical AI implementation, featuring automated evaluation and scalable grading workflows.

## 🎯 Project Overview

This repository contains a series of progressively challenging AI tasks organized by class sessions, each focusing on different aspects of prompt engineering, AI model implementation, and evaluation methodologies.

### **Key Features**
- **Class-based Organization**: Tasks grouped by course sessions (class_3, class_4, class_5)
- **Comprehensive Evaluation**: Dual evaluation approach combining output accuracy and LLM-as-Judge assessment
- **Prompt Engineering Focus**: Demonstrates Chain of Thought, Few-shot prompting, and systematic verification
- **Automated Grading**: Scalable CI/CD pipeline for assessment
- **Production-Ready**: Complete implementations with web interfaces and robust error handling

## 📚 Course Structure

### **Class 3: Foundation Tasks**
- **Task 01 - Technology Extraction**: Extract technologies from job postings using NLP techniques
- **Task 02 - Ticket Classification**: Multi-task learning for entity extraction and classification

### **Class 4: Applied AI Systems**
- **Task 01 - Code Refactorer**: Intelligent code refactoring with LLM assistance
- **Task 02 - Voice Transcribe**: Speech-to-text processing with AI enhancement

### **Class 5: Advanced Prompt Engineering**
- **Task 01 - Hallucination Verifier**: Multi-step verification system using Chain of Thought
- **Task 02 - Invoice Parser**: Structured data extraction using Few-shot prompting

## 🔧 Repository Architecture

### **Public Starter Repo** (this repo)
- **Task Folders**: Organized as `class_N/task-NN-name/` with proper numbering within each class
- **Complete Implementations**: Production-ready solutions with comprehensive documentation
- **Sample Data**: Representative datasets for testing and evaluation
- **Automated Setup**: Shell scripts for environment configuration
- **Web Interfaces**: Gradio-based UIs for interactive testing

### **Private Evaluation Repo** (`ai-course-eval`)
- **Hidden Test Suites**: Comprehensive evaluation datasets
- **Automated Grading**: Pytest-based testing with custom metrics
- **LLM-as-Judge Integration**: Advanced evaluation using AI assessors

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- OpenAI API key (for Class 5 tasks)
- Git

### Quick Setup
```bash
# Clone the repository
git clone https://github.com/your-username/ai-course-starter.git
cd ai-course-starter

# Navigate to any task
cd class_5/task-01-hallucination-verifier

# Run automated setup
./setup.sh

# Start the demo
python main.py
```

## 📊 Evaluation Methodology

### **LLM-as-Judge Comprehensive Evaluation**

All tasks are evaluated using an advanced LLM-as-Judge system that provides scalable, comprehensive assessment across multiple dimensions:

**Universal Evaluation Dimensions:**
- **Output Quality** (25%): Correctness and completeness of results
- **Process Methodology** (25%): Effectiveness of prompt engineering techniques
- **Reasoning Clarity** (20%): Logical flow and explanatory quality
- **Error Handling** (15%): Robustness with edge cases and malformed input
- **Overall Assessment** (15%): Holistic system performance

**Task-Specific Focus Areas:**
- **Class 3**: NLP accuracy, entity recognition, classification quality
- **Class 4**: Code quality, refactoring effectiveness, transcription accuracy
- **Class 5**: Chain-of-thought reasoning, few-shot prompting, verification methodology

### **Performance Categorization**
- **Excellent** (8.0-10.0): Superior performance across all dimensions
- **Good** (6.5-7.9): Strong performance with minor improvements needed
- **Adequate** (5.0-6.4): Acceptable performance meeting basic requirements
- **Needs Improvement** (<5.0): Significant issues requiring attention

## 🛠 CI/CD Workflow

### **Automated Grading Pipeline**
1. **Fork → PR → Grade**: Students fork, implement, and submit via Pull Request
2. **Safety First**: Uses `pull_request_target` event to protect secrets
3. **Smart Detection**: Differential analysis identifies changed tasks
4. **Matrix Execution**: Parallel testing of modified tasks only
5. **Comprehensive Feedback**: Detailed results posted as PR comments

### **Cost Optimization**
- **Selective Testing**: Only runs tests for changed tasks
- **Parallel Execution**: Multiple tasks tested simultaneously  
- **Minimal Tutor Intervention**: Automated pass/fail with detailed metrics

## 📋 Task Details

### **Class 3: Foundation (NLP & Classification)**

#### Task 01 - Technology Extraction
- **Objective**: Extract technology stack from job posting text
- **Techniques**: Named Entity Recognition, spaCy integration
- **Evaluation**: LLM-as-Judge assessment of extraction accuracy and completeness
- **Sample Data**: Job postings with technology annotations

#### Task 02 - Ticket Classification  
- **Objective**: Multi-task entity extraction and ticket categorization
- **Techniques**: Joint learning, multi-label classification
- **Evaluation**: LLM-as-Judge assessment of entity extraction and classification quality
- **Sample Data**: Support tickets with entity and category labels

### **Class 4: Applied Systems (Code & Speech)**

#### Task 01 - Code Refactorer
- **Objective**: Intelligent code improvement and restructuring
- **Techniques**: AST analysis, LLM-guided refactoring
- **Evaluation**: LLM-as-Judge assessment of code quality improvements and functional preservation
- **Interface**: Gradio web application for interactive refactoring

#### Task 02 - Voice Transcribe
- **Objective**: Speech-to-text with AI enhancement
- **Techniques**: Audio processing, transcription refinement
- **Evaluation**: LLM-as-Judge assessment of transcription accuracy and enhancement quality
- **Features**: Multiple audio format support, noise handling

### **Class 5: Advanced Prompting (Verification & Extraction)**

#### Task 01 - Hallucination Verifier
- **Objective**: Multi-step AI response verification system
- **Techniques**: Chain of Thought, Few-shot prompting, systematic verification
- **Process**: Initial answer → Source gathering → Cross-verification
- **Evaluation**: LLM-as-Judge assessment of detection accuracy, reasoning quality, and verification methodology

#### Task 02 - Invoice Parser
- **Objective**: Structured data extraction from unstructured invoices
- **Techniques**: Few-shot prompting, constrained generation, JSON schema validation
- **Output**: Vendor details, line items, totals with confidence scoring
- **Evaluation**: LLM-as-Judge assessment of field extraction accuracy, format consistency, and robustness

## 📈 Metrics & Assessment

### **LLM-as-Judge Evaluation System**
Our scalable evaluation framework uses GPT-4 as an expert assessor to provide comprehensive feedback across five key dimensions:

- **Output Quality**: Correctness and completeness of results
- **Process Methodology**: Effectiveness of prompt engineering techniques
- **Reasoning Clarity**: Logical flow and explanatory quality
- **Error Handling**: Robustness with edge cases and malformed input
- **Overall Assessment**: Holistic system performance

### **Evaluation Benefits**
- **Scalable**: No need for perfect gold standard datasets
- **Comprehensive**: Evaluates both output and process quality
- **Consistent**: Standardized scoring criteria across all tasks
- **Detailed**: Provides specific improvement suggestions
- **Flexible**: Easy to add new evaluation dimensions

## 🔄 Development Workflow

### **For Students**
1. Fork the repository
2. Choose a task from any class
3. Run `./setup.sh` for automated environment setup
4. Implement the solution in `solution.py`
5. Test with `python main.py` and web interface
6. Submit via Pull Request

### **For Instructors**
1. Review automated evaluation results
2. Focus on edge cases flagged by CI
3. Provide targeted feedback on prompt engineering techniques
4. Monitor performance trends across cohorts

## 📁 Project Structure

```
ai-course-starter/
├── class_3/                    # Foundation NLP tasks
│   ├── task-01-tech-extract/   # Technology extraction
│   └── task-02-ticket-classify/ # Ticket classification
├── class_4/                    # Applied AI systems
│   ├── task-01-code-refactorer/ # Code refactoring
│   └── task-02-voice-transcribe/ # Speech processing
├── class_5/                    # Advanced prompt engineering
│   ├── task-01-hallucination-verifier/ # Response verification
│   └── task-02-invoice-parser/  # Structured extraction
├── student/                    # Student workspace (mirrors structure)
├── tools/                      # Utility scripts
└── README.md                   # This file
```

### **Individual Task Structure**
```
task-NN-name/
├── solution.py        # Main implementation
├── main.py           # Command-line demo
├── app.py            # Gradio web interface
├── README.md         # Task-specific documentation
├── pyproject.toml    # Dependencies and configuration
├── setup.sh          # Automated environment setup
└── sample_*.jsonl    # Test data and examples
```

## 🎓 Learning Objectives

### **Prompt Engineering Mastery**
- **Chain of Thought**: Step-by-step reasoning for complex problems
- **Few-shot Learning**: Learning from examples within prompts
- **Systematic Verification**: Multi-step validation workflows
- **Constrained Generation**: Structured output with schema compliance

### **Production AI Skills**
- **Error Handling**: Robust systems with graceful degradation
- **Evaluation Design**: Comprehensive assessment methodologies
- **Interface Development**: User-friendly AI application interfaces
- **Performance Optimization**: Efficient prompt and model usage

### **Quality Assurance**
- **Comprehensive Testing**: Multiple evaluation approaches
- **Confidence Scoring**: Uncertainty quantification in AI outputs
- **Validation Workflows**: Systematic quality assessment
- **Continuous Improvement**: Iterative refinement based on feedback

## 🏆 Success Criteria

### **Technical Excellence**
- All tasks pass automated evaluation thresholds
- Comprehensive documentation and code quality
- Robust error handling and edge case management
- Effective prompt engineering technique application

### **Process Mastery**
- Clear reasoning and methodology explanation
- Appropriate use of AI evaluation techniques
- Thoughtful confidence calibration
- Scalable and maintainable implementation

## 📞 Support & Resources

- **Course Documentation**: Individual task READMEs with detailed instructions
- **Interactive Demos**: Web interfaces for immediate testing and feedback
- **Automated Setup**: Zero-configuration environment preparation
- **Comprehensive Examples**: Sample data and reference implementations

## 🎯 Outcome

This comprehensive course structure supports **unlimited scalable growth** with:
- **Automated Assessment**: Minimal instructor workload for routine grading
- **Quality Focus**: Instructor attention directed to meaningful feedback
- **Progressive Difficulty**: Structured learning path from foundations to advanced techniques
- **Production Readiness**: Real-world applicable skills and implementations

The system successfully balances **accessibility for beginners** with **meaningful depth**, creating an optimal learning environment for AI and prompt engineering mastery.