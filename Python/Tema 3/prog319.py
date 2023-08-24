lista1 = ["1", "3", "7", "15", "18"]

acierto = 0
intentos = 0

while True:
    num1 = input("Introduce un numero: ")

    if num1 in lista1:
        print("Enhorabuena, se sumará un punto a tus aciertos")
        
        acierto = acierto + 1

    elif (num1 == "F") or (num1 == "f"):
        print(f"Felicidades, has acertado {acierto} veces de {intentos} intentos.")
        exit()

    else:
        print("Este número no está en la lista")
    
    intentos = intentos + 1
