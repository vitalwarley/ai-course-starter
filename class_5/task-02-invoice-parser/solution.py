"""Starter stub for Task 06 – Invoice Parser.

Complete `parse_invoice` so that it parses unstructured invoice text into 
structured JSON format using prompt engineering techniques.

This task demonstrates:
- Few-shot prompting with invoice parsing examples
- Structured output generation with JSON schema
- Constrained generation techniques
- Error handling and robustness

Example:
    >>> result = parse_invoice("INVOICE #12345\\nDate: 2024-01-15\\nFrom: TechCorp...")
    >>> result['vendor_name']
    'TechCorp'
    >>> result['total_amount']
    1200.00
"""

from typing import Dict, List, Any, Union
import os
import json
import re
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def parse_invoice(invoice_text: str) -> Dict[str, Any]:
    """
    Parse unstructured invoice text into structured JSON format.
    
    This function should:
    1. Use few-shot prompting to guide the parsing process
    2. Extract key fields: vendor_name, invoice_number, date, total_amount, line_items
    3. Ensure structured JSON output with proper data types
    4. Provide confidence scoring for reliability assessment
    
    Args:
        invoice_text (str): The raw invoice text to parse
        
    Returns:
        Dict[str, Any]: A structured dictionary containing:
            - "vendor_name" (str): Name of the vendor/company
            - "invoice_number" (str): Invoice number or ID
            - "date" (str): Invoice date (YYYY-MM-DD format)
            - "total_amount" (float): Total amount due
            - "line_items" (list): List of items with description, quantity, price
            - "customer_info" (str): Customer/client information
            - "confidence" (float): Confidence score (0.0 to 1.0)
    """
    
    # Clean and preprocess the invoice text
    cleaned_text = _preprocess_invoice_text(invoice_text)
    
    # Use few-shot prompting to parse the invoice
    parsed_result = _parse_with_few_shot(cleaned_text)
    
    # Validate and clean the parsed result
    validated_result = _validate_and_clean_result(parsed_result)
    
    # Calculate confidence score
    confidence = _calculate_confidence(cleaned_text, validated_result)
    validated_result["confidence"] = confidence
    
    return validated_result

def _preprocess_invoice_text(text: str) -> str:
    """
    Clean and normalize invoice text for better parsing.
    """
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Normalize line breaks
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    # Clean up currency symbols and formatting
    text = re.sub(r'[$£€¥]', '$', text)
    
    return text.strip()

