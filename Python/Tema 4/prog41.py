
def checkRango(num1):
    if (int(num1) <= 10) and (int(num1) >= 1):
        print("El número está entre 1 y 10.")
    else:
        print("El número no está entre 1 y 10.")

n1 = input("Introduce un número: ")
while not n1.isnumeric():
        n1 = input("Introduce un número: ")

checkRango(n1)
