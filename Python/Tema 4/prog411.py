# Ahora la función ‘concatenar’ recibirá un número indeterminado de cadenas
# y devolverá todas éllas concatenadas en una sola cadena.

def concatenar (*cd):
    cadena = ""
    for i in cd:
        cadena += i + " "

    return(cadena)

print(concatenar("patatas", "huevos", "árboles"))