# Punto 7
numero = int(input("Ingrese un número entero positivo: "))

# Asegurarse de que sea positivo
if numero < 0:
    print("El número debe ser positivo.")
else:
    suma = 0
    for i in range(numero + 1):  # de 0 hasta numero inclusive
        suma += i

    print("La suma de los números de 0 a", numero, "es:", suma)
