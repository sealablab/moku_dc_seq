from dataclasses import dataclass
from functools import total_ordering
# python -m unittest test_kvmv.py


@total_ordering
@dataclass
class KvMv:
    v: int  # 5-bit value for whole volts (0-31)
    mv: int = 0  # 10-bit base-2 value for fractional volts (0-1023)
    sign: int = 0  # 1 for negative, 0 for positive

    def __post_init__(self):
        if not (0 <= self.v <= 31):
            raise ValueError("Whole volts (v) must be between 0 and 31.")
        if not (0 <= self.mv <= 1023):
            raise ValueError("Millivolts (mv) must be between 0 and 1023.")
        if self.sign not in {0, 1}:
            raise ValueError("Sign must be 0 (positive) or 1 (negative).")

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

    def to_int(self) -> int:
        """Pack the KvMv instance into a 16-bit integer."""
        return (self.sign << 15) | (self.v << 10) | (self.mv & 0x03FF)

    def to_float(self) -> float:
        """Convert KvMv to a float value."""
        total_volts = self.v + (self.mv / 1024.0)
        if self.sign == 1:
            total_volts = -total_volts
        return total_volts

    @staticmethod
    def from_float(value: float) -> "KvMv":
        """Create a KvMv instance from a floating-point value."""
        sign = 0
        if value < 0:
            sign = 1
            value = -value

        max_voltage = 31 + (1023 / 1024.0)
        if value > max_voltage:
            raise ValueError(f"Value out of range (must be between {-max_voltage} and {max_voltage} volts)")

        v = int(value)
        fractional_part = value - v
        mv = int(round(fractional_part * 1024))

        if mv > 1023:
            mv = 0
            v += 1
            if v > 31:
                raise ValueError(f"Value out of range after rounding.")

        return KvMv(v=v, mv=mv, sign=sign)

    def __neg__(self) -> "KvMv":
        """Negate the KvMv value."""
        return KvMv(self.v, self.mv, 1 - self.sign)

    def __eq__(self, other: "KvMv") -> bool:
        """Equality comparison based on packed integer representation."""
        if not isinstance(other, KvMv):
            return NotImplemented
        return self.to_int() == other.to_int()

    def __lt__(self, other: "KvMv") -> bool:
        """Less-than comparison based on floating-point value."""
        if not isinstance(other, KvMv):
            return NotImplemented
        return self.to_float() < other.to_float()

    def __str__(self) -> str:
        """Convert KvMv to a string representation."""
        return f"{self.to_float():.4f}V"

    def __format__(self, format_spec: str) -> str:
        """Custom formatting for KvMv instances."""
        if not format_spec or format_spec == "":
            return str(self)
        elif format_spec.lower() == "x":
            return f"{self.to_int():04x}"
        else:
            raise TypeError(f"Unsupported format specifier '{format_spec}' for KvMv")

