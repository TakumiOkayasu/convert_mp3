
from pathlib import Path
from MovieToSound import extract_mp4_to_wav


def main() -> None:
    extract_mp4_to_wav(Path.cwd() / Path("tests/mp4/AKE100720.mp4"))


if __name__ == "main":
    main()
