def suma(num1, num2):
    suma = num1 + num2
    return suma

n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))

print(f"{n1} + {n2} = {suma(n1, n2)}")