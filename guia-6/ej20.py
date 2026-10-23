#M(AC) = M(AB) * M(BC)
def obtener_matriz_canal_compuesto(matriz_canal_1, matriz_canal_2):
    cantidad_entradas = len(matriz_canal_1)
    cantidad_intermedios = len(matriz_canal_1[0])
    cantidad_salidas = len(matriz_canal_2[0])
    if cantidad_intermedios != len(matriz_canal_2):
        raise ValueError("Las salidas del primer canal deben coincidir con las entradas del segundo")
    matriz_compuesta = [[0 for k in range(cantidad_salidas)] for i in range(cantidad_entradas)]
    for i in range(cantidad_entradas):
        for k in range(cantidad_salidas):
            for j in range(cantidad_intermedios):
                matriz_compuesta[i][k] += (matriz_canal_1[i][j] * matriz_canal_2[j][k])
    return matriz_compuesta