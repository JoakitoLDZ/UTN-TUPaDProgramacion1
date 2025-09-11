#Punto 2
numero = int(input("Ingrese un numero entero: "))
n = abs(numero) # ABS sirve para tener el valor absoluto, lo convierte en positivo

if n == 0:
    cantidad_digitos = 1
else:
    cantidad_digitos = 0
    while n > 0:
        n //= 10
        cantidad_digitos += 1

print("El numero tiene", cantidad_digitos, "digitos.")
