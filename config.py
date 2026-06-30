
from pathlib import Path

ROOT = Path(__file__).parent
INPUT_DIR = ROOT / "input"
OUTPUT_DIR = ROOT / "output"
INPUT_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

INPUT_FILE = INPUT_DIR / "sample.m4a"
LOWCUT = 200
HIGHCUT = 8000
FRAME_THRESHOLD = 0.35
