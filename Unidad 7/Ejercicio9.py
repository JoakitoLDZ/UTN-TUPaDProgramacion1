#Punto 9
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}
dia = input("Día: ")
hora = input("Hora: ")
clave = (dia, hora)
if clave in agenda:
    print(agenda[clave])
else:
    print("No hay actividades en ese horario.")
