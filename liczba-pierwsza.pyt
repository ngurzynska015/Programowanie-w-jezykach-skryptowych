
number = 2
is_prime = True

for i in range(2, number // 2 + 1):
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print("Liczba jest pierwsza")
else:
    print("Liczba nie jest pierwsza")
