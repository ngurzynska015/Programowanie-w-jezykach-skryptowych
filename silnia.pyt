def silnia(n: int) -> int:
    """Zwraca n! dla n ≥ 0."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n musi być całkowite i ≥ 0")
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

print("Silnia(20):", silnia(20))
