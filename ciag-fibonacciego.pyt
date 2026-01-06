def fibonacci(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        b = b + a
        a = b - a
    return b


for i in range(30):
    print(fibonacci(i))
