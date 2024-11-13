
from pathlib import Path

from SoundToText import mp4_to_text


def main() -> None:
    print("処理開始")
    mp4_to_text(Path.cwd() / Path("tests/mp4/AKE100720.mp4"))


if __name__ == "main":
    main()
