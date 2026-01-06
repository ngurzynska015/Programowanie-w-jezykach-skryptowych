

from __future__ import annotations
from math import hypot, isclose, pi
from typing import List, Optional, Tuple, Union, Dict

Number = Union[int, float]

def cwiartka(x: Number, y: Number) -> str:
   
    if x == 0 and y == 0:
        return 
    if x == 0:
        return 
    if y == 0:
        return 
    if x > 0 and y > 0:
        return 
    if x < 0 and y > 0:
        return 
    if x < 0 and y < 0:
        return 
    return 

print("Ćwiartka(2,-3):", cwiartka(2, -3))