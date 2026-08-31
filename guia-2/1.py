import math

P = [0.5, 0.2, 0.3]

# generar una lista con la cantidad de información en bits de cada símbolo (utilizar comprensión de listas).
def informacion(P):
    I = [math.log2(1 / p) for p in P]
    return I

# obtener la entropía de la fuente (utilizar la función anterior).
def entropia(P):
    I = informacion(P)
    H = 0
    for i in range(len(P)):
        H += P[i] * I[i]
    return H