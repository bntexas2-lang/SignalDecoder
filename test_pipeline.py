"""
test_pipeline.py
End-to-end test for the SignalDecoder project.
"""

import numpy as np

from filters import moving_average
from transition_detector import detect_transitions
from frame_detector import detect_frames
from correlation import normalized_correlation
from utils import normalize

from demodulator import Demodulator
from decoder import Decoder
from parser import Parser


def main():
    print("=" * 50)
    print("SignalDecoder Pipeline Test")
    print("=" * 50)

    # Example input signal
    signal = np.array([
        -0.8, -0.6, -0.2,
         0.5,  0.9,  0.8,
        -0.4, -0.7,
         0.4,  0.8,  1.0,
        -0.5
    ])

    print("\nOriginal Signal:")
    print(signal)

    # Normalize
    signal = normalize(signal)

    # Filter
    filtered = moving_average(signal, 3)

    # Transition Detection
    transitions = detect_transitions(filtered)

    # Frame Detection
    frames = detect_frames(filtered, threshold=0.5)

    # Demodulation
    demod = Demodulator(threshold=0.5)
    bits = demod.demodulate(filtered)

    # Decode
    decoder = Decoder()
    bit_string = decoder.decode_bits(bits)

    # Parse
    parser = Parser(frame_size=8)
    parsed = parser.parse(bit_string)

    # Correlation Example
    corr = normalized_correlation(filtered, filtered)

    print("\nFiltered Signal:")
    print(filtered)

    print("\nDetected Transitions:")
    print(transitions)

    print("\nDetected Frames:")
    print(frames)

    print("\nBit Stream:")
    print(bit_string)

    print("\nParsed Frames:")
    print(parsed)

    print("\nSelf Correlation:")
    print(corr)

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    main()
