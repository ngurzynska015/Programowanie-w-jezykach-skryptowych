from __future__ import annotations
from math import hypot, isclose, pi
from typing import List, Optional, Tuple, Union, Dict

Number = Union[int, float]


def max3(a: Number, b: Number, c: Number) -> Number:
    """Zwraca największą z trzech liczb."""
    return max(a, b, c)

print("Max z (3,7,5):", max3(3, 7, 5))

