#Punto 6
alumnos = {}
for i in range(3):
    nombre = input("Nombre del alumno: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    alumnos[nombre] = (n1, n2, n3)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(nombre, promedio)
