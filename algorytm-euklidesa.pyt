def NWD(a, b):
    a = abs(a)
    b = abs(b)

    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a

print(NWD(48, 18))   
print(NWD(101, 103)) 
