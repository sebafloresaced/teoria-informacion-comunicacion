# Para importar este archivo desde la guia:
# import sys
# from pathlib import Path
# carpeta_funciones = (Path(__file__).resolve().parent.parent / "segundo-parcial")
# sys.path.insert(0, str(carpeta_funciones))
# import funciones

import math

def mostrar_matriz(matriz):
    for fila in matriz:
        print("  ".join(f"{valor:.3f}" for valor in fila))

def obtener_probabilidades_a_priori(entrada):
    alfabeto = []
    for simbolo in entrada:
        if simbolo not in alfabeto:
            alfabeto.append(simbolo)
    probabilidades = [
        entrada.count(simbolo) / len(entrada)
        for simbolo in alfabeto
    ]
    return alfabeto, probabilidades

# Las filas son las entradas y las columnas las salidas
def obtener_matriz_canal(entrada, salida):
    if len(entrada) != len(salida):
        raise ValueError("La entrada y la salida deben tener igual longitud")
    alfabeto_entrada, _ = obtener_probabilidades_a_priori(entrada)
    alfabeto_salida = []
    for simbolo in salida:
        if simbolo not in alfabeto_salida:
            alfabeto_salida.append(simbolo)
    matriz = [
        [0 for columna in alfabeto_salida]
        for fila in alfabeto_entrada
    ]
    # Cuento los pares entrada-salida
    for i in range(len(entrada)):
        fila = alfabeto_entrada.index(entrada[i])
        columna = alfabeto_salida.index(salida[i])
        matriz[fila][columna] += 1
    # Divido cada fila por la cantidad de su símbolo de entrada
    for fila in range(len(alfabeto_entrada)):
        cantidad = entrada.count(alfabeto_entrada[fila])
        for columna in range(len(alfabeto_salida)):
            matriz[fila][columna] /= cantidad
    return alfabeto_entrada, alfabeto_salida, matriz

