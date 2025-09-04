#Punto 8
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese 1, 2 o 3 según la opción deseada: ")
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
