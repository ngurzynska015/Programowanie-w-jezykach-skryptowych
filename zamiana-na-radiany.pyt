from __future__ import annotations
from math import hypot, isclose, pi
from typing import List, Optional, Tuple, Union, Dict

Number = Union[int, float]


def stopnie_na_radiany(deg: Number) -> float:
   
    return float(deg) * pi / 180.0

print("45° -> rad:", stopnie_na_radiany(45))