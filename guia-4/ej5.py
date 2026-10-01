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

def huffman(alfabeto, probabilidades):
    codigos = [""] * len(alfabeto)

    # Cada grupo guarda: [probabilidad, índices de símbolos]
    grupos = []

    for i in range(len(alfabeto)):
        grupos.append([probabilidades[i], [i]])

    while len(grupos) > 1:
        # Ordenamos de menor a mayor probabilidad
        grupos.sort(key=lambda x: x[0])

        # Sacamos los dos menos probables
        grupo1 = grupos.pop(0)
        grupo2 = grupos.pop(0)

        # Agregamos 0 y 1 a sus códigos
        for i in grupo1[1]:
            codigos[i] = "0" + codigos[i]

        for i in grupo2[1]:
            codigos[i] = "1" + codigos[i]

        # Fusionamos ambos grupos
        nuevo_grupo = [
            grupo1[0] + grupo2[0],
            grupo1[1] + grupo2[1]
        ]

        grupos.append(nuevo_grupo)

    return codigos

def shannon_fano(alfabeto, probabilidades):
    codigos = [""] * len(alfabeto)

    # Ordenamos los indices de mayor a menor probabilidad
    indices = list(range(len(alfabeto)))
    indices.sort(key=lambda i: probabilidades[i], reverse=True)

    # Grupos que todavía tenemos que dividir
    grupos = [indices]
    while len(grupos) > 0:
        grupo = grupos.pop(0)
        # Si queda un solo simbolo, no se puede dividir mas
        if len(grupo) <= 1:
            continue
        # Calculamos la probabilidad total del grupo
        total = 0
        for i in grupo:
            total += probabilidades[i]
        # Buscamos el mejor punto de corte
        acumulado = 0
        mejor_corte = 1
        menor_diferencia = float("inf")
        for k in range(1, len(grupo)):
            acumulado += probabilidades[grupo[k - 1]]
            suma_izquierda = acumulado
            suma_derecha = total - acumulado
            diferencia = abs(suma_izquierda - suma_derecha)
            if diferencia < menor_diferencia:
                menor_diferencia = diferencia
                mejor_corte = k
        # Dividimos el grupo
        izquierda = grupo[:mejor_corte]
        derecha = grupo[mejor_corte:]
        # Asignamos los bits
        for i in izquierda:
            codigos[i] += "0"
        for i in derecha:
            codigos[i] += "1"
        # Estos grupos después deben volver a dividirse
        grupos.append(izquierda)
        grupos.append(derecha)
    return codigos

w = 0.7
probabilidades = [w , 1 - w]
alfabeto = ["0" , "1"]

codigo1 = huffman(alfabeto, probabilidades)
print("\nCodificacion con huffman:")
print(codigo1)

print("\nVerifica el primer teorema de Shannon:")
print(verifica_Shannon(probabilidades,codigo1))

extension, probabilidades_extension = extension_fuente(alfabeto, probabilidades, 2)

print("\nExtension:")
print(extension)

print("\nProbabilidades extension")
print(probabilidades_extension)

codigo2 = shannon_fano(extension, probabilidades_extension)

print("\nCodificacion:")
print(codigo2)

print("\nVerifica el primer teorema de Shannon:")
print(verifica_Shannon(probabilidades_extension,codigo2))