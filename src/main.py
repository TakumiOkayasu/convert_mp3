from pathlib import Path

from MovieToSound import extract_mp4_to_wav, is_mp4


def main() -> None:
    mp4Path = Path("test.mp4")

    if not is_mp4(mp4Path):
        print(f"{mp4Path} is NOT mp4 file.")
        return

    extract_mp4_to_wav(mp4FullPath=mp4Path)


if __name__ == "main":
    main()
