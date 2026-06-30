"""
parser.py
Frame Parser for SignalDecoder
"""

from typing import List, Dict


class Parser:
    def __init__(self, frame_size: int = 8):
        self.frame_size = frame_size

    def split_frames(self, bit_string: str) -> List[str]:
        """
        Split a binary string into fixed-length frames.
        """
        return [
            bit_string[i:i + self.frame_size]
            for i in range(0, len(bit_string), self.frame_size)
            if len(bit_string[i:i + self.frame_size]) == self.frame_size
        ]

    def frames_to_bytes(self, frames: List[str]) -> List[int]:
        """
        Convert binary frames into integer values.
        """
        return [int(frame, 2) for frame in frames]

    def frames_to_hex(self, frames: List[str]) -> List[str]:
        """
        Convert frames into hexadecimal strings.
        """
        return [hex(int(frame, 2)) for frame in frames]

    def parse(self, bit_string: str) -> Dict:
        """
        Parse a binary stream into multiple formats.
        """
        frames = self.split_frames(bit_string)

        return {
            "frame_count": len(frames),
            "frames": frames,
            "bytes": self.frames_to_bytes(frames),
            "hex": self.frames_to_hex(frames),
        }


if __name__ == "__main__":
    sample = "010000010100001001000011"

    parser = Parser(frame_size=8)

    result = parser.parse(sample)

    print("Frame count:", result["frame_count"])
    print("Frames:", result["frames"])
    print("Bytes:", result["bytes"])
    print("Hex:", result["hex"])
