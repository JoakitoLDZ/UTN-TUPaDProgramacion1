#Punto 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal
c = float(input("Ingrese la temperatura en Celsius: "))
print("Equivalente en Fahrenheit:", celsius_a_fahrenheit(c))
