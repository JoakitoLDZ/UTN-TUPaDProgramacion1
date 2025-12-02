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