def obtener_probabilidades_salida(probabilidades_a_priori, matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    probabilidades_salida = [0 for j in range(cantidad_salidas)]
    for j in range(cantidad_salidas):
        for i in range(cantidad_entradas):
            probabilidades_salida[j] += (probabilidades_a_priori[i] * matriz_canal[i][j])
    return probabilidades_salida

def obtener_matriz_a_posteriori(probabilidades_a_priori, matriz_canal):
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
            matriz_simultaneos[i][j] = matriz_canal[i][j] * probabilidades_a_priori[i]
    return matriz_simultaneos

def obtener_entropia_a_priori(probabilidades_a_priori):
    entropia = 0
    for p in probabilidades_a_priori:
        if (p > 0):
            entropia += p * math.log(1 / p, 2)
    return entropia

def obtener_entropias_a_posteriori(probabilidades_a_priori, matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    entropias_a_posteriori = [0 for j in range(cantidad_salidas)]
    matriz_a_posteriori = obtener_matriz_a_posteriori(probabilidades_a_priori, matriz_canal)
    for j in range(cantidad_salidas):
        for i in range(cantidad_entradas):
            if (matriz_a_posteriori[i][j] > 0): 
                entropias_a_posteriori[j] += matriz_a_posteriori[i][j] * math.log(1 / matriz_a_posteriori[i][j], 2)
    return entropias_a_posteriori

# H(A/B) = ruido
def obtener_ruido(probabilidades_a_priori, matriz_canal):
    cantidad_salidas = len(matriz_canal[0])
    probabilidades_salida = obtener_probabilidades_salida(probabilidades_a_priori, matriz_canal)
    entropias_a_posteriori = obtener_entropias_a_posteriori(probabilidades_a_priori, matriz_canal)
    ruido = 0
    for j in range(cantidad_salidas):
        ruido += probabilidades_salida[j] * entropias_a_posteriori[j]
    return ruido

# H(B/A) = perdida
def obtener_perdida(probabilidades_a_priori, matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    perdida = 0
    for i in range(cantidad_entradas):
        entropia_fila = 0
        for j in range(cantidad_salidas):
            p = matriz_canal[i][j]
            if p > 0:
                entropia_fila += p * math.log2(1 / p)
        perdida += probabilidades_a_priori[i] * entropia_fila
    return perdida

# I(A,B) = H(A) - H(A/B)
def obtener_informacion_mutua(probabilidades_a_priori, matriz_canal):
    return obtener_entropia_a_priori(probabilidades_a_priori) - obtener_ruido(probabilidades_a_priori, matriz_canal)

# H(A,B) = H(A) + H(B/A)
def obtener_entropia_afin(probabilidades_a_priori, matriz_canal):
    return obtener_entropia_a_priori(probabilidades_a_priori) + obtener_perdida(probabilidades_a_priori, matriz_canal)

def verifica_sin_ruido(matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    for j in range(cantidad_salidas):
        elem_no_cero = False
        for i in range(cantidad_entradas):
            if (matriz_canal[i][j] > 0):
                if (elem_no_cero == False):
                    elem_no_cero = True
                else:
                    return False
    return True

def verifica_determinante(matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    for i in range(cantidad_entradas):
        elem_no_cero = False
        for j in range(cantidad_salidas):
            if (matriz_canal[i][j] > 0):
                if (elem_no_cero == False):
                    elem_no_cero = True
                else:
                    return False
    return True

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

def obtener_canal_reducido(matriz_canal):
    # Copiamos la matriz para no modificar la original.
    matriz_reducida = [fila[:] for fila in matriz_canal]
    hubo_reduccion = True
    while hubo_reduccion:
        hubo_reduccion = False
        cantidad_columnas = len(matriz_reducida[0])
        for columna_1 in range(cantidad_columnas):
            for columna_2 in range(columna_1 + 1, cantidad_columnas):
                if verificar_reduccion_suficiente(matriz_reducida, columna_1, columna_2):
                    matriz_determinista = obtener_canal_determinista(matriz_reducida, columna_1, columna_2)
                    matriz_reducida = obtener_matriz_canal_compuesto(matriz_reducida, matriz_determinista)
                    hubo_reduccion = True
                    break
            if hubo_reduccion:
                break
    return matriz_reducida

def verifica_uniforme(matriz_canal):
    primera_fila = sorted(matriz_canal[0])
    for fila in matriz_canal[1:]:
        fila_ordenada = sorted(fila)
        for j in range(len(primera_fila)):
            if not math.isclose(primera_fila[j], fila_ordenada[j], abs_tol=1e-10):
                return False
    return True

def obtener_capacidad(probabilidades_a_priori, matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    if (verifica_sin_ruido(matriz_canal)):
        return math.log(cantidad_entradas, 2)
    elif (verifica_determinante(matriz_canal)):
        return math.log(cantidad_salidas, 2)
    elif verifica_uniforme(matriz_canal):
        return math.log(len(matriz_canal[0]), 2) - obtener_entropia_a_priori(matriz_canal[0])
    else:
        # calculo maximo aproximado
        return 0

# el paso representa cuando aumento la probabilidad en cada iteracion
def estimar_capacidad_canal_binario(matriz_canal, paso = 0.0001):
    if len(matriz_canal) != 2:
        raise ValueError("El canal debe tener dos entradas")
    if not (0 < paso <= 1):
        raise ValueError("El paso debe estar entre 0 y 1")
    capacidad = -1
    mejor_probabilidad = 0
    i = 0
    while True:
        # Incluimos p = 1 aunque el paso no divida exactamente a 1.
        p = min(i * paso, 1.0)
        probabilidades = [p, 1 - p]
        informacion_mutua = obtener_informacion_mutua(probabilidades, matriz_canal)
        if informacion_mutua > capacidad:
            capacidad = informacion_mutua
            mejor_probabilidad = p
        if p == 1:
            break
        i += 1
    return capacidad, mejor_probabilidad

def obtener_probabilidad_error(probabilidades_a_priori, matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    probabilidad_acierto = 0
    for j in range(cantidad_salidas):
        mayor_probabilidad_conjunta = 0
        for i in range(cantidad_entradas):
            probabilidad_conjunta = (probabilidades_a_priori[i] * matriz_canal[i][j])
            if probabilidad_conjunta > mayor_probabilidad_conjunta:
                mayor_probabilidad_conjunta = probabilidad_conjunta
        probabilidad_acierto += mayor_probabilidad_conjunta
    return 1 - probabilidad_acierto