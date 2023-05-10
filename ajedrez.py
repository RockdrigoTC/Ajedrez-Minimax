# Juego de ajedrez por consola
import os
import copy

# Piezas de ajedrez
REY_N = "♔"
REY_B = "♚"
REINA_N = "♕"
REINA_B = "♛"
TORRE_N = "♖"
TORRE_B = "♜"
ALFIL_N = "♗"
ALFIL_B = "♝"
CABALLO_N = "♘"
CABALLO_B = "♞"
PEON_N = "♙"
PEON_B = "♟"
CASILLA_N = "□"
CASILLA_B = "■"
PIEZAS_N = [REY_N, REINA_N, TORRE_N, ALFIL_N, CABALLO_N, PEON_N]
PIEZAS_B = [REY_B, REINA_B, TORRE_B, ALFIL_B, CABALLO_B, PEON_B]


# Tablero de ajedrez
tablero_partida = [
    [" ", "A", "B", "C", "D", "E", "F", "G", "H"],
    ["1", "♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
    ["2", "♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
    ["3", "□", "■", "□", "■", "□", "■", "□", "■"],
    ["4", "■", "□", "■", "□", "■", "□", "■", "□"],
    ["5", "□", "■", "□", "■", "□", "■", "□", "■"],
    ["6", "■", "□", "■", "□", "■", "□", "■", "□"],
    ["7", "♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
    ["8", "♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],
]

# tablero_partida = [
#     [" ", "A", "B", "C", "D", "E", "F", "G", "H"],
#     ["1", "■", "□", "♚", "♛", "■", "□", "■", "♖"],
#     ["2", "□", "♟", "♟", "■", "□", "■", "♙", "■"],
#     ["3", "♙", "□", "■", "□", "■", "♙", "■", "□"],
#     ["4", "□", "■", "♘", "■", "□", "■", "□", "■"],
#     ["5", "■", "□", "■", "♖", "■", "♙", "■", "□"],
#     ["6", "□", "■", "□", "■", "□", "♔", "□", "■"],
#     ["7", "■", "□", "■", "□", "■", "□", "■", "□"],
#     ["8", "□", "■", "□", "■", "□", "■", "□", "■"],
# ]


def imprimir_tablero(tablero):
    print()
    for fila in reversed(tablero):
        for casilla in fila:
            print(casilla, end=" ")
        print()
    print()


def traducir_cordenadas(cordenada):
    if type(cordenada) == str:
        if cordenada == "A" or cordenada == "a":
            return 1
        if cordenada == "B" or cordenada == "b":
            return 2
        if cordenada == "C" or cordenada == "c":
            return 3
        if cordenada == "D" or cordenada == "d":
            return 4
        if cordenada == "E" or cordenada == "e":
            return 5
        if cordenada == "F" or cordenada == "f":
            return 6
        if cordenada == "G" or cordenada == "g":
            return 7
        if cordenada == "H" or cordenada == "h":
            return 8
    else:
        if cordenada == 1:
            return "A"
        if cordenada == 2:
            return "B"
        if cordenada == 3:
            return "C"
        if cordenada == 4:
            return "D"
        if cordenada == 5:
            return "E"
        if cordenada == 6:
            return "F"
        if cordenada == 7:
            return "G"
        if cordenada == 8:
            return "H"


def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def cambiar_turno(turno):
    if turno == "Blancas":
        return "Negras"
    else:
        return "Blancas"


def verificar_turno(tablero, f_origen, c_origen):
    if turno == "Blancas":
        if tablero[f_origen][c_origen] in PIEZAS_B:
            return True
        return False
    if turno == "Negras":
        if tablero[f_origen][c_origen] in PIEZAS_N:
            return True
        return False
    return False


def verificar_movimiento(tablero, f_origen, c_origen, f_destino, c_destino):
    if f_origen == f_destino and c_origen == c_destino:
        return False

    if f_origen < 1 or f_origen > 8 or f_destino < 1 or f_destino > 8:
        return False

    if c_origen < 1 or c_origen > 8 or c_destino < 1 or c_destino > 8:
        return False

    if tablero[f_origen][c_origen] == "□" or tablero[f_origen][c_origen] == "■":
        return False

    if tablero[f_origen][c_origen] in PIEZAS_B:
        if tablero[f_destino][c_destino] in PIEZAS_B:
            return False

    if tablero[f_origen][c_origen] in PIEZAS_N:
        if tablero[f_destino][c_destino] in PIEZAS_N:
            return False

    if tablero[f_origen][c_origen] == "♟":
        if c_origen == c_destino:
            if f_origen == 2:
                if f_destino == 3 or f_destino == 4:
                    if f_destino == 4:
                        if (
                            tablero[f_destino - 1][c_destino] != "□"
                            and tablero[f_destino - 1][c_destino] != "■"
                        ):
                            return False
                    if (
                        tablero[f_destino][c_destino] == "□"
                        or tablero[f_destino][c_destino] == "■"
                    ):
                        return True
            if f_destino == f_origen + 1:
                if (
                    tablero[f_destino][c_destino] == "□"
                    or tablero[f_destino][c_destino] == "■"
                ):
                    return True

        if c_destino == c_origen + 1 or c_destino == c_origen - 1:
            if f_destino == f_origen + 1:
                if (
                    tablero[f_destino][c_destino] != "□"
                    and tablero[f_destino][c_destino] != "■"
                ):
                    return True
            return False
        return False

    if tablero[f_origen][c_origen] == "♙":
        if c_origen == c_destino:
            if f_origen == 7:
                if f_destino == 6 or f_destino == 5:
                    if f_destino == 5:
                        if (
                            tablero[f_destino + 1][c_destino] != "□"
                            and tablero[f_destino + 1][c_destino] != "■"
                        ):
                            return False
                    if (
                        tablero[f_destino][c_destino] == "□"
                        or tablero[f_destino][c_destino] == "■"
                    ):
                        return True
            if f_destino == f_origen - 1:
                if (
                    tablero[f_destino][c_destino] == "□"
                    or tablero[f_destino][c_destino] == "■"
                ):
                    return True

        if c_destino == c_origen + 1 or c_destino == c_origen - 1:
            if f_destino == f_origen - 1:
                if (
                    tablero[f_destino][c_destino] != "□"
                    and tablero[f_destino][c_destino] != "■"
                ):
                    return True
            return False
        return False

    if tablero[f_origen][c_origen] == "♜" or tablero[f_origen][c_origen] == "♖":
        if f_origen == f_destino or c_origen == c_destino:
            if f_origen == f_destino:
                for j in range(min(c_origen, c_destino) + 1, max(c_origen, c_destino)):
                    if tablero[f_origen][j] != "□" and tablero[f_origen][j] != "■":
                        return False
            else:
                for i in range(min(f_origen, f_destino) + 1, max(f_origen, f_destino)):
                    if tablero[i][c_origen] != "□" and tablero[i][c_origen] != "■":
                        return False
            return True
        return False

    if tablero[f_origen][c_origen] == "♞" or tablero[f_origen][c_origen] == "♘":
        if f_destino == f_origen + 2 or f_destino == f_origen - 2:
            if c_destino == c_origen + 1 or c_destino == c_origen - 1:
                return True
        if c_destino == c_origen + 2 or c_destino == c_origen - 2:
            if f_destino == f_origen + 1 or f_destino == f_origen - 1:
                return True
        return False

    if tablero[f_origen][c_origen] == "♝" or tablero[f_origen][c_origen] == "♗":
        if abs(f_destino - f_origen) == abs(c_destino - c_origen):
            fila_inicial, fila_final = sorted([f_origen, f_destino])
            col_inicial, col_final = sorted([c_origen, c_destino])
            if f_destino - f_origen == c_destino - c_origen:
                for fila, columna in zip(
                    range(fila_inicial + 1, fila_final),
                    range(col_inicial + 1, col_final),
                ):
                    if tablero[fila][columna] != "□" and tablero[fila][columna] != "■":
                        return False
            else:
                for fila, columna in zip(
                    range(fila_inicial + 1, fila_final),
                    range(col_final - 1, col_inicial, -1),
                ):
                    if tablero[fila][columna] != "□" and tablero[fila][columna] != "■":
                        return False
            return True
        return False

    if tablero[f_origen][c_origen] == "♛" or tablero[f_origen][c_origen] == "♕":
        if f_origen == f_destino or c_origen == c_destino:
            if f_origen == f_destino:
                for j in range(min(c_origen, c_destino) + 1, max(c_origen, c_destino)):
                    if tablero[f_origen][j] != "□" and tablero[f_origen][j] != "■":
                        return False
            else:
                for i in range(min(f_origen, f_destino) + 1, max(f_origen, f_destino)):
                    if tablero[i][c_origen] != "□" and tablero[i][c_origen] != "■":
                        return False
            return True

        if abs(f_destino - f_origen) == abs(c_destino - c_origen):
            fila_inicial, fila_final = sorted([f_origen, f_destino])
            col_inicial, col_final = sorted([c_origen, c_destino])
            if f_destino - f_origen == c_destino - c_origen:
                for fila, columna in zip(
                    range(fila_inicial + 1, fila_final),
                    range(col_inicial + 1, col_final),
                ):
                    if tablero[fila][columna] != "□" and tablero[fila][columna] != "■":
                        return False
            else:
                for fila, columna in zip(
                    range(fila_inicial + 1, fila_final),
                    range(col_final - 1, col_inicial, -1),
                ):
                    if tablero[fila][columna] != "□" and tablero[fila][columna] != "■":
                        return False
            return True
        return False

    if tablero[f_origen][c_origen] == "♚" or tablero[f_origen][c_origen] == "♔":
        if f_destino == f_origen + 1 or f_destino == f_origen - 1:
            if c_destino == c_origen + 1 or c_destino == c_origen - 1:
                return True
        if f_destino == f_origen:
            if c_destino == c_origen + 1 or c_destino == c_origen - 1:
                return True
        if c_destino == c_origen:
            if f_destino == f_origen + 1 or f_destino == f_origen - 1:
                return True
        return False

    return False


def mover_pieza(tablero, f_origen, c_origen, f_destino, c_destino):
    if verificar_movimiento(tablero, f_origen, c_origen, f_destino, c_destino):
        tablero[f_destino][c_destino] = tablero[f_origen][c_origen]
        if f_origen % 2 != 0:
            if c_origen % 2 != 0:
                tablero[f_origen][c_origen] = "□"
            else:
                tablero[f_origen][c_origen] = "■"
        else:
            if c_origen % 2 != 0:
                tablero[f_origen][c_origen] = "■"
            else:
                tablero[f_origen][c_origen] = "□"
        return True
    return False


def posicion_pieza(tablero, pieza):
    for i in range(1, 9):
        for j in range(1, 9):
            if tablero[i][j] == pieza:
                return (i, j)
    return None


def probar_movimiento(tablero, f_origen, c_origen, f_destino, c_destino):
    tablero_copia = copy.deepcopy(tablero)
    tablero_copia[f_destino][c_destino] = tablero_copia[f_origen][c_origen]
    if f_origen % 2 != 0:
        if c_origen % 2 != 0:
            tablero_copia[f_origen][c_origen] = "□"
        else:
            tablero_copia[f_origen][c_origen] = "■"
    else:
        if c_origen % 2 != 0:
            tablero_copia[f_origen][c_origen] = "■"
        else:
            tablero_copia[f_origen][c_origen] = "□"
    return copy.deepcopy(tablero_copia)


def movimientos_posibles(tablero, f_origen, c_origen):
    movimientos = []
    for i in range(1, 9):
        for j in range(1, 9):
            if verificar_movimiento(tablero, f_origen, c_origen, i, j):
                movimientos.append((i, j))
    return movimientos


def verificar_ahogado(tablero, turno):
    if turno == "Blancas":
        piezas_color = PIEZAS_B
    elif turno == "Negras":
        piezas_color = PIEZAS_N

    for i in range(1, 9):
        for j in range(1, 9):
            if tablero[i][j] in piezas_color:
                movimientos = movimientos_posibles(tablero, i, j)
                for movimiento in movimientos:
                    tablero_copia = probar_movimiento(
                        tablero, i, j, movimiento[0], movimiento[1]
                    )
                    if not verificar_jaque(tablero_copia, turno):
                        return False
    return True


def verificar_jaque(tablero, turno):
    if turno == "Blancas":
        rey = REY_B
        piezas_color = PIEZAS_N
    elif turno == "Negras":
        rey = REY_N
        piezas_color = PIEZAS_B

    f_rey, c_rey = posicion_pieza(tablero, rey)
    for i in range(1, 9):
        for j in range(1, 9):
            if tablero[i][j] in piezas_color:
                if verificar_movimiento(tablero, i, j, f_rey, c_rey):
                    # print(
                    #     f"Pieza en [{traducir_cordenadas(j)}][{i}] amenaza al rey en [{traducir_cordenadas(c_rey)}][{f_rey}]"
                    # )
                    return True
                # print(
                #     f"Pieza en [{traducir_cordenadas(j)}][{i}] no amenaza al rey en [{traducir_cordenadas(c_rey)}][{f_rey}]"
                # )
    return False


def verificar_jaque_mate(tablero, turno):
    if turno == "Blancas":
        piezas_color = PIEZAS_B
    elif turno == "Negras":
        piezas_color = PIEZAS_N

    if verificar_jaque(tablero, turno):
        no_jaque_mate = False
        for i in range(1, 9):
            for j in range(1, 9):
                if tablero[i][j] in piezas_color:
                    movimientos = movimientos_posibles(tablero, i, j)
                    for movimiento in movimientos:
                        tablero_copia = probar_movimiento(
                            tablero, i, j, movimiento[0], movimiento[1]
                        )
                        if not verificar_jaque(tablero_copia, turno):
                            print(
                                # f"Pieza en [{traducir_cordenadas(Sj)}][{i}] puede moverse a [{traducir_cordenadas(movimiento[1])}][{movimiento[0]}]"
                            )
                            no_jaque_mate = True
        return not no_jaque_mate
    return False


def evaluar_tablero(tablero, turno):
    if turno == "Blancas":
        piezas_jugador = PIEZAS_B
        piezas_oponente = PIEZAS_N
        rey_jugador = REY_B
        rey_oponente = REY_N
    elif turno == "Negras":
        piezas_jugador = PIEZAS_N
        piezas_oponente = PIEZAS_B
        rey_jugador = REY_N
        rey_oponente = REY_B

    puntaje_jugador = 0
    puntaje_oponente = 0

    if verificar_jaque_mate(copy.deepcopy(tablero), turno):
        return -1000, 1000

    for i in range(1, 9):
        for j in range(1, 9):
            if tablero[i][j] in piezas_jugador:
                puntaje_jugador += valor_pieza(tablero[i][j])
                puntaje_jugador += len(movimientos_posibles(tablero, i, j))
            elif tablero[i][j] in piezas_oponente:
                puntaje_oponente += valor_pieza(tablero[i][j])
                puntaje_oponente += len(movimientos_posibles(tablero, i, j))

    puntaje_jugador += cobertura_rey(tablero, piezas_jugador, rey_jugador)
    puntaje_oponente += cobertura_rey(tablero, piezas_oponente, rey_oponente)

    if verificar_jaque(tablero, turno):
        puntaje_jugador -= 100
        puntaje_oponente += 100

    return puntaje_jugador, puntaje_oponente


def valor_pieza(pieza):
    if pieza == "♟" or pieza == "♙":
        return 1
    if pieza == "♜" or pieza == "♖":
        return 5
    if pieza == "♞" or pieza == "♘":
        return 3
    if pieza == "♝" or pieza == "♗":
        return 3
    if pieza == "♛" or pieza == "♕":
        return 9
    if pieza == "♚" or pieza == "♔":
        return 100
    return 0


def cobertura_rey(tablero, piezas, rey):
    f_rey, c_rey = posicion_pieza(tablero, rey)
    cobertura = 0
    if f_rey == 1:
        cobertura += 1
    if f_rey == 8:
        cobertura += 1
    if c_rey == 1:
        cobertura += 1
    if c_rey == 8:
        cobertura += 1

    for i in range(1, 9):
        for j in range(1, 9):
            if tablero[i][j] in piezas:
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if verificar_movimiento(tablero, i, j, f_rey + k, c_rey + l):
                            cobertura += 1
    return cobertura


# loop principal
limpiar_pantalla()
turno = "Blancas"
while True:
    if verificar_jaque_mate(copy.deepcopy(tablero_partida), turno):
        print(f"Jaque mate a jugador {turno}")
        imprimir_tablero(tablero_partida)
        break

    if verificar_ahogado(copy.deepcopy(tablero_partida), turno):
        print(f"Jugador {turno} se ha quedado sin movimientos")
        imprimir_tablero(tablero_partida)
        break

    if verificar_jaque(tablero_partida, turno):
        print(f"Jaque a jugador {turno}")

    puntajes = evaluar_tablero(copy.deepcopy(tablero_partida), turno)
    print(f"Puntaje jugador: {puntajes[0]}")
    print(f"Puntaje oponente: {puntajes[1]}")

    print("Turno de las ", turno)
    imprimir_tablero(tablero_partida)
    print("Ingrese la posición de la pieza a mover")
    origen = input("Origen: ")
    print("Ingrese la posición de destino")
    destino = input("Destino: ")

    c_origen = traducir_cordenadas(origen[0])
    f_origen = int(origen[1])
    c_destino = traducir_cordenadas(destino[0])
    f_destino = int(destino[1])

    tablero2 = copy.deepcopy(tablero_partida)
    if (
        verificar_turno(tablero2, f_origen, c_origen)
        and mover_pieza(tablero2, f_origen, c_origen, f_destino, c_destino)
        and not verificar_jaque(tablero2, turno)
    ):
        limpiar_pantalla()
        print("Movimiento realizado con éxito")
        tablero_partida = copy.deepcopy(tablero2)
        turno = cambiar_turno(turno)
    else:
        limpiar_pantalla()
        print("Movimiento inválido")
