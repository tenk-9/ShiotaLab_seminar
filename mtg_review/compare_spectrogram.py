import librosa
import numpy as np
# import numpy.typing as npt
import os
from typing import *
from matplotlib import pyplot as plt
import cv2

DIR: Final = os.path.dirname(__file__)
WAV_16K: Final[str] = f"{DIR}/16k.wav"
WAV_8K: Final[str] = f"{DIR}/8k.wav"

N_FFT: Final[int] = 2048
WIN_LEN: Final[int] = 1024
HOP_LEN: Final[int] = WIN_LEN // 4

def gen_spectrogram(file_path: str, sample_rate: int) -> plt.figure:
    # wav: npt.NDArray[np.float32]
    # sr: int
    # D: npt.NDArray[Shape["1+N_FFT//2, ..."], np.float32]
    # ^ typing diffffff
    
    # stft process
    wav,sr = librosa.load(file_path, sr=sample_rate)
    D = librosa.stft(
        wav,
        n_fft=N_FFT,
        hop_length=HOP_LEN,
        win_length=WIN_LEN,
        window="hann",
    )
    D = np.abs(D)
    D = librosa.amplitude_to_db(D, ref=np.max)
    
    # gen img
    fig, ax = plt.subplots(nrows=1, ncols=1)
    img = librosa.display.specshow(
        D, sr=sr,
        x_axis='time',
        y_axis='linear',
        ax=ax,
    )
    ax.set_ylim(0, 8000)
    ax.set_title(f"sample_rate={sr}, win_length={WIN_LEN}, hop_length={HOP_LEN}")
    return fig

if __name__ == "__main__":
    gen_spectrogram(WAV_16K, 16000)
    plt.savefig(f"{DIR}/16000.png")
    gen_spectrogram(WAV_16K, 8000)
    plt.savefig(f"{DIR}/8000.png")
    
    # joint fig
    im16 = cv2.imread(f"{DIR}/16000.png")
    im8 = cv2.imread(f"{DIR}/8000.png")
    cv2.imwrite(f"{DIR}/compare.png", cv2.hconcat([im8, im16]))
