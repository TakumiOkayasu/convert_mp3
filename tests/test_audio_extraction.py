from MovieToSound import extract_mp4_to_wav
from pathlib import Path

import pytest


def test_extract_audio_to_wav():
    input_mp4s = Path.cwd().glob('tests/mp4/*.mp4')  # テスト用のMP4ファイル

    if not input_mp4s:
        pytest.skip("テスト用のMP4ファイルが存在しないため、テストをスキップします")

    for mp4 in input_mp4s:
        result = extract_mp4_to_wav(mp4)

        assert result.is_file(), f"WAVファイルが生成されていません: {result}"

        # テスト終了後に生成されたWAVファイルを削除
        result.unlink(missing_ok=True)
