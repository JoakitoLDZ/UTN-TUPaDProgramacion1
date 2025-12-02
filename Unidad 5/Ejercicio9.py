#ejercicio 9
tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar():
    for fila in tablero:
        print(fila)

turno = "X"

for _ in range(9):
    print(f"\nTurno de {turno}")
    f = int(input("Fila (0-2): "))
    c = int(input("Columna (0-2): "))

    if tablero[f][c] == "-":
        tablero[f][c] = turno
        mostrar()
        turno = "O" if turno == "X" else "X"
    else:
        print("Casilla ocupada. Intente de nuevo.")
