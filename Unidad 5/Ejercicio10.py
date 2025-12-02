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
