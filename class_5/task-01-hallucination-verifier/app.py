import gradio as gr
from solution import verify_hallucination

def ui_fn(question):
    """
    UI function for the Gradio interface.
    """
    if not question.strip():
        return "Please enter a question", [], "No verification performed", 0.0, "No question provided"
    
    try:
        result = verify_hallucination(question)
        
        # Format sources as a bulleted list
        sources_formatted = "\n".join([f"• {source}" for source in result['sources']])
        
        # Format hallucination result
        hallucination_status = "🚨 Likely Hallucination" if result['is_hallucination'] else "✅ Likely Accurate"
        
        return (
            result['answer'],
            sources_formatted,
            hallucination_status,
            result['confidence'],
            result['reasoning']
        )
    
    except Exception as e:
        return f"Error: {str(e)}", "", "Error in verification", 0.0, f"An error occurred: {str(e)}"

# Create the Gradio interface
demo = gr.Interface(
    fn=ui_fn,
    inputs=[
        gr.Textbox(
            label="Question to Verify",
            placeholder="Enter a question to check for potential hallucinations...",
            lines=2
        )
    ],
    outputs=[
        gr.Textbox(label="AI Answer", lines=4),
        gr.Textbox(label="Sources", lines=4),
        gr.Textbox(label="Verification Result"),
        gr.Number(label="Confidence Score"),
        gr.Textbox(label="Reasoning", lines=4)
    ],
    title="🔍 Hallucination Verifier",
    description="""
    This tool uses a multi-step verification process to detect potential hallucinations in AI responses.
    
    **How it works:**
    1. Gets an initial answer using Chain of Thought reasoning
    2. Requests sources for the answer
    3. Verifies the answer against the provided sources
    4. Provides a confidence score and detailed reasoning
    
    **Try these examples:**
    - "What is the capital of France?" (should be accurate)
    - "Who was the first person to walk on Mars?" (should be detected as hallucination)
    - "What is the largest planet in our solar system?" (should be accurate)
    """,
    examples=[
        ["What is the capital of France?"],
        ["Who was the first person to walk on Mars?"],
        ["What is the largest planet in our solar system?"],
        ["Who invented the computer mouse?"],
        ["What is the capital of the fictional country Wakanda?"]
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