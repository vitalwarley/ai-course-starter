import gradio as gr
from solution import parse_invoice
import json

def ui_fn(invoice_text):
    """
    UI function for the Gradio interface.
    """
    if not invoice_text.strip():
        return "{}", "Please enter invoice text", 0.0
    
    try:
        result = parse_invoice(invoice_text)
        
        # Format result as pretty JSON
        formatted_result = json.dumps(result, indent=2)
        
        # Create summary
        summary = f"""
**Vendor:** {result['vendor_name']}
**Invoice #:** {result['invoice_number']}
**Date:** {result['date']}
**Total:** ${result['total_amount']:.2f}
**Line Items:** {len(result['line_items'])}
**Customer:** {result['customer_info']}
**Confidence:** {result['confidence']:.2f}
        """
        
        return formatted_result, summary, result['confidence']
    
    except Exception as e:
        return f'{{"error": "{str(e)}"}}', f"Error: {str(e)}", 0.0

# Create the Gradio interface
demo = gr.Interface(
    fn=ui_fn,
    inputs=[
        gr.Textbox(
            label="Invoice Text",
            placeholder="""Paste your invoice text here...

Example:
INVOICE #12345
Date: 2024-01-15
From: TechCorp Solutions
To: Client Company

Item: Software License - 2 units @ $500.00 each
Item: Support Services - 1 unit @ $200.00 each

Total: $1,200.00""",
            lines=10
        )
    ],
    outputs=[
        gr.Code(label="Parsed JSON", language="json"),
        gr.Markdown(label="Summary"),
        gr.Number(label="Confidence Score")
    ],
    title="📄 Invoice Parser",
    description="""
    This tool uses advanced prompt engineering techniques to parse unstructured invoice text into structured JSON format.
    
    **Features:**
    - Few-shot prompting for consistent parsing
    - Structured JSON output with key fields
    - Confidence scoring for reliability assessment
    - Handles various invoice formats
    
    **Extracted Fields:**
    - Vendor name
    - Invoice number
    - Date (normalized to YYYY-MM-DD)
    - Total amount
    - Line items (description, quantity, price)
    - Customer information
    """,
    examples=[
        ["""INVOICE #INV-2024-001
Date: March 15, 2024
ABC Company
123 Main Street

Bill To: XYZ Corp
456 Oak Avenue

Description: Web Development Services
Quantity: 40 hours
Rate: $100/hour
Amount: $4,000.00

Total: $4,000.00"""],
        ["""TechSupport Pro
Invoice: TSP-2024-0123
Date: 2024-02-20

To: StartupCorp

1. Server Setup - 1 x $500.00 = $500.00
2. Domain Registration - 1 x $15.00 = $15.00
3. SSL Certificate - 1 x $89.00 = $89.00

TOTAL: $604.00"""],
        ["""Design Studio Inc.
Invoice Number: DS-2024-0045
Date: 01/20/2024

Client: Marketing Agency Ltd.

Logo Design: $800.00
Business Cards: $150.00
Website Mockup: $1,200.00

Subtotal: $2,150.00
Tax (8%): $172.00
TOTAL: $2,322.00"""]
    ],
    theme="soft",
    css="""
    .gradio-container {
        max-width: 1200px;
        margin: 0 auto;
    }
    """
)

if __name__ == "__main__":
    demo.launch() 