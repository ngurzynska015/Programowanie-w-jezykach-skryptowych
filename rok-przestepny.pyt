def czy_rok_przestepny(year: int) -> bool:
    """Zwraca True, jeśli rok jest przestępny."""
    if not isinstance(year, int):
        raise ValueError("Rok musi być liczbą całkowitą")
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

print("Rok 2075 przestępny?:", czy_rok_przestepny(2075))