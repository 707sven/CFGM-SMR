def suma(*n1):
    aux = 0
    for n in n1:
        aux = aux + n
    return aux

print(suma(5, 12, 75, 2, 45, 1, 23))
