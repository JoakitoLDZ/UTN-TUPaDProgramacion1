#Punto 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18 and edad >= 12:
    print("Adolescente")
elif edad < 30 and edad >= 12 :
    print("Adulto/a joven")
else:
    print("Adulto/a")
