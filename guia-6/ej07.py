def obtener_probabilidades_salida(probabilidades_a_priori, matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    probabilidades_salida = [0 for j in range(cantidad_salidas)]
    for j in range(cantidad_salidas):
        for i in range(cantidad_entradas):
            probabilidades_salida[j] += (probabilidades_a_priori[i] * matriz_canal[i][j])
    return probabilidades_salida

def obtener_probabilidades_a_posteriori(probabilidades_a_priori, matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    probabilidades_salida = obtener_probabilidades_salida(probabilidades_a_priori, matriz_canal)
    matriz_posteriori = [[0 for columna in range(cantidad_salidas)] for fila in range(cantidad_entradas)]
    for i in range(cantidad_entradas):
        for j in range(cantidad_salidas):
            if probabilidades_salida[j] > 0:
                matriz_posteriori[i][j] = matriz_canal[i][j] * probabilidades_a_priori[i] / probabilidades_salida[j]
    return matriz_posteriori

def obtener_matriz_simultaneos(probabilidades_a_priori, matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    matriz_simultaneos = [[0 for columna in range(cantidad_salidas)] for fila in range(cantidad_entradas)]
    for i in range(cantidad_entradas):
        for j in range(cantidad_salidas):
            matriz_simultaneos[i][j] = probabilidades_a_priori[i] * matriz_canal[i][j] 
    return matriz_simultaneos