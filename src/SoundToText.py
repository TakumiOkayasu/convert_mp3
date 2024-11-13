import os
from pathlib import Path
from numpy import fromstring, int16
import speech_recognition as sr

import wave
import math
import struct

from MovieToSound import extract_mp4_to_wav


# 音声ファイルの分割(デフォルト30秒)


def cut_wav(wavf, time=30):
    # timeの単位は[sec]
    # ファイルを読み出し
    wr = wave.open(wavf, 'r')

    # waveファイルが持つ性質を取得
    ch = wr.getnchannels()
    width = wr.getsampwidth()
    fr = wr.getframerate()
    fn = wr.getnframes()
    total_time = 1.0 * fn / fr
    integer = math.floor(total_time)  # 小数点以下切り捨て
    t = int(time)  # 秒数[sec]
    frames = int(ch * fr * t)
    num_cut = int(integer//t)

    # waveの実データを取得し、数値化
    data = wr.readframes(wr.getnframes())
    wr.close()
    X = fromstring(data, dtype=int16)

    # wavファイルを削除
    os.remove(wavf)

    outf_list = []
    for i in range(num_cut):
        # 出力データを生成
        output_dir = 'output/cut_wav/'
        os.makedirs(output_dir, exist_ok=True)
        outf = output_dir + str(i).zfill(3) + '.wav'
        start_cut = i*frames
        end_cut = i*frames + frames
        Y = X[start_cut:end_cut]
        outd = struct.pack("h" * len(Y), *Y)

        # 書き出し
        ww = wave.open(outf, 'w')
        ww.setnchannels(ch)
        ww.setsampwidth(width)
        ww.setframerate(fr)
        ww.writeframes(outd)
        ww.close()

        # リストに追加
        outf_list.append(outf)

    return outf_list

# 複数ファイルの音声のテキスト変換


def cut_wavs_str(outf_list):
    output_text = ''
    # 複数処理
    print('音声のテキスト変換')
    for fwav in outf_list:
        print(fwav)
        r = sr.Recognizer()

        # 音声->テキスト
        with sr.AudioFile(fwav) as source:
            audio = r.record(source)
        text = r.recognize_google(audio, language='ja-JP')

        # 各ファイルの出力結果の結合
        output_text = output_text + text + '\n'
        # wavファイルを削除
        os.remove(fwav)

    return output_text


# mp4からwavへの変換から音声のテキスト変換まで
def mp4_to_text(mp4file):
    # 出力ディレクトリ
    (Path.cwd() / Path('output/cut_wav/')).mkdir(exist_ok=True)
    print("処理を開始します\n音声ファイルへ変換")

    # 音声ファイルへの変換
    wav_file = extract_mp4_to_wav(mp4file)
    print("音声ファイルの分割")
    # 音声ファイルの分割(デフォルト30秒)
    cut_wavs = cut_wav(wav_file)
    print("テキスト変換")
    # 複数ファイルの音声のテキスト変換
    out_text = cut_wavs_str(cut_wavs)

    # テキストファイルへの入力
    mp4f_name = os.path.basename(mp4file)
    txt_file = 'output/' + mp4f_name.replace('.mp4', '.txt')
    print('テキスト出力')

    with open(txt_file, "w") as f:
        f.write(out_text)
