oceny = [4.5, 3.5, 5.0, 5.0]
suma = sum(oceny)
srednia = suma / len(oceny)


for index, ocena in enumerate(oceny, start=1):
    print(f"Ocena {index}: {ocena}")


print(f"Średnia arytmetyczna: ({' + '.join(map(str, oceny))}) / {len(oceny)} = {srednia:.2f}")
