#!/usr/bin/env python3
"""Demo script for Invoice Parser Task 06.

This script demonstrates the invoice parsing functionality with sample invoices.
Run this to see how the parsing works in practice.
"""

import os
import json
from solution import parse_invoice, evaluate_invoice_parsing, llm_as_judge_evaluation

def main():
    print("📄 Invoice Parser Demo")
    print("=" * 50)
    
    # Demo invoices with varying complexity
    demo_invoices = [
        """INVOICE #12345
Date: 2024-01-15
From: TechCorp Solutions
To: Client Company

Item: Software License - 2 units @ $500.00 each
Item: Support Services - 1 unit @ $200.00 each

Total: $1,200.00""",
        
        """ABC Company
Invoice: INV-2024-001
Date: March 15, 2024
123 Main Street

Bill To: XYZ Corp
456 Oak Avenue

Description: Web Development Services
Quantity: 40 hours
Rate: $100/hour
Amount: $4,000.00

Total: $4,000.00""",

        """TechSupport Pro
Invoice: TSP-2024-0123
Date: 2024-02-20

To: StartupCorp

1. Server Setup - 1 x $500.00 = $500.00
2. Domain Registration - 1 x $15.00 = $15.00
3. SSL Certificate - 1 x $89.00 = $89.00

TOTAL: $604.00"""
    ]
    
    for i, invoice_text in enumerate(demo_invoices, 1):
        print(f"\n📋 Invoice {i}:")
        print("-" * 40)
        print(invoice_text)
        print("\n🔍 Parsing Result:")
        
        result = parse_invoice(invoice_text)
        
        print(f"🏢 Vendor: {result['vendor_name']}")
        print(f"🔢 Invoice #: {result['invoice_number']}")
        print(f"📅 Date: {result['date']}")
        print(f"💰 Total: ${result['total_amount']:.2f}")
        print(f"📦 Line Items: {len(result['line_items'])}")
        print(f"👤 Customer: {result['customer_info']}")
        print(f"📊 Confidence: {result['confidence']:.2f}")
        
        if result['line_items']:
            print("📋 Items:")
            for item in result['line_items']:
                print(f"   • {item['description']} - {item['quantity']} x ${item['price']:.2f}")
    
    print("\n" + "=" * 50)
    print("Demo completed! ✅")

def evaluation_demo():
    """Demonstrate comprehensive evaluation capabilities."""
    print("\n🧪 Evaluation Demo")
    print("=" * 50)
    
    # Load test invoices from sample data
    test_invoices = []
    try:
        with open('sample_invoices.jsonl', 'r') as f:
            for line in f:
                test_invoices.append(json.loads(line.strip()))
    except FileNotFoundError:
        # Fallback test invoices
        test_invoices = [
            {
                "invoice_text": "INVOICE #12345\nDate: 2024-01-15\nFrom: TechCorp Solutions\n\nItem: Software License - 2 units @ $500.00 each\nTotal: $1,000.00",
                "expected_vendor_name": "TechCorp Solutions",
                "expected_invoice_number": "12345",
                "expected_date": "2024-01-15",
                "expected_total_amount": 1000.00,
                "expected_line_items": [{"description": "Software License", "quantity": 2, "price": 500.00}]
            },
            {
                "invoice_text": "ABC Company\nInvoice: INV-001\nDate: 2024-02-01\nServices: $500.00\nTotal: $500.00",
                "expected_vendor_name": "ABC Company",
                "expected_invoice_number": "INV-001", 
                "expected_date": "2024-02-01",
                "expected_total_amount": 500.00,
                "expected_line_items": [{"description": "Services", "quantity": 1, "price": 500.00}]
            }
        ]
    
    print(f"📊 Running evaluation on {len(test_invoices)} invoices...")
    
    # Basic field accuracy evaluation
    print("\n1️⃣ Basic Field Accuracy Evaluation")
    print("-" * 30)
    basic_results = evaluate_invoice_parsing(test_invoices)
    print(f"✅ Overall Accuracy: {basic_results['overall_accuracy']:.2%}")
    print(f"🏢 Vendor Name Accuracy: {basic_results['vendor_name_accuracy']:.2%}")
    print(f"🔢 Invoice Number Accuracy: {basic_results['invoice_number_accuracy']:.2%}")
    print(f"📅 Date Accuracy: {basic_results['date_accuracy']:.2%}")
    print(f"💰 Total Amount Accuracy: {basic_results['total_amount_accuracy']:.2%}")
    print(f"📦 Line Items Accuracy: {basic_results['line_items_accuracy']:.2%}")
    
    # LLM-as-Judge comprehensive evaluation
    print("\n2️⃣ LLM-as-Judge Comprehensive Evaluation")
    print("-" * 30)
    print("🤖 Running comprehensive analysis...")
    
    llm_results = llm_as_judge_evaluation(test_invoices)
    
    print(f"\n🏆 Performance Level: {llm_results['performance_level']}")
    print(f"🎯 Average Field Accuracy: {llm_results['avg_field_accuracy']:.2%}")
    print(f"📊 Average Scores (0-10 scale):")
    print(f"   • Extraction Accuracy: {llm_results['avg_extraction_accuracy']:.1f}")
    print(f"   • Data Completeness: {llm_results['avg_data_completeness']:.1f}")
    print(f"   • Format Consistency: {llm_results['avg_format_consistency']:.1f}")
    print(f"   • Process Methodology: {llm_results['avg_process_methodology']:.1f}")
    print(f"   • Error Handling: {llm_results['avg_error_handling']:.1f}")
    print(f"   • Overall Assessment: {llm_results['avg_overall_assessment']:.1f}")
    
    print("\n💡 Evaluation Insights:")
    if llm_results['avg_overall_assessment'] >= 8.0:
        print("   🌟 Excellent performance! The parser demonstrates superior extraction capabilities.")
    elif llm_results['avg_overall_assessment'] >= 6.5:
        print("   👍 Good performance with room for fine-tuning few-shot examples.")
    elif llm_results['avg_overall_assessment'] >= 5.0:
        print("   ⚠️  Adequate performance but consider improving structured output handling.")
    else:
        print("   🔧 Needs improvement in methodology and prompt engineering.")

if __name__ == "__main__":
    # Check for required API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Please set your OpenAI API key and try again.")
        exit(1)
    
    # Run main demo
    main()
    
    # Run evaluation demo
    evaluation_demo() 