# Implementa la función ‘nompropio’.
# Tienes su funcionamiento en https://help.libreoffice.org/4.3/Calc/Text_Functions/es#NOMPROPIO.

def nompropio(texto):
    texto_final = ""
    for letra in range(len(texto)):
        if letra == 0:
            if (ord(texto[0]) >= 97) and (ord(texto[0]) <= 122):
                primera_mayuscula = ord(texto[0]) - 32
                texto_final = chr(primera_mayuscula)
            
            else:
                texto_final = texto[letra]
                
        else:
            if (ord(texto[letra - 1]) == 32):
                if (ord(texto[letra]) >= 97) and (ord(texto[letra]) <= 122):
                    letra_siguiente = ord(texto[letra])
                    letra_siguiente_mayuscula = chr(letra_siguiente - 32)
                    texto_final += letra_siguiente_mayuscula

                else:
                    texto_final += texto[letra]
            
            else:
                texto_final += texto[letra]

    return texto_final

palabra = input("Introduce una palabra: ")

print(nompropio(palabra))