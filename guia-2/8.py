import math

# Realizar una función en Python que reciba como parámetro el valor ω de una fuente binaria de memoria nula y, 
# utilizando las funciones desarrolladas en el ejercicio 1, calcule la entropía de la fuente.

def informacion(probabilidades):
    info = [
        math.log2(1 / p) if p > 0 else 0
        for p in probabilidades
    ]
    return info


def entropia(probabilidades):
    info = informacion(probabilidades)
    h = 0
    for i in range(len(probabilidades)):
        h += probabilidades[i] * info[i]
    return h

def entropia_binaria(w):
    probabilidades = [w, 1 - w]
    return entropia(probabilidades)