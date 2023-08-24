def maximo(num1, num2, num3=0):
    lista = [num1, num2, num3]
    aux = lista [0]
    for i in lista:
        if (aux < i):
            aux = i
    return aux

print(maximo(581, 123, 4330))