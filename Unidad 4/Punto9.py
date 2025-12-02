#Punto 9
CANTIDAD = 100   # Cambiar para probar

suma = 0

for i in range(CANTIDAD):
    n = int(input(f"Ingrese el número {i+1}: "))
    suma += n

media = suma / CANTIDAD

print("\nLa media es:", media)
