from __future__ import annotations
from math import hypot, isclose, pi
from typing import List, Optional, Tuple, Union, Dict

Number = Union[int, float]


def czy_trojkat(a: Number, b: Number, c: Number) -> bool:
    """Sprawdza, czy z odcinków a, b, c da się zbudować trójkąt."""
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a

print("Trójkąt(3,4,5):", czy_trojkat(3, 4, 5))
