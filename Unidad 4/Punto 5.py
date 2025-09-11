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
