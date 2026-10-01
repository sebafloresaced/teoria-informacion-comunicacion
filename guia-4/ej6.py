import math

def informacion(P, r=2):
    I = [math.log(1 / p, r) if p > 0 else 0 for p in P]
    return I

def calcular_entropia(P, r=2):
    I = informacion(P,r)
    H = 0
    for i in range(len(P)):
        H += P[i] * I[i]
    return H

def obtener_alfabeto_codigo(codigo):
    alfabeto = []
    for palabra in codigo:
        for caracter in palabra:
            if caracter not in alfabeto:
                alfabeto.append(caracter)
    return alfabeto
    
def obtener_longitudes(codigo):
    return [len(palabra) for palabra in codigo]

def calcular_longitud_media(codigo, probabilidades):
    suma = 0
    longitudes = obtener_longitudes(codigo)
    for i in range(len(longitudes)):
        suma += probabilidades[i] * longitudes[i]
    return suma

def rendimiento(probabilidades, codificacion, r = 2):
    return calcular_entropia(probabilidades, r) / calcular_longitud_media(codificacion, probabilidades)

def redundancia(probabilidades, codificacion, r = 2):
    return 1 - rendimiento(probabilidades, codificacion, r)