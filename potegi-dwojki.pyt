from __future__ import annotations
from math import hypot, isclose, pi
from typing import List, Optional, Tuple, Union, Dict

Number = Union[int, float]


def czy_potega_dwojki(n: int) -> bool:
    
    return isinstance(n, int) and n > 0 and (n & (n - 1)) == 0


def potegi_dwojki(k: int) -> List[int]:

    if not isinstance(k, int) or k < 0:
        raise ValueError("k musi być liczbą całkowitą ≥ 0")
    out = []
    p = 1
    for _ in range(k):
        out.append(p)
        p <<= 1  # szybkie mnożenie przez 2
    return out


print("Czy potęga 2 (16):", czy_potega_dwojki(16))  
print("Potęgi 2 (k=5):", potegi_dwojki(5))
