# Deep Dive into Prompt Engineering and Documentation - Class Notes

**Date:** [Insert Date]  
**Instructor:** [Insert Instructor Name]  
**Source:** www.vertex.org.br

## Course Content Overview

The class is structured into six main sections:

1. **Introduction to Concepts**
2. **Advanced Prompting Techniques**
3. **Ensuring Model Reliability**
4. **Observability and Guidance Tools**
5. **Practical Demonstration**
6. **Definition of the Individual Task**

---

## 1. Introduction to Concepts

### Important Terminology
* **Hallucination:** A phenomenon where an AI model generates false, nonsensical, or factually incorrect information that was not present in its training data.

* **Few-shot Prompting:** Providing a few examples of the desired input/output format within the prompt itself to guide the model's response.

* **Chain of Thought (CoT):** A prompting technique that encourages the model to generate a series of intermediate reasoning steps before giving a final answer, improving performance on complex tasks.

* **Function Calling:** Enabling a model to connect to external tools and APIs to access real-time information or perform specific actions, extending its capabilities beyond its training data.

* **Model Context Protocol (MCP):** Standardized protocol that defines how the model actions are actually executed and integrated with external systems, ensuring interoperability, tool discovery, and standardization of responses.

### Questions/Clarifications Needed:
[To be filled as content is presented]

---

## 2. Advanced Prompting Techniques

### Overview
Advanced prompting techniques move beyond simple instructions to provide more structured, reliable, and accurate AI interactions through examples and systematic reasoning approaches.

### Technique Categories

#### Few-Shot Prompting
**Description:** Moves beyond simple instructions (zero-shot) by including examples to show the model exactly what you want  
**Use Cases:** When you need consistent output format and accuracy for specific tasks  
**Key Benefit:** Improves output format consistency and accuracy for specific tasks  
**Example Template:**
```
System: Translate to Portuguese:
■ car -> carro
■ house -> casa
User: dog
Assistant: cachorro
```

#### Chain of Thought (CoT)
**Description:** Breaks down complex problems into smaller, logical steps by making the model "think step by step"  
**Use Cases:** Math, logic, and multi-step problem solving  
**Key Benefit:** Enhances reasoning ability, leading to more accurate answers for complex problems  
**Example Template:**
```
User: John has 5 apples, he gives 2 to Jane and eats 1. 
How many are left? Let's think step by step.

1. John starts with 5 apples.
2. He gives 2 away, so 5 - 2 = 3.
3. He eats 1, so 3 - 1 = 2.
Assistant: John has 2 apples left.
```

### Template Examples

```
Few-Shot Template:
System: [Task description]:
■ [Example 1 input] -> [Example 1 output]
■ [Example 2 input] -> [Example 2 output]
User: [New input]
```

```
Chain of Thought Template:
User: [Complex problem]. Let's think step by step.
1. [Step 1 reasoning]
2. [Step 2 reasoning]  
3. [Step 3 reasoning]
Assistant: [Final answer]
```

---

## 3. Ensuring Model Reliability

### Reliability Challenges
Hallucinations are a major challenge in production systems, requiring systematic approaches to ensure factual accuracy and consistent performance.

### Function Calling and MCP

#### Core Functionality
**Method:** Gives the LLM access to external tools (APIs, databases)  
**Implementation:** The model decides if and how to call a function you provide  
**Key Benefit:** Grounds the model in real-world, up-to-date information, overcoming knowledge cutoffs  

**Example Use Cases:**
- Chatbot using a function to check real-time stock prices
- Weather forecast integration
- Database queries for current information

### Hallucination Mitigation Strategies

#### Strategy 1: Grounding
**Method:** Base prompts on retrieved, factual documents (RAG)  
**Implementation:** Retrieve relevant documents before generating responses  
**Purpose:** Provide factual foundation for model responses

#### Strategy 2: Verification  
**Method:** Use a second LLM call to check the first answer for factual consistency  
**Implementation:** Cross-validation between multiple model calls  
**Purpose:** Quality assurance through independent verification

#### Strategy 3: Constrained Generation
**Method:** Use tools to force the model to generate output in a specific, valid format  
**Implementation:** JSON schema validation, structured output requirements  
**Purpose:** Ensure technical accuracy and format compliance

#### Strategy 4: Precise Prompting
**Method:** Employing well-defined guidelines and techniques like CoT and Few-shot in prompt design  
**Implementation:** Systematic prompt engineering with examples and step-by-step reasoning  
**Purpose:** Diminishes the likelihood of hallucinations through clear guidance

### Validation Techniques
* **RAG (Retrieval-Augmented Generation):** Ground responses in factual documents
* **Multi-LLM Verification:** Cross-check answers with secondary models
* **Structured Output Validation:** Force compliance with predefined formats
* **Systematic Prompt Design:** Use CoT and Few-shot techniques consistently

