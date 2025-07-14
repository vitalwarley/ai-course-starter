# Voice-to-Text Transcriber

An intelligent audio transcription tool that converts speech to text using OpenAI's advanced GPT-4 transcription model. Features a user-friendly web interface built with Gradio and includes utilities for downloading audio content from YouTube.

## Features

- **OpenAI GPT-4 Transcription**: Uses OpenAI's latest high-accuracy speech model (gpt-4o-transcribe)
- **Multi-format Support**: Handles various audio formats including WAV, MP3, FLAC, and more
- **Web Interface**: User-friendly Gradio interface with upload and microphone recording options
- **YouTube Integration**: Download and extract audio from YouTube videos automatically
- **High Accuracy**: Leverages state-of-the-art speech recognition technology
- **Real-time Processing**: Fast transcription with minimal latency
- **Multiple Input Sources**: Upload files or record directly through the interface

## Requirements

- Python 3.12 or higher
- OpenAI API key
- UV package manager (will be installed automatically if not present)
- Internet connection for OpenAI API access

## Installation

### Quick Setup

Run the provided setup script to automatically install all dependencies:

```bash
./setup.sh
```

This script will:
1. Install the UV package manager if not already present
2. Create a Python 3.12 virtual environment
3. Install all required dependencies (Gradio, OpenAI)
4. Set up the project for immediate use

### Manual Setup

If you prefer to set up manually:

1. **Install UV package manager**:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Create virtual environment**:
   ```bash
   uv venv --python=python3.12 .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   uv pip install --requirement pyproject.toml
   ```

### Environment Setup

Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Or create a `.env` file in the project directory:
```
OPENAI_API_KEY=your-api-key-here
```

## Usage

### Web Interface

Launch the Gradio web interface for easy transcription:

```bash
source .venv/bin/activate  # If not already activated
python app.py
```

or run directly with uv:

```bash
uv run python app.py
```

This will start a local web server where you can:
- Upload audio files for transcription
- Record audio directly using your microphone
- View transcription results in real-time

### Command Line Usage

You can also use the transcription function directly in your Python code:

```python
from solution import transcribe_audio

# Transcribe an audio file
audio_path = "path/to/your/audio.wav"
transcript = transcribe_audio(audio_path)
print(transcript)
```

### YouTube Audio Download

Use the provided script to download and extract audio from YouTube videos:

```bash
./download_and_extract.sh "https://www.youtube.com/watch?v=183tAr8imcU"
```

This will:
- Download the video from YouTube
- Extract audio in WAV format
- Save to the `./downloads` directory
- Create a log file with download details

Custom output directory:
```bash
./download_and_extract.sh "https://www.youtube.com/watch?v=VIDEO_ID" ./custom_output
```

## API Reference

### `transcribe_audio(path: str) -> str`

Transcribes audio file to text using OpenAI's GPT-4 transcription model.

**Parameters:**
- `path` (str): Path to the audio file to transcribe

**Returns:**
- `str`: Plain text transcript of the audio content

**Supported Formats:**
- WAV
- MP3
- FLAC
- M4A
- OGG
- And other common audio formats

**Example:**
```python
transcript = transcribe_audio("recording.wav")
print(transcript)
# Output: "Hello, this is a test recording for transcription."
```

## Project Structure

```
task-04-voice-transcribe/
├── app.py                    # Gradio web interface
├── solution.py               # Core transcription logic
├── download_and_extract.sh   # YouTube audio download script
├── setup.sh                  # Automated setup script
├── pyproject.toml           # Project configuration
├── downloads/               # Directory for downloaded audio files
│   ├── download_log.txt     # Download log file
│   └── *.wav               # Downloaded audio files
└── README.md               # This file
```

## Development

### Core Technology

The transcription system uses:

1. **OpenAI GPT-4 Transcription**: State-of-the-art speech recognition model
2. **Gradio Interface**: Modern web interface for easy interaction
3. **yt-dlp Integration**: Robust YouTube audio extraction
4. **Multi-format Support**: Handles various audio file types

### Audio Processing Pipeline

1. **Input Handling**: Accepts audio files or direct microphone input
2. **Format Validation**: Ensures audio is in supported format
3. **API Processing**: Sends audio to OpenAI transcription service
4. **Text Output**: Returns clean, formatted transcript

### Sample Usage Examples

```python
# Basic transcription
transcript = transcribe_audio("interview.mp3")

# Batch processing
import os
audio_files = [f for f in os.listdir("./audio") if f.endswith(('.wav', '.mp3'))]
transcripts = [transcribe_audio(f"./audio/{file}") for file in audio_files]

# Web interface integration
def process_recording(audio_file):
    if audio_file is None:
        return "No audio file provided"
    return transcribe_audio(audio_file)
```

## Performance

- **Accuracy**: High accuracy with OpenAI's advanced speech recognition
- **Speed**: Typical transcription completes in seconds
- **Reliability**: Robust error handling and format support
- **Scalability**: Can handle files of various lengths and qualities

## Troubleshooting

### Common Issues

1. **Missing API Key**: Ensure `OPENAI_API_KEY` environment variable is set
2. **Audio Format**: Check that your audio file is in a supported format
3. **Internet Connection**: Transcription requires internet access for OpenAI API
4. **File Size**: Large audio files may take longer to process
5. **Python Version**: Ensure you're using Python 3.12 or higher

### Error Messages

- **"OpenAI API key not found"**: Set the `OPENAI_API_KEY` environment variable
- **"Unsupported audio format"**: Convert your audio to a supported format (WAV, MP3, etc.)
- **"File not found"**: Check that the audio file path is correct
- **"API quota exceeded"**: Check your OpenAI API usage limits

### YouTube Download Issues

- **Invalid URL**: Ensure the YouTube URL is valid and accessible
- **Network Error**: Check your internet connection
- **Missing yt-dlp**: The script will automatically install yt-dlp via uvx

## License

This project is part of the TIC43 AI Course and is intended for educational purposes.

## Support

For issues and questions, please refer to the course materials or contact the course instructor.

## Additional Resources

- [OpenAI Whisper API Documentation](https://platform.openai.com/docs/guides/speech-to-text)
- [Gradio Documentation](https://gradio.app/docs/)
- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp) 