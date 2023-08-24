numero = int(input("Introduce un número del 1 al 10: "))
contador = 0

if (numero > 10) or (numero < 1):
    print("Error. El número introducido no está dentro del rango.")
    numero = int(input("Introduce un número del 1 al 10: "))
else:
    while (contador <= 10) and (contador >= 0):
        multiplicacion = numero * contador
        print(f"{numero} x {contador} = {multiplicacion}")
        contador = contador + 1