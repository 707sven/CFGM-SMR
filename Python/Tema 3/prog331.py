lista = []
num1 = int(input ("¿Cuantos números quiere en la lista? "))

while (len(lista) < num1):
    numero = int(input("Introduce un número: "))
    lista.append(numero)

menor = lista[0]

for i in lista:
    if (menor > i):
        menor = i

print(f"El número menor de la lista es: {menor}")
