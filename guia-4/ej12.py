import math

def huffman(probabilidades):
    codigos = [""] * len(probabilidades)

    # Cada grupo guarda: [probabilidad, índices de símbolos]
    grupos = []

    for i in range(len(probabilidades)):
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

def shannon_fano(probabilidades):
    codigos = [""] * len(probabilidades)

    # Ordenamos los indices de mayor a menor probabilidad
    indices = list(range(len(probabilidades)))
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

def obtener_longitudes(codigo):
    return [len(palabra) for palabra in codigo]

def calcular_longitud_media(codigo, probabilidades):
    suma = 0
    longitudes = obtener_longitudes(codigo)
    for i in range(len(longitudes)):
        suma += probabilidades[i] * longitudes[i]
    return suma

def informacion(P, r=2):
    I = [math.log(1 / p, r) if p > 0 else 0 for p in P]
    return I

# obtener la entropia de la fuente (utilizar la funcion anterior).
def calcular_entropia(P, r=2):
    I = informacion(P,r)
    H = 0
    for i in range(len(P)):
        H += P[i] * I[i]
    return H

def rendimiento(probabilidades, codificacion, r = 2):
    return calcular_entropia(probabilidades, r) / calcular_longitud_media(codificacion, probabilidades)

def redundancia(probabilidades, codificacion, r = 2):
    return 1 - rendimiento(probabilidades, codificacion, r)

def crear_arbol(codigos, probabilidades):
    arbol = {}

    for i in range(len(codigos)):
        nodo = arbol

        for bit in codigos[i]:
            if bit not in nodo:
                nodo[bit] = {}

            nodo = nodo[bit]

        nodo["simbolo"] = "S" + str(i + 1)
        nodo["probabilidad"] = probabilidades[i]

    return arbol


def mostrar_arbol(nodo, prefijo=""):
    if "simbolo" in nodo:
        print(
            prefijo
            + nodo["simbolo"]
            + " (" + str(nodo["probabilidad"]) + ")"
        )
        return

    if "0" in nodo:
        print(prefijo + "├── 0")
        mostrar_arbol(nodo["0"], prefijo + "│   ")

    if "1" in nodo:
        print(prefijo + "└── 1")
        mostrar_arbol(nodo["1"], prefijo + "    ")

probabilidades = [0.385, 0.154, 0.128, 0.154, 0.179]

print("Entropia de la fuente:")
print(calcular_entropia(probabilidades))

codificacion_huffman = huffman(probabilidades)
codificacion_shannon_fano = shannon_fano(probabilidades)

print("\nCodificacion huffman:")
print(codificacion_huffman)

print("\nLongitud media:")
print(calcular_longitud_media(codificacion_huffman,probabilidades))

print("\nRendimiento:")
print(rendimiento(probabilidades,codificacion_huffman))

print("\nRedundancia:")
print(redundancia(probabilidades,codificacion_huffman))

print("\nArbol de Huffman:")
arbol_huffman = crear_arbol(codificacion_huffman, probabilidades)
print("Raiz")
mostrar_arbol(arbol_huffman)

print("\n\nCodificacion shannon_fano:")
print(codificacion_shannon_fano)

print("\nLongitud media:")
print(calcular_longitud_media(codificacion_shannon_fano,probabilidades))

print("\nRendimiento:")
print(rendimiento(probabilidades,codificacion_shannon_fano))

print("\nRedundancia:")
print(redundancia(probabilidades,codificacion_shannon_fano))

print("\nArbol de Shannon-Fano:")
arbol_shannon = crear_arbol(codificacion_shannon_fano, probabilidades)
print("Raiz")
mostrar_arbol(arbol_shannon)