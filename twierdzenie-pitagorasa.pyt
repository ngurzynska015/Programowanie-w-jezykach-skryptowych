from __future__ import annotations
from math import hypot, isclose, pi
from typing import List, Optional, Tuple, Union, Dict

Number = Union[int, float]


def pitagoras(a: Number, b: Number) -> float:
    """Zwraca długość przeciwprostokątnej dla przyprostokątnych a i b."""
    return hypot(a, b)  # stabilniejsze numerycznie


def czy_prostokatny(a: Number, b: Number, c: Number, eps: float = 1e-12) -> bool:
    """Sprawdza, czy trójkąt o bokach a, b, c jest prostokątny."""
    boky = sorted([a, b, c])
    p, q, r = boky
    return isclose(r * r, p * p + q * q, rel_tol=0, abs_tol=eps)


print("Pitagoras(3,4):", pitagoras(3, 4))
print("Czy prostokątny(3,4,5):", czy_prostokatny(3, 4, 5))
