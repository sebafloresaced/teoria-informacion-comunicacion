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

def verifica_Shannon(probabilidades, codigo):
    alfabeto_codigo = obtener_alfabeto_codigo(codigo)
    r = len(alfabeto_codigo)
    entropia = calcular_entropia(probabilidades, r)
    longitud_media = calcular_longitud_media(codigo, probabilidades)

    print("\nEntropia:")
    print(entropia)

    print("\nLongitud media:")
    print(longitud_media)

    return (entropia <= longitud_media) and (longitud_media <= entropia + 1)

probabilidades = [0.5, 0.2, 0.3]
codigo = ["11", "010", "00"]
extension = ["10", "001", "110", "010", "0000", "0001", "111", "0110", "0111"]

_ , probabilidades_extension = extension_fuente(codigo, probabilidades, 2)

print("La fuente verifica el primer teorema de Shannon: ")
print(verifica_Shannon(probabilidades, codigo))

print("\nLa extension de orden 2 verifica el primer teorema de Shannon: ")
print(verifica_Shannon(probabilidades_extension, extension))