"""Starter stub for Task 05 – Hallucination Verifier.

Complete `verify_hallucination` so that it implements a multi-step verification process
to detect hallucinations in AI responses using prompt engineering techniques.

This task demonstrates:
- Chain of Thought (CoT) reasoning
- Few-shot prompting with verification examples
- Multi-step verification workflows
- Systematic hallucination detection

Example:
    >>> result = verify_hallucination("Who was the first person to walk on Mars?")
    >>> result['is_hallucination']
    True
    >>> result['confidence']
    0.95
"""

from typing import Dict, List, Any
import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def verify_hallucination(question: str) -> Dict[str, Any]:
    """
    Implement a multi-step verification process to detect hallucinations.
    
    This function should:
    1. Get an initial answer from the LLM using Chain of Thought
    2. Request sources for the answer
    3. Verify the answer against the sources
    4. Return a comprehensive verification result
    
    Args:
        question (str): The question to verify for potential hallucinations
        
    Returns:
        Dict[str, Any]: A dictionary containing:
            - "answer" (str): The initial AI response
            - "sources" (List[str]): List of sources provided by the AI
            - "is_hallucination" (bool): Whether the response is likely a hallucination
            - "confidence" (float): Confidence score (0.0 to 1.0)
            - "reasoning" (str): Detailed explanation of the verification process
    """
    
    # Step 1: Get initial answer with Chain of Thought reasoning
    initial_answer = _get_initial_answer(question)
    
    # Step 2: Request sources for the answer
    sources = _get_sources(question, initial_answer)
    
    # Step 3: Verify answer against sources
    verification_result = _verify_against_sources(question, initial_answer, sources)
    
    return {
        "answer": initial_answer,
        "sources": sources,
        "is_hallucination": verification_result["is_hallucination"],
        "confidence": verification_result["confidence"],
        "reasoning": verification_result["reasoning"]
    }

def _get_initial_answer(question: str) -> str:
    """
    Get initial answer using Chain of Thought prompting with few-shot examples.
    """
    
    # Few-shot prompting with Chain of Thought examples
    system_prompt = """You are an expert knowledge assistant. Answer questions using step-by-step reasoning.

Examples:
1. Question: "What is the capital of France?"
   Let me think step by step:
   - France is a country in Europe
   - Capital cities are the main administrative centers
   - Paris is widely known as France's capital
   - This is basic geographical knowledge
   Answer: Paris is the capital of France.

2. Question: "Who invented the telephone?"
   Let me think step by step:
   - The telephone was invented in the 1870s
   - Alexander Graham Bell is credited with the invention
   - He received the first U.S. patent for the telephone in 1876
   - This is well-documented historical fact
   Answer: Alexander Graham Bell invented the telephone in 1876.

3. Question: "What is the population of Mars?"
   Let me think step by step:
   - Mars is a planet in our solar system
   - Mars is currently uninhabited by humans
   - There are no permanent settlements on Mars
   - Therefore, Mars has no human population
   Answer: Mars has no human population as it is currently uninhabited.

Now answer the following question using the same step-by-step approach:"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Question: {question}"}
            ],
            temperature=0.1,
            max_tokens=500
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Error getting initial answer: {str(e)}"

def _get_sources(question: str, answer: str) -> List[str]:
    """
    Request specific sources for the given answer.
    """
    
    source_prompt = """You are a research assistant. For the given question and answer, provide specific sources that could verify this information.

List 3-5 specific sources that would contain this information. Be specific about:
- Type of source (academic paper, book, website, database, etc.)
- Specific title or name when possible
- Institution or organization
- For historical facts, mention specific documents or archives

Format your response as a simple list:
1. [Source 1]
2. [Source 2]
3. [Source 3]
etc.

