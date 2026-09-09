import math

def obtener_alfabeto_codigo(codigo):
    alfabeto = []
    for palabra in codigo:
        for caracter in palabra:
            if caracter not in alfabeto:
                alfabeto.append(caracter)
    return alfabeto

def calcular_entropia(codigo, probabilidades):
    alfabeto = obtener_alfabeto_codigo(codigo)
    r = len(alfabeto)
    suma = 0
    for p in probabilidades:
        suma += p * math.log(1 / p, r)
    return suma

def obtener_longitudes(codigo):
    return [len(palabra) for palabra in codigo]

def calcular_longitud_media(codigo, probabilidades):
    suma = 0
    longitudes = obtener_longitudes(codigo)
    for i in range(len(longitudes)):
        suma += probabilidades[i] * longitudes[i]
    return suma