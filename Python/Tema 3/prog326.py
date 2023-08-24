import random
lista = []

while len(lista) < 10:
    numero = random.randint(1, 100)

    if numero not in lista:
        lista.append(numero)
        
lista.sort(reverse = True)
print (lista)

posicion = input(f"Introduce una posición del 1 al {len(lista) - 1}: ")

while (posicion != "f") and (posicion != "F"):

    if (len(lista) == 0):
        print("Lista vacía.")
    
    elif (len(lista) < int(posicion) + 1):
        print("Posición fuera de rango")

    else:
        lista.pop(int(posicion))
    
    posicion = input(f"Introduce una posición del 1 al {len(lista) - 1}: ")

lista.sort(reverse = True)
print (lista)