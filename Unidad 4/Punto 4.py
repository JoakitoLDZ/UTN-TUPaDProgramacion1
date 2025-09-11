# Punto 4
suma = 0   # acumulador

while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print("La suma total es:", suma)
