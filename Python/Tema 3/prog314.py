num = int(input("Escribe un número del 1 al 20: "))

if (num > 20) or (num < 1):
    print(f"Error. El número {num} no está entre 1 y 20.")
else:
    i = 1
    while i < (num + 1):
        print(f"{i}")
        i += 1