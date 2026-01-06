from __future__ import annotations
from math import hypot, isclose, pi
from typing import List, Optional, Tuple, Union, Dict

Number = Union[int, float]


def dzielniki(n: int) -> List[int]:
    """
    Zwraca listę dodatnich dzielników liczby n (dla n != 0).
    Dla ujemnych liczb bierze wartość bezwzględną.
    """
    if not isinstance(n, int) or n == 0:
        raise ValueError("n musi być niezerową liczbą całkowitą")
    n = abs(n)
    s = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            s.add(i)
            s.add(n // i)
        i += 1
    return sorted(s)

print("Dzielniki(36):", dzielniki(36))