"""
Stub signature required by the hidden tests:
    def transcribe_audio(path: str) -> str
Environment:
    • Set OPENAI_API_KEY
    • pip install -r requirements.txt
"""
import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]
client = openai.OpenAI()

def transcribe_audio(path: str) -> str:
    """Return the plain-text transcript of <path> (wav/mp3/flac…)."""
    with open(path, "rb") as f:
        resp = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",   # new high-accuracy speech model
            file=f,
            response_format="text",
        )
    return resp
