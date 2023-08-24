# Implementa la función "mid"
# Tienes su funcionamiento en https://help.libreoffice.org/4.3/Calc/Text_Functions/es#COMPACTAR_2

def mid (texto, comienzo, numero):
    texto_final = ""

    for i in range(numero):
        texto_final = texto_final + texto[comienzo - 1]
        comienzo = comienzo + 1
    
    return texto_final

palabra = input("Introduce una palabra: ")
posicion = int(input("Introduce una posicion: "))
cantidad = int(input("Introduce un número: "))

while (posicion > len(palabra)) or (cantidad > len(palabra)):
    posicion = int(input("Error. Introduce una posición válida: "))
    cantidad = int(input("Introduce una cantidad válida: "))

else:
    print(mid(palabra, posicion, cantidad))