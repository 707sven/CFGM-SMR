# Implementa la función ‘mayusculas’.
# Tienes su funcionamiento en https://help.libreoffice.org/4.3/Calc/Text_Functions/es#MAY.C3.9ASC.
# chr (cardinal)
# ord (ordinal)

def mayusculas(cadena):
    mayuscula = ""
    for letra in cadena:
        if (ord(letra) >= 97) and (ord(letra) <= 122):
            representacion = ord(letra)
            mayuscula += chr(representacion - 32)
        else:
            mayuscula += letra

    return mayuscula

texto = input("Introduce un texto en minúsculas: ")
print (mayusculas(texto))