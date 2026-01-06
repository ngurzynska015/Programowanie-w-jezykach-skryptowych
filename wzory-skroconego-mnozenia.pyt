
a_input = input("Podaj wartość a: ")
b_input = input("Podaj wartość b: ")
c_input = input("Podaj wartość c: ")


def to_float(value, name):
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Błąd: Wprowadzono nieprawidłową wartość dla '{name}' (musi być liczbą).")

a = to_float(a_input, "a")
b = to_float(b_input, "b")


c = to_float(c_input, "c")


if any(map(lambda x: isinstance(x, float) is False, [a, b])):
   
    raise ValueError("Wartości a i b muszą być liczbami")


kwadrat_sumy = (a + b) ** 2
kwadrat_roznicy = (a - b) ** 2
roznica_kwadratow = a ** 2 - b ** 2
szescian_sumy = (a + b) ** 3
szescian_roznicy = (a - b) ** 3
suma_szescianow = a ** 3 + b ** 3
roznica_szescianow = a ** 3 - b ** 3
kwadrat_sumy_trzech_skladnikow = (a + b + c) ** 2


print(f"Kwadrat sumy z {a}, {b} wynosi {kwadrat_sumy}")
print(f"Kwadrat różnicy z {a}, {b} wynosi {kwadrat_roznicy}")
print(f"Różnica kwadratów z {a}, {b} wynosi {roznica_kwadratow}")
print(f"Sześcian sumy z {a}, {b} wynosi {szescian_sumy}")
print(f"Sześcian różnicy z {a}, {b} wynosi {szescian_roznicy}")
print(f"Suma sześcianów z {a}, {b} wynosi {suma_szescianow}")
print(f"Różnica sześcianów z {a}, {b} wynosi {roznica_szescianow}")
print(f"Kwadrat sumy trzech składników z {a}, {b} oraz {c} wynosi {kwadrat_sumy_trzech_skladnikow}")
