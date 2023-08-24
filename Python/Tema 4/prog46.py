def prod(*n1):
    aux = 1
    for n in n1:
        aux = aux * n
    return aux

print(prod(2, 25, 42, 7))
