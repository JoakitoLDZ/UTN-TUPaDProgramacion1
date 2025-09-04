#Punto 7
num1=int(input("Ingrese el primer numero (distinto que 0): "))
num2=int(input("Ingrese el segundo numero (distinto que 0): "))

if num1 == 0 or num2 == 0:
    print("Error los números deben ser distintos de 0.")
else:
    suma=num1+num2
    resta=num1-num2
    multi=num1*num2
    div=num1/num2

print(f"Segun los numeros ingresados, el resultado de su suma es igual a {suma}, su resta es igual a {resta}, si los multiplicamos obtendremos el resultado {multi} y si los dividimos tendremos como resultado {div}.")
