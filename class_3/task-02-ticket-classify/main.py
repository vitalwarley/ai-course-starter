#!/usr/bin/env python3
"""
Main demonstration script for Task 02 - Support Ticket Entity Extraction & Classification
"""

from solution import extract_entities, classify

def main():
    """Demonstrate the extract_entities and classify functions with sample inputs."""
    
    # Sample support tickets for testing
    sample_tickets = [
        "The application crashes when I click Export. This is blocking my work! - User: bob, OS: Ubuntu 22.04, Version: v2.0.0",
        "Is there a way to change the theme? - User: alice, OS: Windows 11, Version: v2.0.1",
        "I'm getting a 404 error when trying to access the dashboard. Need urgent help! - User: charlie, OS: macOS 13.2, Version: v1.9.5",
        "Could you add support for dark mode? That would be great! - User: diana, OS: Windows 10, Version: v2.1.0",
        "Server is down and users cannot login. Critical issue! - User: eve, OS: Linux, Version: v2.0.0",
    ]
    
    print("=== Support Ticket Entity Extraction & Classification Demo ===\n")
    
    for i, ticket in enumerate(sample_tickets, 1):
        print(f"Ticket {i}:")
        print(f"Text: {ticket}")
        
        try:
            # Extract entities
            entities = extract_entities(ticket)
            print(f"Extracted entities:")
            print(f"  User: {entities['user']}")
            print(f"  OS: {entities['os']}")
            print(f"  Version: {entities['version']}")
            
            # Classify ticket
            priority, category = classify(ticket)
            print(f"Classification:")
            print(f"  Priority: {priority}")
            print(f"  Category: {category}")
            
        except NotImplementedError:
            print("Functions not implemented yet")
        except Exception as e:
            print(f"Error: {e}")
        
        print("-" * 60)

if __name__ == "__main__":
    main() 