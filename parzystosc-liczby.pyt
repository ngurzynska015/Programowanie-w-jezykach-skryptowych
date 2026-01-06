def czy_parzysta(n: int) -> bool:
    
    return isinstance(n, int) and n % 2 == 0

print("Parzysta(12):", czy_parzysta(12))
