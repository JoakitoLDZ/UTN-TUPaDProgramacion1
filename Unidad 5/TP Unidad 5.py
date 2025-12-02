# Ejercicio 1
notas = [7, 5, 9, 10, 4, 6, 8, 7, 9, 3]

print("Lista completa:", notas)

promedio = sum(notas) / len(notas)
print("Promedio:", promedio)

print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

#Ejercicio 2
productos = []

for i in range(5):
    prod = input(f"Ingrese producto {i+1}: ")
    productos.append(prod)

print("Lista ordenada:", sorted(productos))

a_eliminar = input("¿Qué producto desea eliminar?: ")

if a_eliminar in productos:
    productos.remove(a_eliminar)
else:
    print("El producto no está en la lista.")

print("Lista actualizada:", productos)

#Ejercicio 3
import random

numeros = [random.randint(1, 100) for _ in range(15)]

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("Pares:", pares, "Cantidad:", len(pares))
print("Impares:", impares, "Cantidad:", len(impares))

#Ejercicio 4
datos = [1,3,5,3,7,1,9,5,3]

sin_repetidos = list(set(datos))

print("Lista sin repetidos:", sin_repetidos)

#Ejercicio 5
estudiantes = ["Ana", "Luis", "Pedro", "Juan", "Lucía", "Marta", "Diego", "Sofía"]

accion = input("¿Desea agregar (A) o eliminar (E) un estudiante?: ").upper()

if accion == "A":
    nuevo = input("Nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)

elif accion == "E":
    borrar = input("Nombre del estudiante a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
    else:
        print("No existe en la lista.")

print("Lista actualizada:", estudiantes)

#Ejercicio 6
lista = [10, 20, 30, 40, 50, 60, 70]

ultimo = lista.pop()
lista.insert(0, ultimo)

print("Lista rotada:", lista)

#Ejercicio 7
# [min, max]
temps = [
    [12, 25],
    [10, 22],
    [14, 28],
    [9, 20],
    [13, 27],
    [11, 24],
    [15, 30]
]

prom_min = sum(fila[0] for fila in temps) / 7
prom_max = sum(fila[1] for fila in temps) / 7

print("Promedio mínimas:", prom_min)
print("Promedio máximas:", prom_max)

amplitudes = [fila[1] - fila[0] for fila in temps]
dia_max_amp = amplitudes.index(max(amplitudes))

print("Mayor amplitud térmica en el día:", dia_max_amp + 1)

#Ejercicio 8
notas = [
    [7, 8, 9],
    [5, 6, 7],
    [9, 9, 10],
    [4, 5, 6],
    [8, 7, 9]
]

# Promedio por estudiante
for i in range(5):
    prom = sum(notas[i]) / 3
    print(f"Promedio del estudiante {i+1}:", prom)

# Promedio por materia
for m in range(3):
    prom = sum(notas[e][m] for e in range(5)) / 5
    print(f"Promedio de materia {m+1}:", prom)

#ejercicio 9
tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar():
    for fila in tablero:
        print(fila)

turno = "X"

for _ in range(9):
    print(f"\nTurno de {turno}")
    f = int(input("Fila (0-2): "))
    c = int(input("Columna (0-2): "))

    if tablero[f][c] == "-":
        tablero[f][c] = turno
        mostrar()
        turno = "O" if turno == "X" else "X"
    else:
        print("Casilla ocupada. Intente de nuevo.")

#ejercicio 10
ventas = [
    [10, 12, 11, 14, 9, 8, 13],
    [5, 6, 7, 5, 4, 6, 7],
    [20, 18, 22, 19, 21, 23, 20],
    [7, 9, 8, 6, 7, 8, 10]
]

# Total por producto
for p in range(4):
    total = sum(ventas[p])
    print(f"Producto {p+1} total vendido:", total)

# Día con mayores ventas
ventas_por_dia = [sum(ventas[p][d] for p in range(4)) for d in range(7)]
dia_max = ventas_por_dia.index(max(ventas_por_dia))
print("Día con mayores ventas:", dia_max + 1)

# Producto más vendido en la semana
totales = [sum(prod) for prod in ventas]
prod_max = totales.index(max(totales))
print("Producto más vendido:", prod_max + 1)