def _parse_with_few_shot(invoice_text: str) -> Dict[str, Any]:
    """
    Use few-shot prompting to parse the invoice text.
    """
    
    # Few-shot prompt with examples
    system_prompt = """You are an expert invoice parser. Parse the given invoice text into structured JSON format.

IMPORTANT: Always return valid JSON only, no additional text or explanation.

Examples:

Input: "INVOICE #INV-2024-001
Date: March 15, 2024
ABC Company
123 Main Street

Bill To: XYZ Corp
456 Oak Avenue

Description: Web Development Services
Quantity: 40 hours
Rate: $100/hour
Amount: $4,000.00

Total: $4,000.00"

Output: {
  "vendor_name": "ABC Company",
  "invoice_number": "INV-2024-001",
  "date": "2024-03-15",
  "total_amount": 4000.00,
  "line_items": [
    {
      "description": "Web Development Services",
      "quantity": 40,
      "price": 100.00
    }
  ],
  "customer_info": "XYZ Corp"
}

Input: "TechSupport Pro
Invoice: TSP-2024-0123
Date: 2024-02-20

To: StartupCorp

1. Server Setup - 1 x $500.00 = $500.00
2. Domain Registration - 1 x $15.00 = $15.00
3. SSL Certificate - 1 x $89.00 = $89.00

TOTAL: $604.00"

Output: {
  "vendor_name": "TechSupport Pro",
  "invoice_number": "TSP-2024-0123",
  "date": "2024-02-20",
  "total_amount": 604.00,
  "line_items": [
    {
      "description": "Server Setup",
      "quantity": 1,
      "price": 500.00
    },
    {
      "description": "Domain Registration",
      "quantity": 1,
      "price": 15.00
    },
    {
      "description": "SSL Certificate",
      "quantity": 1,
      "price": 89.00
    }
  ],
  "customer_info": "StartupCorp"
}

Input: "INVOICE #12345
Date: 2024-01-15
From: TechCorp Solutions
To: Client Company

Item: Software License - 2 units @ $500.00 each
Item: Support Services - 1 unit @ $200.00 each

Total: $1,200.00"

Output: {
  "vendor_name": "TechCorp Solutions",
  "invoice_number": "12345",
  "date": "2024-01-15",
  "total_amount": 1200.00,
  "line_items": [
    {
      "description": "Software License",
      "quantity": 2,
      "price": 500.00
    },
    {
      "description": "Support Services",
      "quantity": 1,
      "price": 200.00
    }
  ],
  "customer_info": "Client Company"
}

Now parse the following invoice. Return only valid JSON:"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": invoice_text}
            ],
            temperature=0.1,
            max_tokens=800
        )
        
        response_text = response.choices[0].message.content.strip()
        
        # Try to parse the JSON response
        try:
            parsed_result = json.loads(response_text)
            return parsed_result
        except json.JSONDecodeError:
            # If JSON parsing fails, try to extract JSON from the response
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            else:
                return _create_default_result()
    
    except Exception as e:
        return _create_default_result()

def _validate_and_clean_result(result: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate and clean the parsed result to ensure proper format.
    """
    
    # Default structure
    validated = {
        "vendor_name": "",
        "invoice_number": "",
        "date": "",
        "total_amount": 0.0,
        "line_items": [],
        "customer_info": ""
    }
    
    # Validate and clean each field
    if "vendor_name" in result and result["vendor_name"]:
        validated["vendor_name"] = str(result["vendor_name"]).strip()
    
    if "invoice_number" in result and result["invoice_number"]:
        validated["invoice_number"] = str(result["invoice_number"]).strip()
    
    if "date" in result and result["date"]:
        validated["date"] = _normalize_date(str(result["date"]))
    
    if "total_amount" in result:
        validated["total_amount"] = _extract_amount(result["total_amount"])
    
    if "line_items" in result and isinstance(result["line_items"], list):
        validated["line_items"] = _validate_line_items(result["line_items"])
    
    if "customer_info" in result and result["customer_info"]:
        validated["customer_info"] = str(result["customer_info"]).strip()
    
    return validated

def _normalize_date(date_str: str) -> str:
    """
    Normalize date string to YYYY-MM-DD format.
    """
    # Remove common date separators and try to parse
    date_patterns = [
        r'(\d{4})-(\d{1,2})-(\d{1,2})',  # YYYY-MM-DD
        r'(\d{1,2})/(\d{1,2})/(\d{4})',  # MM/DD/YYYY
        r'(\d{1,2})-(\d{1,2})-(\d{4})',  # MM-DD-YYYY
        r'(\d{4})/(\d{1,2})/(\d{1,2})',  # YYYY/MM/DD
    ]
    
    for pattern in date_patterns:
        match = re.search(pattern, date_str)
        if match:
            groups = match.groups()
            if len(groups) == 3:
                if len(groups[0]) == 4:  # YYYY-MM-DD or YYYY/MM/DD
                    year, month, day = groups
                else:  # MM/DD/YYYY or MM-DD-YYYY
                    month, day, year = groups
                
                # Ensure proper formatting
                try:
                    month = int(month)
                    day = int(day)
                    year = int(year)
                    
                    if 1 <= month <= 12 and 1 <= day <= 31:
                        return f"{year:04d}-{month:02d}-{day:02d}"
                except ValueError:
                    pass
    
    return date_str

def _extract_amount(amount_input: Union[str, float, int]) -> float:
    """
    Extract and clean monetary amount.
    """
    if isinstance(amount_input, (int, float)):
        return float(amount_input)
    
    if isinstance(amount_input, str):
        # Remove currency symbols and commas
        amount_str = re.sub(r'[$£€¥,]', '', amount_input)
        
        # Extract numeric value
        amount_match = re.search(r'(\d+\.?\d*)', amount_str)
        if amount_match:
            try:
                return float(amount_match.group(1))
            except ValueError:
                pass
    
    return 0.0

