"""
demodulator.py
Digital Signal Demodulator
Supports simple threshold-based ASK/OOK demodulation.
"""

import numpy as np


class Demodulator:
    def __init__(self, threshold=0.0):
        self.threshold = threshold

    def set_threshold(self, threshold):
        self.threshold = threshold

    def demodulate(self, samples):
        """
        Convert analog samples into binary bits.

        Parameters
        ----------
        samples : list or numpy array

        Returns
        -------
        numpy.ndarray
            Array containing 0 and 1.
        """
        samples = np.asarray(samples, dtype=float)
        bits = (samples > self.threshold).astype(np.uint8)
        return bits

    def demodulate_inverted(self, samples):
        """
        Inverted threshold demodulation.
        """
        samples = np.asarray(samples, dtype=float)
        bits = (samples <= self.threshold).astype(np.uint8)
        return bits

    def statistics(self, samples):
        """
        Return basic signal statistics.
        """
        samples = np.asarray(samples, dtype=float)

        return {
            "min": float(np.min(samples)),
            "max": float(np.max(samples)),
            "mean": float(np.mean(samples)),
            "std": float(np.std(samples)),
            "threshold": self.threshold,
        }


if __name__ == "__main__":
    signal = np.array([
        -0.8, -0.2, 0.4, 0.9,
        -0.1, 0.6, 0.8, -0.5
    ])

    demod = Demodulator(threshold=0.0)

    bits = demod.demodulate(signal)

    print("Signal:", signal)
    print("Bits:", bits)
    print("Statistics:", demod.statistics(signal))
