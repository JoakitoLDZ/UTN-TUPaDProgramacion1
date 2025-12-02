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
