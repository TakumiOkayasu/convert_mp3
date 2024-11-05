from pydub import AudioSegment
from pathlib import Path


def extract_mp4_to_wav(movieFullPath: Path, input_format="mp4", output_format="wav") -> Path:
    try:
        output_file = Path(movieFullPath.stem + output_format)

        # 入力ファイルをロード
        audio = AudioSegment.from_file(movieFullPath, format=input_format)

        # 指定された形式で出力
        audio.export(output_file, format=output_format)

        print(f"変換が完了しました: {movieFullPath} ({
              input_format}) -> {output_file} ({output_format})")

        return output_file

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return Path("")
