from itertools import product

# Desarrollar una función en Python que reciba: una lista con el alfabeto de una fuente, otra con su distribución de probabilidades 
# y un número entero N. Esta función debe generar dos nuevas listas con la extensión de orden N y su distribución de probabilidades
def extension_fuente(alfabeto, probabilidades, n):
    alfabeto_extendido = []
    probabilidades_extendidas = []
    combinaciones = product(range(len(alfabeto)), repeat=n)
    for combinacion in combinaciones:
        simbolo = ""
        probabilidad = 1
        for i in combinacion:
            simbolo += alfabeto[i]
            probabilidad *= probabilidades[i]
        alfabeto_extendido.append(simbolo)
        probabilidades_extendidas.append(probabilidad)
    return alfabeto_extendido, probabilidades_extendidas