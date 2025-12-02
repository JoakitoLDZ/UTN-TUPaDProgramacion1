#punto 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

# Programa principal
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

suma, resta, multi, div = operaciones_basicas(a, b)

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multi)
print("División:", div)
