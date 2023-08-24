nombre = input("Introduce tu nombre: ").capitalize()
apellido = input("Introduce tu apellido: ").capitalize()
localizacion = input("Introduce tu población donde vivas: ").capitalize()

espaciador = ""
cadena1 = (f"Hola {nombre} {apellido}").center(50, " ")
cadena2 = (f"Adiós habitante de {localizacion}").center(50, " ")

print (espaciador.center(50, "="))
print (cadena1)
print (cadena2)
print (espaciador.center(50, "="))