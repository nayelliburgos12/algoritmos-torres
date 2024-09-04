num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

if suma > multiplicacion:
    print("La suma es mayor que la multiplicación.")
else:
    print("La multiplicación es mayor o igual que la suma.")
