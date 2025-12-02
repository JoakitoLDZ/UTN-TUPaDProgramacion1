# Punto 1
for i in range(0,101):
    print(i);

#Punto 2
numero = int(input("Ingrese un numero entero: "))
n = abs(numero) # ABS sirve para tener el valor absoluto, lo convierte en positivo

if n == 0:
    cantidad_digitos = 1
else:
    cantidad_digitos = 0
    while n > 0:
        n //= 10
        cantidad_digitos += 1

print("El numero tiene", cantidad_digitos, "digitos.")

# Punto 3
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

# Hacemos que a sea el menor y b el mayor
menor = min(a, b)
mayor = max(a, b)


suma = 0
for i in range(menor + 1, mayor):  # empieza en menor+1 y termina en mayor-1
    suma += i

print("La suma de los enteros entre", menor, "y", mayor, "es:", suma)

# Punto 4
suma = 0   # acumulador

while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print("La suma total es:", suma)

#Punto 5
import random
n=random.randint(0,9)
intentos=0

print("Adivine el numero entre 0 y 9: ")
while True:
    numero=int(input("Ingrese un numero: "))
    intentos+=1
    if numero==n:
        print("Felicidades, adivinaste el numero en", intentos, "intentos")
        break

# Punto 6
for i in range(100, -1, -2):
    print(i)

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

#Punto 9
CANTIDAD = 100   # Cambiar para probar

suma = 0

for i in range(CANTIDAD):
    n = int(input(f"Ingrese el número {i+1}: "))
    suma += n

media = suma / CANTIDAD

print("\nLa media es:", media)

#Punto 10
num = int(input("Ingrese un número: "))
invertido = 0

while num > 0:
    dig = num % 10
    invertido = invertido * 10 + dig
    num //= 10

print("Número invertido:", invertido)