def _validate_line_items(line_items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Validate and clean line items.
    """
    validated_items = []
    
    for item in line_items:
        if isinstance(item, dict):
            validated_item = {
                "description": "",
                "quantity": 1,
                "price": 0.0
            }
            
            if "description" in item and item["description"]:
                validated_item["description"] = str(item["description"]).strip()
            
            if "quantity" in item:
                try:
                    validated_item["quantity"] = int(item["quantity"])
                except (ValueError, TypeError):
                    validated_item["quantity"] = 1
            
            if "price" in item:
                validated_item["price"] = _extract_amount(item["price"])
            
            validated_items.append(validated_item)
    
    return validated_items

def _calculate_confidence(text: str, result: Dict[str, Any]) -> float:
    """
    Calculate confidence score based on extracted data quality.
    """
    confidence = 0.0
    
    # Check if key fields are present
    if result["vendor_name"]:
        confidence += 0.25
    
    if result["invoice_number"]:
        confidence += 0.2
    
    if result["date"]:
        confidence += 0.15
    
    if result["total_amount"] > 0:
        confidence += 0.25
    
    if result["line_items"]:
        confidence += 0.15
    
    # Bonus for completeness
    if all([result["vendor_name"], result["invoice_number"], result["date"], 
            result["total_amount"] > 0, result["line_items"]]):
        confidence = min(confidence + 0.1, 1.0)
    
    return round(confidence, 2)

def _create_default_result() -> Dict[str, Any]:
    """
    Create a default result structure when parsing fails.
    """
    return {
        "vendor_name": "",
        "invoice_number": "",
        "date": "",
        "total_amount": 0.0,
        "line_items": [],
        "customer_info": ""
    }

# Additional helper functions for testing and evaluation



def llm_as_judge_evaluation(test_invoices: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Comprehensive LLM-as-Judge evaluation assessing both output and process quality.
    
    This function evaluates:
    1. Output accuracy and completeness
    2. Process methodology (Few-shot prompting, structured output)
    3. Data extraction quality and format consistency
    4. Overall system effectiveness
    
    Args:
        test_invoices: List of dicts with 'invoice_text' and expected field values
        
    Returns:
        Dict with comprehensive evaluation metrics
    """
    
    evaluation_results = []
    
    for test_case in test_invoices:
        invoice_text = test_case['invoice_text']
        
        # Get the full parsing result
        result = parse_invoice(invoice_text)
        
        # Evaluate this specific case with LLM-as-Judge
        case_evaluation = _evaluate_single_invoice_with_llm(
            invoice_text, result, test_case
        )
        
        evaluation_results.append(case_evaluation)
    
    # Aggregate results
    return _aggregate_llm_judge_results(evaluation_results)

def _evaluate_single_invoice_with_llm(invoice_text: str, result: Dict[str, Any], test_case: Dict[str, Any]) -> Dict[str, Any]:
    """
    Use LLM-as-Judge to evaluate a single invoice parsing case comprehensively.
    """
    
    judge_prompt = """You are an expert AI evaluator assessing an invoice parsing system.

Evaluate the following test case across these dimensions:

1. **EXTRACTION ACCURACY** (0-10): How accurately were the key fields extracted?
2. **DATA COMPLETENESS** (0-10): How complete is the extracted information?
3. **FORMAT CONSISTENCY** (0-10): How well-structured and consistent is the JSON output?
4. **PROCESS METHODOLOGY** (0-10): How effective was the few-shot prompting approach?
5. **ERROR HANDLING** (0-10): How well does the system handle edge cases and errors?

For each dimension, provide:
- Score (0-10)
- Brief justification (1-2 sentences)

Also provide an OVERALL ASSESSMENT (0-10) with reasoning.

Expected format:
EXTRACTION_ACCURACY: [score] - [justification]
DATA_COMPLETENESS: [score] - [justification]
FORMAT_CONSISTENCY: [score] - [justification]
PROCESS_METHODOLOGY: [score] - [justification]
ERROR_HANDLING: [score] - [justification]
OVERALL_ASSESSMENT: [score] - [justification]

Test Case:
Original Invoice Text: {invoice_text}
System Result: {result}
Expected Values: {expected}"""

    # Extract expected values from test case
    expected_values = {}
    for key, value in test_case.items():
        if key.startswith('expected_'):
            field_name = key.replace('expected_', '')
            expected_values[field_name] = value

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": judge_prompt.format(
                    invoice_text=invoice_text[:500] + "..." if len(invoice_text) > 500 else invoice_text,
                    result=result,
                    expected=expected_values
                )}
            ],
            temperature=0.1,
            max_tokens=800
        )
        
        evaluation_text = response.choices[0].message.content.strip()
        
        # Parse the evaluation scores
        scores = {}
        dimensions = [
            "EXTRACTION_ACCURACY", "DATA_COMPLETENESS", "FORMAT_CONSISTENCY", 
            "PROCESS_METHODOLOGY", "ERROR_HANDLING", "OVERALL_ASSESSMENT"
        ]
        
        for dimension in dimensions:
            try:
                if dimension in evaluation_text:
                    line = [l for l in evaluation_text.split('\n') if dimension in l][0]
                    score_match = re.search(r'(\d+(?:\.\d+)?)', line.split('-')[0])
                    if score_match:
                        scores[dimension.lower()] = float(score_match.group(1))
                    else:
                        scores[dimension.lower()] = 5.0  # Default middle score
                else:
                    scores[dimension.lower()] = 5.0
            except:
                scores[dimension.lower()] = 5.0
        
        # Calculate field accuracy
        field_accuracy = _calculate_field_accuracy(result, expected_values)
        
        return {
            "invoice_text": invoice_text[:100] + "..." if len(invoice_text) > 100 else invoice_text,
            "field_accuracy": field_accuracy,
            "llm_scores": scores,
            "evaluation_text": evaluation_text,
            "system_result": result,
            "expected_values": expected_values
        }
        
    except Exception as e:
        # Fallback evaluation
        field_accuracy = _calculate_field_accuracy(result, expected_values)
        
        return {
            "invoice_text": invoice_text[:100] + "..." if len(invoice_text) > 100 else invoice_text,
            "field_accuracy": field_accuracy,
            "llm_scores": {dim.lower(): 5.0 for dim in [
                "EXTRACTION_ACCURACY", "DATA_COMPLETENESS", "FORMAT_CONSISTENCY", 
                "PROCESS_METHODOLOGY", "ERROR_HANDLING", "OVERALL_ASSESSMENT"
            ]},
            "evaluation_text": f"Error in LLM evaluation: {str(e)}",
            "system_result": result,
            "expected_values": expected_values
        }

