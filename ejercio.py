# Solicitar al usuario su nombre y edad
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

# Solicitar el año actual
año_actual = int(input("Ingresa el año actual: "))

# Calcular el año en el que cumplirá 100 años
año_cumple_100 = año_actual + (100 - edad)

# Imprimir el resultado
print(f"{nombre}, cumplirás 100 años en el año {año_cumple_100}.")
