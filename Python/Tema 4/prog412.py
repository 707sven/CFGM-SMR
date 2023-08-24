# Implementa la función ‘derecha’.
# Tienes su funcionamiento en https://help.libreoffice.org/4.3/Calc/Text_Functions/es#DERECHA

def derecha(text, num):
    aux = ""
    for letra in range(num):
        aux = text[(len(text)-1) - letra] + aux
    return aux

palabra = input("Introduce una palabra: ")
numero = int(input("Introduce un número: "))

while numero > len(palabra):
    numero = int(input("Error. Introduce un número válido: "))

else:
    print(derecha(palabra, numero))

