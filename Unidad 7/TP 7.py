#Punto 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

#Punto 2
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

#Punto 3
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

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

#Punto 5
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
print(palabras_unicas)
print(recuento)

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

#Punto 7
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}
print(parcial1 & parcial2)
print(parcial1 ^ parcial2)
print(parcial1 | parcial2)

#Punto 8
stock = {"pan": 10, "leche": 20, "huevos": 12}
producto = input("Producto a consultar: ")
if producto in stock:
    print(stock[producto])
    agregar = int(input("Unidades a agregar: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Ingrese stock para agregarlo: "))
    stock[producto] = nuevo_stock
print(stock)

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

#Punto 10
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais
print(invertido)
