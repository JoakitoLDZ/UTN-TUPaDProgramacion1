# Punto 1
print("Hola Mundo")

#Punto 2
nombre = input("Ingrese su nombre: ")
print (f"Hola, {nombre}!")

#Punto 3
nombre = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad = input ("Ingrese su edad: ")
residencia = input ("Ingrese lugar de residencia: ")
print (f"Hola soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}.")

#Punto 4
import math
radio = float(input("Ingrese el radio de un circulo: "))
area= math.pi * (radio**2)
perimetro=2* math.pi * radio

print (f"El área del círculo es: {area} y el perímetro del círculo es: {perimetro}")

#Punto 5
segundos= float(input("Ingrese cantidad de segundos: "))
horas = segundos/3600
print (f"Los {segundos} segundos son equivalentes a {horas} horas")

#Punto 6
numero = int(input("Ingrese un número: "))

print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#Punto 7
num1=int(input("Ingrese el primer numero (distinto que 0): "))
num2=int(input("Ingrese el segundo numero (distinto que 0): "))

if num1 == 0 or num2 == 0:
    print("Error los números deben ser distintos de 0.")
else:
    suma=num1+num2
    resta=num1-num2
    multi=num1*num2
    div=num1/num2

print(f"Segun los numeros ingresados, el resultado de su suma es igual a {suma}, su resta es igual a {resta}, si los multiplicamos obtendremos el resultado {multi} y si los dividimos tendremos como resultado {div}.")

#Punto 8 
peso=float(input("Indique su peso en kg: "))
estatura=float(input("Indique su altura en metros: "))

imc=peso/(estatura**2)

print(f"Su indice de masa corporal es {imc:.2f}")

#Punto 9
celcius=float(input("Indique grados celcius: "))
farenheit= (1.8*celcius)+32

print(f"Los {celcius} grados celcius son equivalentes a {farenheit} grados farenheit.")

#Punto 10
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
num3=float(input("Ingrese el tercer numero: "))

promedio= (num1+num2+num3)/3

print(f"El promedio de los numeros ingresados es {promedio}")
