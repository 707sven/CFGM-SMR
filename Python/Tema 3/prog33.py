num1 = int(input("Introduce un número positivo menor que 57: "))
num2 = int(input("Introduce otro número positivo menor que 57: "))

if (num1 >= 57) or (num1 < 0):
    print("Fallo. El numero 1 es negativo, mayor o igual que 57.")
elif (num2 >= 57) or (num2 < 0):
    print("Fallo. El numero 2 es negativo, mayor o igual que 57.")
else:
    print(f"El producto de ambos numeros es {num1 * num2}")
