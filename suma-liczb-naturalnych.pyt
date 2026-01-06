def suma_naturalnych(n: int) -> int:
    """Zwraca sumę 1 + 2 + ... + n. Dla n=0 zwraca 0."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n musi być całkowite i ≥ 0")
    return n * (n + 1) // 2


print("Suma 100 liczb naturalnych wynosi", suma_naturalnych(100))
