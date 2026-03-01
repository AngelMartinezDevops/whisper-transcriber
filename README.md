# Whisper Transcriber

Transcribe video and audio files using [OpenAI Whisper](https://github.com/openai/whisper).

## Requirements

- Python 3.10+
- [FFmpeg](https://ffmpeg.org/) (must be in PATH)
- ~2GB RAM for base model, more for larger models

---

## Installation on Windows 11

### 1. Install Python 3.12 (winget)

```powershell
winget install Python.Python.3.12 --accept-package-agreements --accept-source-agreements
```

### 2. Install FFmpeg (winget)

```powershell
winget install Gyan.FFmpeg --accept-package-agreements --accept-source-agreements
```

### 3. Refresh PATH (or open a new terminal)

After installing Python and FFmpeg, you may need to refresh the environment variables:

```powershell
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
```

Or simply **close and reopen PowerShell/CMD** — that's usually enough.

### 4. Verify Python and FFmpeg

```powershell
python --version
ffmpeg -version
```

### 5. Install Whisper

```powershell
pip install -r requirements.txt
```

Or directly:

```powershell
pip install openai-whisper
```

---

## Installation (Linux / macOS)

```bash
# Install FFmpeg (Ubuntu/Debian)
sudo apt install ffmpeg

# Install via pip
pip install -r requirements.txt
```

## Usage

```bash
python transcribe.py path/to/your/video.mp4
```

### Model size

By default uses `small` model (good balance between speed and accuracy). You can specify:

```bash
python transcribe.py interview.mp4 base   # faster, less accurate
python transcribe.py interview.mp4 medium # slower, more accurate
```

Available models: `tiny` | `base` | `small` | `medium` | `large`

### Output

Creates a `*_transcript.txt` file in the same directory as the input file.

## Supported formats

MP4, MP3, WAV, WebM, MKV, and most common audio/video formats (via FFmpeg).
