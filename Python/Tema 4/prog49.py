def sumar(num1, num2):
    suma = num1 + num2
    return suma

def restar(num1, num2):
    resta = num1 - num2
    return resta

def dividir (num1, num2):
    try:
        division = num1 / num2
    except ZeroDivisionError:
        return ("Se ha dividido por cero")

    return division

def multiplicar (num1, num2):
    multiplicacion = num1 * num2
    return multiplicacion

def menu ():
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Dividir")
    print("4.- Multiplicar")
    print("5.- Salir")

def pedir_numeros():
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))

    return n1, n2

def opcion():
    op=int(input("Introduzca opción (1-5): "))

    if op == 1:
        n1, n2 = pedir_numeros()
        print(f"{n1} + {n2} = {sumar(n1, n2)}")

    elif op == 2:
        n1, n2 = pedir_numeros()

        print(f"{n1} - {n2} = {restar(n1,n2)}")

    elif op == 3:
        n1, n2 = pedir_numeros()
        print(f"{n1} / {n2} = {dividir(n1,n2)}")
    elif op == 4:
        n1, n2 = pedir_numeros()

        print(f"{n1} x {n2} = {multiplicar(n1,n2)}")

    elif op == 5:
        print("Hasta la próxima.")
        exit()

    else:
        print("Esta opción no está en el menú.")
        menu()
        opcion()

menu()
opcion()