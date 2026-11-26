import math

def obtener_fuente(mensaje):
    alfabeto = []
    for caracter in mensaje:
        if caracter not in alfabeto:
            alfabeto.append(caracter)
    probabilidades = [ mensaje.count(simbolo) / len(mensaje) for simbolo in alfabeto]
    return alfabeto, probabilidades

def obtener_fuente_markov(mensaje):
    # Genero el alfabeto sin repetir simbolos
    alfabeto = []
    for simbolo in mensaje:
        if simbolo not in alfabeto:
            alfabeto.append(simbolo)
    n = len(alfabeto)
    # Creo una matriz n x n inicialmente llena de ceros
    matriz = [
        [0 for columna in range(n)]
        for fila in range(n)
    ]
    # Cuento las transiciones del mensaje
    for i in range(len(mensaje) - 1):
        actual = mensaje[i]
        siguiente = mensaje[i + 1]
        columna = alfabeto.index(actual)
        fila = alfabeto.index(siguiente)
        matriz[fila][columna] += 1
    # Convierto las cantidades en probabilidades
    for columna in range(n):
        total = 0
        # Cantidad total de transiciones que salen de ese estado
        for fila in range(n):
            total += matriz[fila][columna]
        # Si existen transiciones desde ese estado, divido cada cantidad por el total
        if total > 0:
            for fila in range(n):
                matriz[fila][columna] /= total
    return alfabeto, matriz

def tiene_memoria(matriz, tolerancia = 0.000000001):
    n = len(matriz)
    # Comparo todas las columnas contra la primera
    for columna in range(1, n):
        for fila in range(n):
            diferencia = abs(
                matriz[fila][columna]
                - matriz[fila][0]
            )
            # Si alguna diferencia supera la tolerancia, el estado anterior afecta las probabilidades
            if diferencia > tolerancia:
                return True
    return False

def vector_estacionario(matriz,vector):
    n = len(matriz)
    for j in range(10000):
        # Aca guardo M * vector
        nuevo_vector = [0 for i in range(n)]
        # Multiplicacion matriz por vector
        for fila in range(n):
            for columna in range(n):
                nuevo_vector[fila] += (
                    matriz[fila][columna]
                    * vector[columna]
                )
        # Busco cuanto cambio el vector
        diferencia = max(
            abs(nuevo_vector[i] - vector[i])
            for i in range(n)
        )
        # Si practicamente no cambia, llegue al estacionario
        if diferencia < 0.000001:
            return nuevo_vector
        # Sigo iterando
        vector = nuevo_vector
    return vector

def extension_fuente(alfabeto, probabilidades, N):
    extension = [""]
    probabilidades_extension = [1]
    for _ in range(N):
        nuevas_palabras = []
        nuevas_probabilidades = []
        for i in range(len(extension)):
            for j in range(len(alfabeto)):
                nuevas_palabras.append(extension[i] + alfabeto[j])
                nuevas_probabilidades.append(probabilidades_extension[i] * probabilidades[j])
        extension = nuevas_palabras
        probabilidades_extension = nuevas_probabilidades
    return extension, probabilidades_extension

def informacion(probabilidades, r=2):
    I = [math.log(1 / p, r) if p > 0 else 0 for p in probabilidades]
    return I

def entropia(probabilidades, r):
    I = informacion(probabilidades,r)
    H = 0
    for i in range(len(probabilidades)):
        H += probabilidades[i] * I[i]
    return H

def entropia_markov(matriz, vector_estacionario, r):
    n = len(matriz)
    h_total = 0
    # Cada columna representa las transiciones posibles desde un estado
    for columna in range(n):
        probabilidades = []
        # Contruyo la distribucion de probabilidades correspondiente a ese estado
        for fila in range(n):
            probabilidades.append(
                matriz[fila][columna]
            )
        # Entropia estando en ese estado
        h_estado = entropia(probabilidades, r)
        # La multiplico por la probabilidad estacionaria de encontrarnos en dicho estado
        h_total += vector_estacionario[columna] * h_estado
    return h_total

mensaje = "BBCCAABBCCAABBCCAABBCCAABBCCAA"

alfabeto, probabilidades = obtener_fuente(mensaje)
alfabeto, matriz = obtener_fuente_markov(mensaje)

print("\nAlfabeto:")
print(alfabeto)
print("Matriz:")
# Muestro la matriz con formato
for fila in matriz:
    print("  ".join(f"{valor:.3f}" for valor in fila))

tieneMemoria = tiene_memoria(matriz,0.000000001)
print("\nTiene memoria:")
print(tieneMemoria)

print("Vector estacionario:")
vector_estacionario = vector_estacionario(matriz, probabilidades)
print(vector_estacionario)

print("\nEntropia: ")
entropia = entropia_markov(matriz,vector_estacionario,3)
print(entropia)

extension, probabilidades_extension = extension_fuente(alfabeto, vector_estacionario, 2)

print("\nExtension:")
print(extension)
print("\nProbabilidades extension:")
print(probabilidades_extension)

print("\nEntropia extension:")
print(2 * entropia)