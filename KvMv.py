from dataclasses import dataclass


@dataclass
class KvMv:
    sign: int = 0  # 1 for negative, 0 for positive
    v: int  # 5-bit value for whole volts (0-31)
    mv: int  # 10-bit value for millivolts (0-999)

    def __post_init__(self):
        # Ensure v and mv are within valid ranges
        if not (0 <= self.v <= 31):
            raise ValueError("Whole volts (v) must be between 0 and 31.")
        if not (0 <= self.mv <= 999):
            raise ValueError("Millivolts (mv) must be between 0 and 999.")

    def __str__(self) -> str:
        """
        Override the default string representation to call to_str().
        """
        return self.to_str()

    def to_str(self) -> str:
        """
        Convert the KvMv instance to a string representation with 4 decimal places.
        """
        total_volts = self.v + (self.mv / 1000.0)
        if self.sign == 1:
            total_volts = -total_volts
        return f"{total_volts:.4f}V"

    def to_int(self) -> int:
        """
        Pack the KvMv into a 16-bit integer.
        """
        packed = (self.sign << 15) | (self.v << 10) | (self.mv & 0x03FF)
        return packed

    @staticmethod
    def from_int(value: int) -> "KvMv":
        """
        Unpack a 16-bit integer into a KvMv instance.
        """
        if not (0 <= value <= 0xFFFF):
            raise ValueError("Value must be a 16-bit integer (0-65535).")
        sign = (value >> 15) & 0x01
        v = (value >> 10) & 0x1F
        mv = value & 0x03FF
        return KvMv(v=v, mv=mv, sign=sign)


if __name__ == "__main__":
    for i in range(0, 5):
        for j in range(1, 4):
            curr_v = KvMv(i, j)
            print("As a str: %s" % (curr_v))
