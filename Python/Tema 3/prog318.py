lista1 = [1, 3, 7, 15, 18]

acierto = 0

for i in range (10):
    num1 = int(input("Introduce un numero: "))

    if num1 in lista1:
        print("Enhorabuena, se sumará un punto a tus aciertos")

        acierto = acierto + 1

    else:
        print("Este número no está en la lista")

print(f"Felicidades, has conseguido {acierto} aciertos")
