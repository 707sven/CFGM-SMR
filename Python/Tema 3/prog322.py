lista = [0, 7, 10, 25, 4, 707]

while True:
    valor = int(input("Introduce un valor a añadir: "))
    posicion = int(input ("Introduce una posición: "))

    if posicion in range (0, len(lista)):
        lista.insert (posicion, valor)
        print (lista)

    elif (posicion < 0):
        print("Error, la lista no acepta posiciones negativas.")
        exit()

    else: 
        print("Error, la lista no tiene una posición tan larga.")