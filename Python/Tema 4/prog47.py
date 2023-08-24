def promedio(*n1):
    aux = 0
    for n in n1:
        aux = aux + n
    aux = aux / len(n1)
    
    return aux
    
print(promedio(5, 6, 10))
