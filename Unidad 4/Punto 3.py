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
