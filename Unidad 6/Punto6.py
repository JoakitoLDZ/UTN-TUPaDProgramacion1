#Punto 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
num = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num)
