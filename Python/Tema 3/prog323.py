import random
lista = []

while len(lista) < 10:
    numero = random.randint(1, 100)

    if numero not in lista:
        lista.append(numero)
        
lista.sort(reverse = True)
print (lista)

