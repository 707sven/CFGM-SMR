# Crea una función que se llame ‘concatenar’.
# Esta función recibirá dos cadenas y devolverá una cadena con esas dos cadenas concatenadas.

from http.client import REQUEST_URI_TOO_LONG


def concatenar (cd1, cd2):
    completa = (cd1 + " " + cd2)

    return (completa)

cadena1 = str(input("Primera parte de la cadena: "))
cadena2 = str(input("Segunda parte de la cadena: "))

print(concatenar(cadena1, cadena2))