def _calculate_field_accuracy(result: Dict[str, Any], expected_values: Dict[str, Any]) -> float:
    """
    Calculate field-level accuracy between result and expected values.
    """
    if not expected_values:
        return 0.0
    
    correct_fields = 0
    total_fields = 0
    
    for field, expected in expected_values.items():
        if field in result:
            total_fields += 1
            actual = result[field]
            
            if field == "total_amount":
                # Allow small floating point differences
                if abs(float(actual) - float(expected)) < 0.01:
                    correct_fields += 1
            elif field == "line_items":
                # Check if line items count matches
                if len(actual) == len(expected):
                    correct_fields += 1
            else:
                # String comparison (case insensitive)
                if str(actual).lower() == str(expected).lower():
                    correct_fields += 1
    
    return correct_fields / total_fields if total_fields > 0 else 0.0

def _aggregate_llm_judge_results(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Aggregate LLM-as-Judge evaluation results into summary metrics.
    """
    if not results:
        return {}
    
    # Calculate averages for each dimension
    dimensions = ["extraction_accuracy", "data_completeness", "format_consistency", 
                 "process_methodology", "error_handling", "overall_assessment"]
    
    aggregated = {
        "total_cases": len(results),
        "avg_field_accuracy": sum(r["field_accuracy"] for r in results) / len(results),
    }
    
    # Average LLM scores
    for dim in dimensions:
        scores = [r["llm_scores"].get(dim, 5.0) for r in results]
        aggregated[f"avg_{dim}"] = sum(scores) / len(scores) if scores else 5.0
    
    # Performance categorization
    overall_avg = aggregated["avg_overall_assessment"]
    if overall_avg >= 8.0:
        performance_level = "Excellent"
    elif overall_avg >= 6.5:
        performance_level = "Good"
    elif overall_avg >= 5.0:
        performance_level = "Adequate"
    else:
        performance_level = "Needs Improvement"
    
    aggregated["performance_level"] = performance_level
    
    # Detailed results for inspection
    aggregated["detailed_results"] = results
    
    return aggregated 