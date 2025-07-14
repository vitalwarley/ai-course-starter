#!/bin/bash
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if URL is provided
if [ $# -eq 0 ]; then
    print_error "Usage: $0 <youtube_url> [output_directory]"
    print_info "Example: $0 https://www.youtube.com/watch?v=dQw4w9WgXcQ ./downloads"
    exit 1
fi

YOUTUBE_URL="$1"
OUTPUT_DIR="${2:-./downloads}"

# Validate YouTube URL
if [[ ! "$YOUTUBE_URL" =~ ^https?://(www\.)?(youtube\.com|youtu\.be) ]]; then
    print_error "Invalid YouTube URL. Please provide a valid YouTube URL."
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

print_info "Starting YouTube video download and audio extraction..."
print_info "URL: $YOUTUBE_URL"
print_info "Output directory: $OUTPUT_DIR"

# Install uv if not already installed
if ! command -v uv &> /dev/null; then
    print_info "Installing uv package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    
    # Check if .local/bin is in PATH and add it if not
    if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
        print_warning "Adding ~/.local/bin to PATH for current session..."
        export PATH="$HOME/.local/bin:$PATH"
    fi
fi

# Check if uvx is available
if ! command -v uvx &> /dev/null; then
    print_error "uvx command not found. Please make sure uv is properly installed."
    exit 1
fi

print_info "Downloading video and extracting audio to WAV format..."

# Use yt-dlp via uvx to download and extract audio
# Options explanation:
# --extract-audio: Extract audio from video
# --audio-format wav: Convert audio to WAV format
# --audio-quality 0: Best audio quality
# --output: Output filename template
# --no-playlist: Don't download playlist, just the single video
# --restrict-filenames: Restrict filenames to ASCII characters
uvx yt-dlp \
    --extract-audio \
    --audio-format wav \
    --audio-quality 0 \
    --output "$OUTPUT_DIR/%(title)s.%(ext)s" \
    --no-playlist \
    --restrict-filenames \
    --print-to-file "Downloaded: %(title)s" "$OUTPUT_DIR/download_log.txt" \
    "$YOUTUBE_URL"

print_info "Download and extraction completed!"
print_info "Files saved to: $OUTPUT_DIR"
print_info "Check $OUTPUT_DIR/download_log.txt for details."

# List the downloaded files
print_info "Downloaded files:"
find "$OUTPUT_DIR" -name "*.wav" -type f -exec basename {} \; | head -10 