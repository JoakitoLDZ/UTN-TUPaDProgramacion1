#Punto 10
num = int(input("Ingrese un número: "))
invertido = 0

while num > 0:
    dig = num % 10
    invertido = invertido * 10 + dig
    num //= 10

print("Número invertido:", invertido)
