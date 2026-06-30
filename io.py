"""
io.py
Input / Output utilities for SignalDecoder
"""

import numpy as np
import soundfile as sf
import librosa


class SignalIO:
    """
    Read and write signal files.
    """

    @staticmethod
    def load_wav(file_path, sample_rate=None, mono=True):
        """
        Load a WAV/audio file.

        Parameters
        ----------
        file_path : str
        sample_rate : int or None
            Target sample rate.
        mono : bool
            Convert to mono if True.

        Returns
        -------
        signal : numpy.ndarray
        sr : int
        """

        signal, sr = librosa.load(
            file_path,
            sr=sample_rate,
            mono=mono
        )

        return signal.astype(np.float32), sr

    @staticmethod
    def save_wav(file_path, signal, sample_rate):
        """
        Save signal to WAV file.
        """

        sf.write(
            file_path,
            np.asarray(signal),
            sample_rate
        )

    @staticmethod
    def normalize(signal):
        """
        Normalize signal to [-1,1]
        """

        signal = np.asarray(signal)

        maximum = np.max(np.abs(signal))

        if maximum == 0:
            return signal

        return signal / maximum

    @staticmethod
    def info(signal, sample_rate):
        """
        Return signal information.
        """

        duration = len(signal) / sample_rate

        return {
            "sample_rate": sample_rate,
            "samples": len(signal),
            "duration_sec": duration,
            "min": float(np.min(signal)),
            "max": float(np.max(signal)),
            "mean": float(np.mean(signal)),
            "std": float(np.std(signal))
        }


if __name__ == "__main__":

    print("SignalIO module ready.")

    # Example:
    #
    # signal, sr = SignalIO.load_wav("sample.wav")
    # signal = SignalIO.normalize(signal)
    # print(SignalIO.info(signal, sr))
    # SignalIO.save_wav("output.wav", signal, sr)
