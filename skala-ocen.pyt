def skala_ocen(percent: float) -> int:
    """Zwraca ocenę 1–6 dla procentu 0–100 zgodnie z przykładowymi progami."""
    if percent < 0 or percent > 100:
        raise ValueError("Procent musi być w zakresie 0–100")
    if percent < 40:
        return 1
    if percent < 56:
        return 2
    if percent < 71:
        return 3
    if percent < 86:
        return 4
    if percent < 96:
        return 5
    return 6

print("Skala ocen(83%):", skala_ocen(83))

