import os


def convert_mp4_to_wav() -> None:
    pass


def main() -> None:
    # mp4 -> wav
    os.system(
        "ffmpeg -i input_video.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 output_audio.wav"
    )


if __name__ == "main":
    main()
