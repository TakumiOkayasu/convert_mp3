# テストケース
import os
from pathlib import Path

import pytest

from MovieToSound import extract_mp4_to_wav


def test_extract_audio_to_wav():
    input_mp4 = Path('AKE100720.mp4')  # テスト用のMP4ファイル

    # テスト用MP4ファイルが存在するかをチェック（存在しなければスキップ）
    if not os.path.exists(input_mp4):
        pytest.skip(f"{input_mp4} が存在しないため、テストをスキップします")

    result = extract_mp4_to_wav(input_mp4)

    assert result is Path(""), "音声抽出が失敗しました"
    assert not result.exists(), "WAVファイルが生成されていません"

    # テスト終了後に出力ファイルを削除
    result.rmdir()
