"""
cli.py
Command Line Interface for SignalDecoder
"""

import argparse
from pathlib import Path

from signal_io import SignalIO
from filters import moving_average
from demodulator import Demodulator
from decoder import Decoder
from parser import Parser
from export import Exporter


def process_file(input_file, output_prefix="result", sample_rate=None):
    """
    Complete signal processing pipeline.
    """

    print(f"[INFO] Loading file: {input_file}")

    signal, sr = SignalIO.load_wav(
        input_file,
        sample_rate=sample_rate
    )

    signal = SignalIO.normalize(signal)

    print("[INFO] Filtering signal...")
    filtered = moving_average(signal, 5)

    print("[INFO] Demodulating...")
    demod = Demodulator(threshold=0.5)
    bits = demod.demodulate(filtered)

    print("[INFO] Decoding...")
    decoder = Decoder()
    bit_string = decoder.decode_bits(bits)

    print("[INFO] Parsing...")
    parser = Parser(frame_size=8)
    parsed = parser.parse(bit_string)

    print("[INFO] Exporting results...")
    Exporter.export_all(parsed, output_prefix)

    print("[DONE]")
    print(f"Files created:")
    print(f"  {output_prefix}.json")
    print(f"  {output_prefix}.csv")
    print(f"  {output_prefix}.txt")


def build_parser():

    parser = argparse.ArgumentParser(
        description="SignalDecoder Command Line Interface"
    )

    parser.add_argument(
        "input",
        help="Input WAV file"
    )

    parser.add_argument(
        "-o",
        "--output",
        default="result",
        help="Output filename prefix"
    )

    parser.add_argument(
        "--sample-rate",
        type=int,
        default=None,
        help="Resample audio before processing"
    )

    return parser


def main():

    parser = build_parser()

    args = parser.parse_args()

    input_path = Path(args.input)

    if not input_path.exists():
        print(f"[ERROR] File not found: {input_path}")
        return

    process_file(
        input_file=input_path,
        output_prefix=args.output,
        sample_rate=args.sample_rate
    )


if __name__ == "__main__":
    main()
