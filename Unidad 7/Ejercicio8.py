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