---

## 4. Observability and Guidance Tools

### Why Observability Matters
Tools are essential for debugging, monitoring, and controlling LLM-based applications, providing detailed insights into model performance and behavior.

### Tool Categories

#### Debugging & Monitoring Platforms
**LangSmith:**  
**Purpose:** Platform for debugging, testing, evaluating, and monitoring flows (chains) and intelligent agents built on any LLM framework  
**Integration:** Works with any LLM framework  
**Outputs:** Detailed analysis and execution tracing for comprehensive debugging

**LangFuse:**  
**Purpose:** Open source platform for LLM engineering that allows you to track, debug, and collect detailed metrics in complex applications  
**Integration:** Designed for complex application environments  
**Outputs:** Detailed metrics for continuous improvement of models and flows

#### Programming & Control Tools  
**Guidance:**  
**Purpose:** Programming paradigm developed by Microsoft that offers greater control and efficiency in building prompts for LLMs  
**Integration:** Microsoft-developed framework for prompt engineering  
**Outputs:** Ensures valid syntax and facilitates creation of complex and conditional instructions

#### Model Health & Performance
**Phoenix:**  
**Purpose:** Open source library focused on machine learning observability  
**Integration:** Production environment monitoring  
**Outputs:** Helps detect and correct failures in models, including data drift and performance issues during production

### Key Metrics to Track
* **Execution Tracing:** Detailed analysis of prompt flows and agent behavior
* **Performance Metrics:** Model response quality and accuracy measurements  
* **Data Drift Detection:** Monitoring for changes in input patterns over time
* **Syntax Validation:** Ensuring prompt structure and format compliance

---

## 5. Practical Demonstration

### Demonstration Goal
Test multiple prompt styles for accuracy on a Q&A task to compare effectiveness of different prompting techniques.

### Setup Requirements
**Prerequisites:** Python environment with textwrap library and agent framework  
**Environment:** Development environment with tracing capabilities  
**Dependencies:** 
- `textwrap` for text formatting
- Agent system with OpenAI integration
- Tracing provider for observability

#### Step 1: Define the Test Question
```python
TASK = "Who was the person that created the GAN architecture?"
```

#### Step 2: Craft Two Different Prompt Approaches

**Prompt A (Without Samples):**
```python
WITHOUT_SAMPLES_PROMPT = """
<Persona> You are an expert in history and recent events.</Persona>
<Guidelines> Answer the question simply, direct and straightforward. Do not make up information. Only answer the question, in the most simple way possible. Add the word "Answer:" before the answer. </Guidelines>
"""
```

**Prompt B (Few-shot with Examples):**
```python
WITH_SAMPLES_PROMPT = """
<Persona> You are an expert in history and recent events.</Persona>
<Guidelines> Answer the question simply, direct and straightforward. Do not make up information. Only answer the question, in the most simple way possible. Add the word "Answer:" before the answer. </Guidelines>
<Samples>
1. Who is the actual president of the USA?
   Answer: Donald Trump
2. What is the capital of France?
   Answer: Paris
3. Where is the Silicon Valley?
   Answer: California, USA
4. Whats the newest version of Python?
   Answer: Python 3.12
</Samples>
"""
```

#### Step 3: Implementation with Agent System
```python
# Setup tracing for observability
tracer_provider = register(
    project_name="TICU3",
    auto_instrument=True,
    protocol="http/protobuf"
)
tracer = tracer_provider.get_tracer(__name__)

# Create agents with different prompts
cot_agent = Agent(
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    model=OpenAIChat(id="gpt-4o-mini", system_prompt=WITH_SAMPLES_PROMPT)
)

without_cot_agent = Agent(
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    model=OpenAIChat(id="gpt-4o-mini", system_prompt=WITHOUT_SAMPLES_PROMPT)
)

# Execute both approaches
cot_agent.print_response(message=TASK)
without_cot_agent.print_response(message=TASK)
```

#### Step 4: Output Comparison and Analysis

**Evaluation Criteria:**
- Which prompt gives a more structured, accurate, and detailed answer?
- Does one style reduce the risk of irrelevant information?

### Expected Results
```
Demo Output Comparison:

Response 1 (3.6s - Without Samples):
Answer: Ian Goodfellow

Response 2 (2.1s - Few-shot with Samples):  
Answer: The GAN (Generative Adversarial Network) architecture was created by Ian Goodfellow in 2014.

Key Observations:
- Few-shot approach provided more detailed, contextual information
- Response time was actually faster for the few-shot approach (2.1s vs 3.6s)
- Format consistency maintained in both responses with "Answer:" prefix
- Few-shot version included important context (full form of GAN, year created)
```

