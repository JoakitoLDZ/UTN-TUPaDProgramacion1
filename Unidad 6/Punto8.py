#Punto 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))

imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")
