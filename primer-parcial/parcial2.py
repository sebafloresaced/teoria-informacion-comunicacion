import math

def obtener_alfabeto_codigo(codigo):
    alfabeto = []
    for palabra in codigo:
        for caracter in palabra:
            if caracter not in alfabeto:
                alfabeto.append(caracter)
    return alfabeto

def obtener_longitudes(codigo):
    return [len(palabra) for palabra in codigo]

def calcula_kraft(codigo):
    suma = 0
    longitudes = obtener_longitudes(codigo)
    alfabeto = obtener_alfabeto_codigo(codigo)
    r = len(alfabeto)
    for longitud in longitudes:
        suma += r ** (-longitud)
    return suma

def informacion(probabilidades, r=2):
    I = [math.log(1 / p, r) if p > 0 else 0 for p in probabilidades]
    return I

def entropia(probabilidades, r=2):
    I = informacion(probabilidades,r)
    H = 0
    for i in range(len(probabilidades)):
        H += probabilidades[i] * I[i]
    return H

def calcular_longitud_media(codigo, probabilidades):
    suma = 0
    longitudes = obtener_longitudes(codigo)
    for i in range(len(longitudes)):
        suma += probabilidades[i] * longitudes[i]
    return suma

def verifica_univoco(codigo):
    palabras_generadas = []
    for i in range(len(codigo)):
        for j in range(len(codigo)):
            palabra = codigo[i] + codigo[j]
            if palabra in palabras_generadas:
                return False
            palabras_generadas.append(palabra)
    return True

def verificar_compacta(codigo, probabilidades):
    if not verifica_univoco(codigo):
        return False
    r = len(obtener_alfabeto_codigo(codigo))
    longitudes = obtener_longitudes(codigo)
    for i in range(len(codigo)):
        limite = math.ceil(math.log(1 / probabilidades[i], r))
        if longitudes[i] > limite:
            return False
    return True

alfabeto_codigo = ["A", "AB", "AC", "B", "CA"]
# Codigo compacto propuesto:
# alfabeto_codigo = ["A", "CA", "CB", "B", "CC"]

probabilidades = [1/3, 1/9, 1/9, 1/3, 1/9]
r = len(obtener_alfabeto_codigo(alfabeto_codigo))

print("\nSuma de Kraft:")
print(calcula_kraft(alfabeto_codigo))

print("\nEntropia:")
print(entropia(probabilidades,r))

print("\nLongitud media:")
print(calcular_longitud_media(alfabeto_codigo,probabilidades))

print("\nEs compacto:")
print(verificar_compacta(alfabeto_codigo,probabilidades))

