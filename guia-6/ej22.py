import math

def verificar_reduccion_suficiente(matriz_canal, columna_1, columna_2):
    cantidad_columnas = len(matriz_canal[0])
    if not (0 <= columna_1 < cantidad_columnas and 0 <= columna_2 < cantidad_columnas):
        raise ValueError("Índice de columna fuera de rango")
    if columna_1 == columna_2:
        raise ValueError("Se deben seleccionar dos columnas distintas")
    suma_1 = sum(fila[columna_1] for fila in matriz_canal)
    suma_2 = sum(fila[columna_2] for fila in matriz_canal)
    # Una columna nula representa una salida imposible.
    # Se puede agrupar con otra sin perder información.
    if suma_1 == 0 or suma_2 == 0:
        return True
    for fila in matriz_canal:
        valor_1 = fila[columna_1] / suma_1
        valor_2 = fila[columna_2] / suma_2
        if not math.isclose(valor_1, valor_2, abs_tol=1e-10):
            return False
    return True

def obtener_canal_determinista(matriz_canal, columna_1, columna_2):
    if not verificar_reduccion_suficiente(matriz_canal, columna_1, columna_2):
        raise ValueError("Las columnas no permiten una reducción suficiente")
    cantidad_salidas = len(matriz_canal[0])
    # Conservamos la posición de la primera y eliminamos la segunda.
    primera = min(columna_1, columna_2)
    segunda = max(columna_1, columna_2)
    matriz_determinista = [[0 for j in range(cantidad_salidas - 1)]for i in range(cantidad_salidas)]
    for i in range(cantidad_salidas):
        if i == segunda:
            destino = primera
        elif i > segunda:
            destino = i - 1
        else:
            destino = i
        matriz_determinista[i][destino] = 1
    return matriz_determinista