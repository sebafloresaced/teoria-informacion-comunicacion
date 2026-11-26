import math

def obtener_entropia_a_priori(probabilidades_a_priori):
    entropia = 0
    for p in probabilidades_a_priori:
        if (p > 0):
            entropia += p * math.log(1 / p, 2)
    return entropia

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

def mostrar_matriz(matriz):
    for fila in matriz:
        print("  ".join(f"{valor:.3f}" for valor in fila))

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

matriz_canal_1 = [
  [0.3, 0, 0.7, 0], # entrada 0
  [0, 0.5, 0, 0.5] # entrada 1
]

matriz_canal_2 = [
  [0, 1], # entrada T
  [1, 0], # entrada U
  [0, 1], # entrada V
  [1, 0] # entrada W
]

print("\nCanal 1:")
# Obtener la distribución óptima de entrada.
capacidad, p_0 = estimar_capacidad_canal_binario(matriz_canal_1)
p_1 = 1 - p_0
probabilidades_a_priori_1 = [p_0, p_1]

print("Probabilidades a priori: ", probabilidades_a_priori_1)
print("Ruido del canal H(A/B): ", obtener_ruido(probabilidades_a_priori_1, matriz_canal_1))
print("Perdida del canal H(B/A): ", obtener_perdida(probabilidades_a_priori_1, matriz_canal_1))
print("Informacion mutua del canal I(A, B): ", obtener_informacion_mutua(probabilidades_a_priori_1, matriz_canal_1))
print("Probabilidad de error: ", obtener_probabilidad_error(probabilidades_a_priori_1, matriz_canal_1))
print("Determinante: ", verifica_determinante(matriz_canal_1))
print("Sin ruido: ", verifica_sin_ruido(matriz_canal_1))

print("\nCanal 2:")
# Entradas equiprobables
probabilidades_a_priori_2 = [1/4, 1/4, 1/4, 1/4]
print("Ruido del canal H(A/B): ", obtener_ruido(probabilidades_a_priori_2, matriz_canal_2))
print("Perdida del canal H(B/A): ", obtener_perdida(probabilidades_a_priori_2, matriz_canal_2))
print("Informacion mutua del canal I(A, B): ", obtener_informacion_mutua(probabilidades_a_priori_2, matriz_canal_2))
print("Probabilidad de error: ", obtener_probabilidad_error(probabilidades_a_priori_2, matriz_canal_2))
print("Determinante: ", verifica_determinante(matriz_canal_2))
print("Sin ruido: ", verifica_sin_ruido(matriz_canal_2))

print("\nCanal compuesto:")
canal_compuesto = obtener_matriz_canal_compuesto(matriz_canal_1, matriz_canal_2)
mostrar_matriz(canal_compuesto)
probabilidades_a_priori_compuesto = probabilidades_a_priori_1
print("Ruido del canal H(A/B): ", obtener_ruido(probabilidades_a_priori_compuesto, canal_compuesto))
print("Perdida del canal H(B/A): ", obtener_perdida(probabilidades_a_priori_compuesto, canal_compuesto))
print("Informacion mutua del canal I(A, B): ", obtener_informacion_mutua(probabilidades_a_priori_compuesto, canal_compuesto))
print("Probabilidad de error: ", obtener_probabilidad_error(probabilidades_a_priori_compuesto, canal_compuesto))
print("Determinante: ", verifica_determinante(canal_compuesto))
print("Sin ruido: ", verifica_sin_ruido(canal_compuesto))