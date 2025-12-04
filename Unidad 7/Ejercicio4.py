#Punto 4
contactos = {}
for i in range(5):
    nombre = input("Nombre: ")
    numero = input("Número: ")
    contactos[nombre] = numero

consulta = input("¿A quién querés buscar?: ")
if consulta in contactos:
    print(contactos[consulta])
else:
    print("No existe ese contacto.")
