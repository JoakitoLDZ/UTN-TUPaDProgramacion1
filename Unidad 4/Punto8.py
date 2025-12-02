#Punto 8
CANTIDAD = 100   # Cambiar a un número menor para pruebas

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(CANTIDAD):
    n = int(input(f"Ingrese el número {i+1}: "))

    # Par / Impar
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Positivo / Negativo
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

print("\nRESULTADOS:")
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)
