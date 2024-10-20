from pathlib import Path

import ffmpeg


def is_mp4(fullPath: Path) -> bool:
    try:
        probe = ffmpeg.probe(fullPath)
        return probe['format']['format_name'] == 'mov,mp4,m4a,3gp,3g2,mj2'
    except ffmpeg.Error:
        return False


def extract_mp4_to_wav(mp4FullPath: Path) -> Path:
    wav_path = Path(mp4FullPath.stem + ".wav")
    try:
        ffmpeg.input(mp4FullPath).output(mp4FullPath.parent.cwd() / wav_path,
                                         format='wav', acodec='pcm_s16le', ar='44100', ac=2).run()
        return wav_path

    except ffmpeg.Error as e:
        print(f'Error extracting audio: {e}')

    finally:
        return Path("")
