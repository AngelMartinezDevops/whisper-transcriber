#!/usr/bin/env python3
"""
Transcribe video/audio using OpenAI Whisper.
Usage: python transcribe.py <path_to_video_or_audio>
"""
import sys
import whisper


def main():
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <path_to_video_or_audio>")
        print("\nExample: python transcribe.py interview.mp4")
        print("\nModels: tiny, base, small, medium, large (default: small)")
        sys.exit(1)

    file_path = sys.argv[1]
    model_name = sys.argv[2] if len(sys.argv) > 2 else "small"

    print(f"Loading Whisper ({model_name} model)...")
    model = whisper.load_model(model_name)
    print(f"Transcribing: {file_path}")
    result = model.transcribe(file_path, language=None, task="transcribe")

    print("\n" + "=" * 60 + "\nTRANSCRIPT\n" + "=" * 60)
    print(result["text"])

    output_path = file_path.rsplit(".", 1)[0] + "_transcript.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    print(f"\n\nSaved to: {output_path}")


if __name__ == "__main__":
    main()
