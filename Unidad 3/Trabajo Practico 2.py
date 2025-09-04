#Punto 1
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#Punto 2
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Punto 3
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#Punto 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18 and edad >= 12:
    print("Adolescente")
elif edad < 30 and edad >= 12 :
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Punto 5
contrasena = input("Ingrese su contraseña: ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Punto 6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")

#Punto 7
texto = input("Ingrese una frase o palabra: ")
if texto[-1].lower() in "aeiou":
    texto += "!"
print(texto)

#Punto 8
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese 1, 2 o 3 según la opción deseada: ")
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())

#Punto 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

#Punto 10
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día: "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
else:
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"

print(estacion)
