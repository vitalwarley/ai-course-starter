import gradio as gr
from solution import refactor_code   # local import

def ui_fn(code):
    result = refactor_code(code)
    return result["refactored"], result["explanation"]

demo = gr.Interface(
    fn=ui_fn,
    inputs=gr.Code(language="python", label="Input code"),
    outputs=[
        gr.Code(language="python", label="Refactored code"),
        gr.Markdown(label="Explanation"),
    ],
    title="AI Code Refactorer",
    theme="soft",
)

if __name__ == "__main__":
    demo.launch()
