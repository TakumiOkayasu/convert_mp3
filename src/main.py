import os
from pathlib import Path

import ffmpeg


def is_mp4(fullPath: Path) -> bool:
    try:
        probe = ffmpeg.probe(fullPath)
        return probe['format']['format_name'] == 'mov,mp4,m4a,3gp,3g2,mj2'
    except ffmpeg.Error:
        return False


def extract_mp4_to_wav(mp4FullPath: Path) -> None:
    try:
        (
            ffmpeg
            .input(mp4FullPath)
            .output(mp4FullPath.stem + ".wav", format='wav', acodec='pcm_s16le', ar='44100', ac=2)
            .run()
        )

    except ffmpeg.Error as e:
        print(f'Error extracting audio: {e}')
    os.system(
        f"ffmpeg -i {mp4FullPath} -vn -acodec pcm_s16le -ar 44100 -ac 2 wav/{mp4FullPath.stem}.wav"
    )


def main() -> None:
    mp4Path = Path("test.mp4")

    if not is_mp4(mp4Path):
        print(f"{mp4Path} is NOT mp4 file.")
        return

    extract_mp4_to_wav(mp4FullPath=mp4Path)


if __name__ == "main":
    main()
