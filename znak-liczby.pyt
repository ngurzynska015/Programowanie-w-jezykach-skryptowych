from __future__ import annotations
from math import hypot, isclose, pi
from typing import List, Optional, Tuple, Union, Dict

Number = Union[int, float]


def znak_liczby(x: Number) -> int:
    
    try:
        if isinstance(x, float) and x != x:  
            return 0
    except Exception:
        pass
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


print("Znak(-2):", znak_liczby(-2))