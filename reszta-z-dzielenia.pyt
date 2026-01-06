from __future__ import annotations
from math import hypot, isclose, pi
from typing import List, Optional, Tuple, Union, Dict

Number = Union[int, float]


def modulo(a: Number, b: Number) -> Number:
    
    if b == 0:
        raise ZeroDivisionError("Modulo przez zero!")
    return ((a % b) + b) % b

print("Modulo(-3,5):", modulo(-3, 5))