Examples:
For "Who invented the telephone?":
1. U.S. Patent Office records - Patent No. 174,465 (March 7, 1876)
2. Library of Congress - Alexander Graham Bell Family Papers
3. Smithsonian Institution - National Museum of American History
4. Encyclopedia Britannica - Telephone invention entry
5. IEEE History Center - Bell telephone documentation

For "What is the capital of France?":
1. Official French government website (gouvernement.fr)
2. UNESCO World Heritage Centre - Paris documentation
3. Encyclopedia Britannica - France country profile
4. CIA World Factbook - France entry
5. French Constitution - Article on national capital

Now provide sources for:"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": source_prompt},
                {"role": "user", "content": f"Question: {question}\nAnswer: {answer}"}
            ],
            temperature=0.1,
            max_tokens=400
        )
        
        sources_text = response.choices[0].message.content.strip()
        # Parse the numbered list into a list of sources
        sources = []
        for line in sources_text.split('\n'):
            line = line.strip()
            if line and (line[0].isdigit() or line.startswith('-')):
                # Remove numbering and extract source
                source = line.split('.', 1)[-1].strip() if '.' in line else line.lstrip('- ')
                sources.append(source)
        
        return sources
    
    except Exception as e:
        return [f"Error getting sources: {str(e)}"]

def _verify_against_sources(question: str, answer: str, sources: List[str]) -> Dict[str, Any]:
    """
    Verify the answer against the provided sources and assess hallucination risk.
    """
    
    verification_prompt = """You are a fact-checking expert. Your task is to assess whether an answer is likely to be a hallucination based on the question, answer, and sources provided.

Consider these factors:
1. Source quality and specificity
2. Consistency between answer and expected sources
3. Whether the sources are verifiable and real
4. Whether the answer contains specific claims that can be fact-checked

Examples of hallucination indicators:
- Vague or generic sources ("various studies", "experts say")
- Sources that don't exist or are made up
- Answers about impossible or fictional scenarios presented as fact
- Contradictory information within the answer
- Claims that cannot be verified through the listed sources

Examples of reliable indicators:
- Specific, named sources (patents, official documents, institutions)
- Consistent information across multiple source types
- Answers that acknowledge uncertainty when appropriate
- Sources that are known to be authoritative and verifiable

Assessment format:
HALLUCINATION_RISK: [HIGH/MEDIUM/LOW]
CONFIDENCE: [0.0-1.0]
REASONING: [Detailed explanation of assessment]

Now assess:"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": verification_prompt},
                {"role": "user", "content": f"Question: {question}\nAnswer: {answer}\nSources: {sources}"}
            ],
            temperature=0.1,
            max_tokens=400
        )
        
        verification_text = response.choices[0].message.content.strip()
        
        # Parse the verification result
        is_hallucination = False
        confidence = 0.5
        reasoning = verification_text
        
        # Extract hallucination risk
        if "HALLUCINATION_RISK: HIGH" in verification_text:
            is_hallucination = True
            confidence = 0.8
        elif "HALLUCINATION_RISK: MEDIUM" in verification_text:
            is_hallucination = True
            confidence = 0.6
        elif "HALLUCINATION_RISK: LOW" in verification_text:
            is_hallucination = False
            confidence = 0.8
        
        # Try to extract confidence score if provided
        if "CONFIDENCE:" in verification_text:
            try:
                confidence_line = [line for line in verification_text.split('\n') if 'CONFIDENCE:' in line][0]
                confidence = float(confidence_line.split(':')[1].strip())
            except:
                pass  # Keep default confidence
        
        # Extract reasoning
        if "REASONING:" in verification_text:
            reasoning_start = verification_text.find("REASONING:")
            reasoning = verification_text[reasoning_start:].replace("REASONING:", "").strip()
        
        return {
            "is_hallucination": is_hallucination,
            "confidence": confidence,
            "reasoning": reasoning
        }
    
    except Exception as e:
        return {
            "is_hallucination": False,
            "confidence": 0.0,
            "reasoning": f"Error in verification: {str(e)}"
        } 