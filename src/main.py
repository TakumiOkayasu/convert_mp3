
from pathlib import Path
from SoundToText import mp4_to_text


def main() -> None:
    mp4_to_text(Path.cwd() / Path("tests/mp4/動画視聴本講義-01.mp4"))


if __name__ == "main":
    main()
