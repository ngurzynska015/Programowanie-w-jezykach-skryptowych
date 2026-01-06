from __future__ import annotations
from math import hypot, isclose, pi
from typing import List, Optional, Tuple, Union, Dict

Number = Union[int, float]


def kalkulator(a: Number, op: str, b: Number) -> Number:
    """Wykonuje działanie a (op) b dla op ∈ {+, -, *, /, %, ^}."""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Dzielenie przez zero!")
        return a / b
    if op == "%":
        
        return a % b
    if op == "^":
        return a ** b
    raise ValueError(f"Nieznany operator: {op}")

print("Kalkulator 6 / 3:", kalkulator(6, "/", 3))
