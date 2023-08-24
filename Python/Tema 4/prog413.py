# Implementa la función ‘repetir’.
# Tienes su funcionamiento en https://help.libreoffice.org/4.3/Calc/Text_Functions/es#REPETIR

def repetir(text, num):
    textoRepetido = ""
    for i in range(num):
        textoRepetido = textoRepetido + text

    return textoRepetido

texto = input("Introduce un texto: ")
numRepeticiones = int(input("Introduce un número de repetición: "))

print(repetir(texto, numRepeticiones))