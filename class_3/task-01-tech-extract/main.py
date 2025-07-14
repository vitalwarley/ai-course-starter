#!/usr/bin/env python3
"""
Main demonstration script for Task 01 - Technology Extraction from Job Postings
"""

from solution import extract_tech

def main():
    """Demonstrate the extract_tech function with sample inputs."""
    
    # Sample job postings for testing
    sample_texts = [
        "We are looking for a Python developer with experience in Django and PostgreSQL.",
        "Frontend engineer skilled in React, TypeScript, and GraphQL; familiarity with AWS is a plus.",
        "Seeking data scientist proficient in PyTorch, TensorFlow, and cloud platforms like GCP.",
        "Backend role: Python/Django with PostgreSQL and Redis for caching.",
        "We need a React & TypeScript engineer familiar with AWS and Docker.",
    ]
    
    print("=== Technology Extraction Demo ===\n")
    
    for i, text in enumerate(sample_texts, 1):
        print(f"Sample {i}:")
        print(f"Text: {text}")
        
        try:
            technologies = extract_tech(text)
            if technologies:
                print(f"Extracted technologies: {', '.join(sorted(technologies))}")
            else:
                print("No technologies found")
        except NotImplementedError:
            print("Function not implemented yet")
        except Exception as e:
            print(f"Error: {e}")
        
        print("-" * 50)

if __name__ == "__main__":
    main() 