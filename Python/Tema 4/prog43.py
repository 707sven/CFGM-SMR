def multiplica(num1, num2):
    multiplicacion = num1 * num2
    return multiplicacion

n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))

print(f"{n1} x {n2} = {multiplica(n1,n2)}")