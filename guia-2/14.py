import math

def entropia(probabilidades):
    h = 0
    for p in probabilidades:
        if p > 0:
            h += p * math.log2(1 / p)
    return h

def vector_estacionario(matriz):
    n = len(matriz)
    # Arrancamos suponiendo todos los estados equiprobables
    vector = [1 / n for i in range(n)]
    for _ in range(10000):
        # Acá guardaremos M * vector
        nuevo_vector = [0 for i in range(n)]
        # Multiplicación matriz por vector
        for fila in range(n):
            for columna in range(n):
                nuevo_vector[fila] += (
                    matriz[fila][columna]
                    * vector[columna]
                )
        # Buscamos cuánto cambió el vector
        diferencia = max(
            abs(nuevo_vector[i] - vector[i])
            for i in range(n)
        )
        # Si prácticamente no cambia, llegamos al estacionario
        if diferencia < 0.000001:
            return nuevo_vector
        # Seguimos iterando
        vector = nuevo_vector
    return vector

def entropia_markov(matriz):
    # Primero calculamos la distribución estacionaria
    vector = vector_estacionario(matriz)
    n = len(matriz)
    h_total = 0
    # Cada columna representa las transiciones
    # posibles desde un estado
    for columna in range(n):
        probabilidades = []
        # Construimos la distribución de probabilidades
        # correspondiente a ese estado
        for fila in range(n):
            probabilidades.append(
                matriz[fila][columna]
            )
        # Entropía estando en ese estado
        h_estado = entropia(probabilidades)
        # La ponderamos por la probabilidad estacionaria
        # de encontrarnos en dicho estado
        h_total += vector[columna] * h_estado
    return h_total

matriz = [
    [1/2, 1/3, 0],
    [1/2, 1/3, 1],
    [0,   1/3, 0]
]

print("Vector estacionario:")
print(vector_estacionario(matriz))

print("Entropía:")
print(entropia_markov(matriz))