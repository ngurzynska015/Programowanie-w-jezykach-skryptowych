from __future__ import annotations
from math import hypot, isclose, pi
from typing import List, Optional, Tuple, Union, Dict

Number = Union[int, float]


def wartosc_bezwzgledna(x: Number) -> Number:
    """Zwraca |x|."""
    return abs(x)

print("| -7 |:", wartosc_bezwzgledna(-7))

