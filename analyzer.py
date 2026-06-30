import os

from config import INPUT_FILE, OUTPUT_DIR

from signal_io import SignalIO
from filters import moving_average
from demodulator import Demodulator
from decoder import Decoder
from parser import Parser
from visualizer import Visualizer
from export import Exporter


class Analyzer:

    def run(self):

        print("[1/6] Loading signal...")

        signal, sr = SignalIO.load_wav(INPUT_FILE)

        signal = SignalIO.normalize(signal)

        print("[2/6] Filtering...")

        filtered = moving_average(signal, 5)

        print("[3/6] Demodulating...")

        demod = Demodulator(threshold=0.5)
        bits = demod.demodulate(filtered)

        print("[4/6] Decoding...")

        decoder = Decoder()
        bitstream = decoder.decode_bits(bits)

        print("[5/6] Parsing...")

        parser = Parser()
        result = parser.parse(bitstream)

        print("[6/6] Saving results...")

        os.makedirs(OUTPUT_DIR, exist_ok=True)

        Exporter.export_json(result, os.path.join(OUTPUT_DIR, "result.json"))
        Exporter.export_txt(result, os.path.join(OUTPUT_DIR, "result.txt"))

        Visualizer.plot_signal(filtered)
        Visualizer.plot_bits(bits)

        print("\nFinished Successfully.")
