# Implementa la función ‘minúsculas”.
# Tienes su funcionamiento en https://help.libreoffice.org/4.3/Calc/Text_Functions/es#MINUSC
# chr (cardinal)
# ord (ordinal)

def mayusculas(cadena):
    minuscula = ""
    for letra in cadena:
        if (ord(letra) >= 65) and (ord(letra) <= 90):
            representacion = ord(letra)
            minuscula += chr(representacion + 32)
        else:
            minuscula += letra

    return minuscula

texto = input("Introduce un texto en mayúsculas: ")
print(mayusculas(texto))