"""
decoder.py
Bitstream Decoder for SignalDecoder
"""

from typing import Iterable


class Decoder:
    def __init__(self):
        pass

    def decode_bits(self, bits: Iterable[int]) -> str:
        """
        Convert iterable of bits to binary string.
        Example:
            [1,0,1,1] -> "1011"
        """
        return "".join(str(int(b)) for b in bits)

    def decode_bytes(self, bits: Iterable[int]) -> bytes:
        """
        Convert bit stream to bytes.
        """
        bit_string = self.decode_bits(bits)

        # Padding
        padding = (8 - len(bit_string) % 8) % 8
        bit_string += "0" * padding

        result = bytearray()

        for i in range(0, len(bit_string), 8):
            result.append(int(bit_string[i:i + 8], 2))

        return bytes(result)

    def decode_ascii(self, bits: Iterable[int]) -> str:
        """
        Decode bit stream as ASCII text.
        """
        try:
            return self.decode_bytes(bits).decode("ascii", errors="ignore")
        except Exception:
            return ""


if __name__ == "__main__":
    decoder = Decoder()

    sample = [1,0,0,0,0,0,1,0]

    print(decoder.decode_bits(sample))
    print(decoder.decode_bytes(sample))
    print(decoder.decode_ascii(sample))
