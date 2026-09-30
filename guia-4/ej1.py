import math

def extension_fuente(alfabeto, probabilidades, N):
    extension = [""]
    probabilidades_extension = [1]
    for _ in range(N):
        nuevas_palabras = []
        nuevas_probabilidades = []
        for i in range(len(extension)):
            for j in range(len(alfabeto)):
                nuevas_palabras.append(extension[i] + alfabeto[j])
                nuevas_probabilidades.append(
                    probabilidades_extension[i] * probabilidades[j]
                )
        extension = nuevas_palabras
        probabilidades_extension = nuevas_probabilidades
    return extension, probabilidades_extension

def informacion(P, r=2):
    I = [math.log(1 / p, r) if p > 0 else 0 for p in P]
    return I

def calcular_entropia(P, r=2):
    I = informacion(P,r)
    H = 0
    for i in range(len(P)):
        H += P[i] * I[i]
    return H

def obtener_longitudes(codigo):
    return [len(palabra) for palabra in codigo]
    
def calcular_longitud_media(codigo, probabilidades):
    suma = 0
    longitudes = obtener_longitudes(codigo)
    for i in range(len(longitudes)):
        suma += probabilidades[i] * longitudes[i]
    return suma

def obtener_alfabeto_codigo(codigo):
    alfabeto = []
    for palabra in codigo:
        for caracter in palabra:
            if caracter not in alfabeto:
                alfabeto.append(caracter)
    return alfabeto

def extension_verifica_Shannon(probabilidades, palabras_codigo, N):
    r = len(obtener_alfabeto_codigo(palabras_codigo))
    entropia = calcular_entropia(probabilidades, r)

    # Genero un alfabeto numerico con la cantidad de probabilidades que tengo (simula el alfabeto original de orden 1)
    alfabeto_aux = [str(i) for i in range(len(probabilidades))] 
    # Genero las probabilidades de la extensión de orden N
    _, probabilidades_extension = extension_fuente(alfabeto_aux, probabilidades, N)

    longitud_media = calcular_longitud_media(palabras_codigo, probabilidades_extension)

    return (entropia <= longitud_media / N) and (longitud_media / N <= entropia + 1 / N)