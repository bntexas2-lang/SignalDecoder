
import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert
from config import INPUT_FILE

class Analyzer:
    def run(self):
        audio,sr=librosa.load(INPUT_FILE,sr=None,mono=True)
        audio=audio-np.mean(audio)
        audio=audio/np.max(np.abs(audio))
        env=np.abs(hilbert(audio))
        t=np.arange(len(audio))/sr
        plt.figure(figsize=(14,3))
        plt.plot(t,audio)
        plt.title("Waveform")
        plt.grid()
        plt.figure(figsize=(14,3))
        plt.plot(t,env)
        plt.title("Envelope")
        plt.grid()
        plt.show()
