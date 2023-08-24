import random
lista = []

while len(lista) < 10:
    numero = random.randint(1, 100)

    if numero not in lista:
        lista.append(numero)
        
lista.sort(reverse = True)
print (lista)

for x in range (5):

        num = int(input("Escribe un número: "))

        if num not in lista:
            print("Este número no está en la lista")

        else:
            print("El número será eliminador de la lista.")
            lista.remove(int(num))
            
        print(lista)   

