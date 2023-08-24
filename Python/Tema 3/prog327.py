listanombres = []
nombre = input("Introduce un nombre: ")

while (nombre!="F") and (nombre!="f"):
    
    if (nombre not in listanombres):
        listanombres.append(nombre)       

    nombre = input("Introduce un nombre: ")

listanombres.sort()
print(listanombres)

listacopiada = listanombres.copy()

listacopiada.sort(reverse = True)
print (listacopiada)