num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))

if (num1>num2):
    print(f"El numero mayor es {num1} y el numero menor es {num2}")
elif (num1<num2):
    print(f"El numero mayor es {num2} y el numero menor es {num1}")
else:
    print("Los números son iguales.")