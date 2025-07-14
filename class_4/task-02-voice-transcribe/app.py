import gradio as gr
from solution import transcribe_audio

def ui_fn(audio_file):
    return transcribe_audio(audio_file)

demo = gr.Interface(
    fn=ui_fn,
    inputs=gr.Audio(
        sources=["upload", "microphone"],
        type="filepath",
        label="Upload or record audio",
    ),
    outputs="text",
    title="Voice-to-Text Transcriber",
    theme="soft",
)

if __name__ == "__main__":
    demo.launch()
