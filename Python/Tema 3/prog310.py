num1 = int(input("Escribe un número de inicio entre 1 y 20: "))
num2 = int(input("Escribe un número para el final entre 1 y 20: "))

if (num1 > 20) or (num1 < 1):
    print(f"Error. El número {num1} no está entre 1 y 20.")

elif(num2 > 20) or (num2 < 1):
    print(f"Error. El número {num2} no está entre 1 y 20.")

elif (num1 == num2):
    print("Error. Los números son iguales")

elif (num1 > num2):
    print("Error. El primer número no puede ser mayor que el segundo.")
    
else:
    for i in range (num1, num2 + 1):
        print(f"{i}")