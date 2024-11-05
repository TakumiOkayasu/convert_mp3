from MovieToSound import extract_mp4_to_wav
from pathlib import Path

import pytest


def test_extract_audio_to_wav():
    input_mp4 = Path.cwd() / Path('tests/mp4/動画視聴本講義-01.mp4')  # テスト用のMP4ファイル

    # テスト用MP4ファイルが存在するかをチェック（存在しなければスキップ）
    if not input_mp4.exists():
        pytest.skip(f"{input_mp4} が存在しないため、テストをスキップします")

    result = extract_mp4_to_wav(input_mp4)

    assert not result.exists(), "WAVファイルが生成されていません"

    # テスト終了後に出力ファイルを削除
    result.rmdir()
