#Ejercicio 2
productos = []

for i in range(5):
    prod = input(f"Ingrese producto {i+1}: ")
    productos.append(prod)

print("Lista ordenada:", sorted(productos))

a_eliminar = input("¿Qué producto desea eliminar?: ")

if a_eliminar in productos:
    productos.remove(a_eliminar)
else:
    print("El producto no está en la lista.")

print("Lista actualizada:", productos)
