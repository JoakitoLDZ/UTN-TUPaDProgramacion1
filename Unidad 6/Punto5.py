#Punto 5
def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segundos = int(input("Ingrese la cantidad de segundos: "))
print("Equivalen a horas:", segundos_a_horas(segundos))
