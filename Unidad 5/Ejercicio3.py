#Ejercicio 3
import random

numeros = [random.randint(1, 100) for _ in range(15)]

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("Pares:", pares, "Cantidad:", len(pares))
print("Impares:", impares, "Cantidad:", len(impares))
