num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))
suma_total = 0
for i in range(num1, num2 + 1):
    suma_total += i
print(f"La suma de los números entre {num1} y {num2} es: {suma_total}")