num = int(input("Escribe un número del 1 al 20: "))

if (num > 20) or (num < 1):
    print(f"Error. El número {num} no está entre 1 y 20.")
else:
    for i in range (1, num + 1):
        print(f"{i}")
