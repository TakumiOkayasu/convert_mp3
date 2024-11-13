from pathlib import Path
from SoundToText import cut_wav
from MovieToSound import extract_mp4_to_wav
import pytest


def test_cut_wav():
    input_mp4s = Path.cwd().glob('tests/mp4/*.mp4')  # テスト用のMP4ファイル

    if not input_mp4s:
        pytest.skip("テスト用のMP4ファイルが存在しないため、テストをスキップします")

        for mp4 in input_mp4s:
            wav_file = extract_mp4_to_wav(mp4)
            assert not wav_file.exists(), "wavファイルが存在していません"
            cut_lists = cut_wav(wav_file)
            assert len(cut_lists) < 1, "分割されていません"
            wav_file.unlink(missing_ok=True)
