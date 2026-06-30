"""
visualizer.py
Signal visualization utilities for SignalDecoder
"""

import matplotlib.pyplot as plt
import numpy as np


class Visualizer:

    @staticmethod
    def plot_signal(signal, title="Signal", xlabel="Sample", ylabel="Amplitude"):
        signal = np.asarray(signal)

        plt.figure(figsize=(12, 4))
        plt.plot(signal)

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_bits(bits, title="Decoded Bits"):
        bits = np.asarray(bits)

        plt.figure(figsize=(12, 3))
        plt.step(range(len(bits)), bits, where="mid")

        plt.ylim(-0.2, 1.2)
        plt.title(title)
        plt.xlabel("Bit Index")
        plt.ylabel("Bit")

        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def compare(original, processed):
        original = np.asarray(original)
        processed = np.asarray(processed)

        plt.figure(figsize=(12, 5))

        plt.plot(original, label="Original")
        plt.plot(processed, label="Processed")

        plt.title("Signal Comparison")
        plt.xlabel("Sample")
        plt.ylabel("Amplitude")

        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

    @staticmethod
    def histogram(signal):
        signal = np.asarray(signal)

        plt.figure(figsize=(8, 4))
        plt.hist(signal, bins=30)

        plt.title("Signal Histogram")
        plt.xlabel("Amplitude")
        plt.ylabel("Count")

        plt.grid(True)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    signal = np.random.randn(500)

    Visualizer.plot_signal(signal)
    Visualizer.histogram(signal)
