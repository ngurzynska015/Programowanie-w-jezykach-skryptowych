

from __future__ import annotations
from math import hypot, isclose, pi
from typing import List, Optional, Tuple, Union, Dict

Number = Union[int, float]

def blad_bezwzgledny(measured: Number, true_value: Number) -> float:
   
    return abs(measured - true_value)


def blad_wzgledny(measured: Number, true_value: Number, as_percent: bool = True) -> float:

    abs_err = blad_bezwzgledny(measured, true_value)
    if true_value == 0:
        return float("inf")
    rel = abs_err / abs(true_value)
    return rel * 100 if as_percent else rel

print("Błąd bezwzgledny/wzgledny:", blad_bezwzgledny(9.8, 10), blad_wzgledny(9.8, 10))