# Punto 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


# Punto 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))


# Punto 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


# Punto 4
import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))

print("Área:", calcular_area_circulo(radio))
print("Perímetro:", calcular_perimetro_circulo(radio))


# Punto 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
print("Equivalen a horas:", segundos_a_horas(segundos))


# Punto 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num)


# Punto 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

suma, resta, multi, div = operaciones_basicas(a, b)

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multi)
print("División:", div)


# Punto 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))

imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")


# Punto 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

c = float(input("Ingrese la temperatura en Celsius: "))
print("Equivalente en Fahrenheit:", celsius_a_fahrenheit(c))


# Punto 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))

print("El promedio es:", calcular_promedio(a, b, c))
