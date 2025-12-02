#Ejercicio 5
estudiantes = ["Ana", "Luis", "Pedro", "Juan", "Lucía", "Marta", "Diego", "Sofía"]

accion = input("¿Desea agregar (A) o eliminar (E) un estudiante?: ").upper()

if accion == "A":
    nuevo = input("Nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)

elif accion == "E":
    borrar = input("Nombre del estudiante a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
    else:
        print("No existe en la lista.")

print("Lista actualizada:", estudiantes)
