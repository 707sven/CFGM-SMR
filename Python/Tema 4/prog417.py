# Implementa la función ‘decimalABinario’. Pasa un número decimal positivo a binario.
# Devolverá una cadena, texto, representado el binario de la cadena pasada en el argumento.

def decimalBinario (decimal):
    binario = 0
    multiplicador = 1

    while decimal != 0:
        binario = binario + decimal % 2 * multiplicador
        decimal //= 2
        multiplicador *= 10

    return binario

numero = int(input("Introduce un número positivo: "))


print(decimalBinario(numero))