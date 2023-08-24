lista = []

while True:

    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce otro número: "))
    
    if (num1==num2):
        print ("Error. Los dos números son iguales.")

    elif (num1 > num2):
        print ("Error. El primer número es mayor que el segundo número.")

    else:

        while num1 <= num2:
            if (num1 % 5 == 0):
                lista.append (num1)
            num1 = num1 + 1
            
        print(lista)
