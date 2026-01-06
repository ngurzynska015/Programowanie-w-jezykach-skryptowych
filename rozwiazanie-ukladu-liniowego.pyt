from __future__ import annotations
from math import hypot, isclose, pi
from typing import List, Optional, Tuple, Union, Dict

Number = Union[int, float]

def rozwiaz_uklad_2x2(
    a: Number, b: Number, e: Number, c: Number, d: Number, f: Number, eps: float = 1e-12
) -> Optional[Dict[str, float]]:
   
    det = a * d - b * c
    if abs(det) < eps:
        return None
    x = (e * d - b * f) / det
    y = (a * f - e * c) / det
    return {"x": x, "y": y}

print("Układ 2x2:", rozwiaz_uklad_2x2(2, 1, 5, 1, -1, 1))