### Key Takeaways from Demo
* **Structured Comparison:** Direct A/B testing of prompting techniques reveals effectiveness differences
* **Tracing Integration:** Observability tools provide detailed insights into agent execution and decision-making
* **Format Consistency:** Few-shot examples significantly improve output format adherence
* **Real-world Testing:** Using concrete questions allows measurable assessment of technique effectiveness

### Troubleshooting Notes
- Ensure proper agent configuration with correct model parameters
- Verify tracing setup for comprehensive monitoring
- Test with multiple questions to validate consistency across different topics

---

## 6. Definition of the Individual Task

### Project Overview
Choose one of two practical projects that apply the prompt engineering techniques learned in this course.

### Project Options

#### **Option 1: Build a Hallucination Verifier**
**Description:** Develop a multi-step process to verify if a model hallucinates

**Technical Requirements:**
* **Step 1:** Ask the LLM a question to get an initial response
* **Step 2:** Ask the model to provide sources for its answer
* **Step 3:** Ask the model to verify its answer against the provided sources
* **Implementation:** Create a systematic verification workflow using multiple LLM calls

#### **Option 2: Create an Invoice Parser**
**Description:** Build a robust prompt to parse unstructured text from invoices into structured JSON format

**Technical Requirements:**
* **Input:** Unstructured text from invoices
* **Output:** Structured JSON format
* **Required Fields:** 
  - Vendor name
  - Date
  - Total amount
  - Line items
* **Implementation:** Design prompts that handle various invoice formats reliably

### Deliverables
* **[Deliverable 1]:** Working implementation of chosen project
* **[Deliverable 2]:** Documentation of prompt engineering techniques used
* **[Deliverable 3]:** Test cases demonstrating effectiveness and reliability

### Evaluation Criteria
* **[Criterion 1]:** Correct application of prompt engineering techniques (Few-shot, CoT, etc.)
* **[Criterion 2]:** Implementation of reliability measures (verification, structured output)
* **[Criterion 3]:** Code quality and documentation
* **[Criterion 4]:** Effectiveness testing and validation

### Timeline and Milestones
* **[Milestone 1]:** Project selection and initial design
* **[Milestone 2]:** Implementation with basic functionality
* **[Milestone 3]:** Testing, refinement, and final documentation

### Resources Provided
* Course examples and templates
* Access to observability tools (LangSmith, LangFuse)
* Reference implementations from practical demonstration

**Special Notes:** Both projects directly apply the core concepts covered: hallucination mitigation, structured output generation, and systematic prompt engineering approaches.

---

## Summary & Key Takeaways

### Most Important Concepts:
1. **Few-Shot Prompting** - Providing examples dramatically improves output consistency and accuracy, as demonstrated with 2.1s response time vs 3.6s for zero-shot
2. **Chain of Thought (CoT)** - Step-by-step reasoning enhances performance on complex tasks requiring logical thinking and problem-solving
3. **Hallucination Mitigation** - Multi-layered approach using grounding (RAG), verification, constrained generation, and precise prompting to ensure reliability
4. **Function Calling with MCP** - Extending LLM capabilities with real-time data access through standardized protocols for production systems

### Actionable Implementation Tips:
* Use few-shot examples with specific input/output formats for consistent results
* Implement "Let's think step by step" for complex reasoning tasks
* Set up verification workflows using multiple LLM calls for fact-checking
* Integrate observability tools (LangSmith, LangFuse) from the start for debugging and monitoring
* Apply constrained generation with JSON schemas for structured outputs
* Combine techniques - use CoT with Few-shot for maximum effectiveness

### Follow-up Questions for Deeper Understanding:
* How do you balance the cost of multiple verification calls with reliability requirements?
* What are the optimal prompt structures for different types of reasoning tasks?
* How do you measure and quantify hallucination reduction in production systems?
* Which observability metrics are most predictive of model performance issues?

### Additional Resources to Explore:
* LangSmith documentation for advanced debugging workflows
* Microsoft Guidance library for structured prompt engineering
* Phoenix ML observability best practices
* RAG implementation patterns with vector databases
* JSON schema validation for constrained generation
* Production deployment strategies for multi-agent systems

---

## Personal Reflections

### What surprised me:
* [To be filled during/after class]

### Areas I want to practice more:
* [To be filled during/after class]

### How I'll apply this knowledge:
* [To be filled during/after class]

### Connections to previous learning:
* [To be filled during/after class]

### Questions to explore further:
* [To be filled during/after class]

---

## Action Items
- [ ] [Action item 1]
- [ ] [Action item 2]
- [ ] [Action item 3]
- [ ] [Action item 4]

**Next Steps:** [What to do immediately after this class]