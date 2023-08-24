lista1 = [1, 3, 7, 15, 18]

acierto = 0
contador = 0
repetidos = []

while (contador <= 10):

    num1 = int(input("Introduce un numero: "))

    if num1 in repetidos:
        print ("Este número ya se ha usado antes, podrás repetir el intento.")
        contador = contador - 1

    elif num1 in lista1:
        print("Enhorabuena, se sumará un punto a tus aciertos")
        acierto = acierto + 1

    else:
        print("Este número no está en la lista")
       
    repetidos.append (num1)
    contador = contador + 1

print(f"Felicidades, has conseguido {acierto} aciertos")