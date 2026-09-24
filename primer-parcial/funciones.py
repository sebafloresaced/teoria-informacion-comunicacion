import math
import random

# Obtener la informacion y entropia a partir de un vector de probabilidades

# generar una lista con la cantidad de información en bits de cada símbolo (utilizar comprensión de listas).
def informacion(P, r=2):
    I = [math.log(1 / p, r) if p > 0 else 0 for p in P]
    return I

# obtener la entropía de la fuente (utilizar la función anterior).
def entropia(P, r=2):
    I = informacion(P,r)
    H = 0
    for i in range(len(P)):
        H += P[i] * I[i]
    return H


# Dada una cadena de caracteres que representa un mensaje emitido por una fuente de memoria nula, devolver dos listas paralelas que contengan: 
# el alfabeto de la fuente y las probabilidades de cada símbolo

def obtener_fuente(mensaje):
    alfabeto = []
    for caracter in mensaje:
        if caracter not in alfabeto:
            alfabeto.append(caracter)

    probabilidades = [ mensaje.count(simbolo) / len(mensaje) for simbolo in alfabeto]
    return alfabeto, probabilidades

# Dados un número entero N, una lista que contenga el alfabeto de una fuente y otra con las probabilidades de cada símbolo, 
# simular la generación de una cadena de caracteres de longitud N emitida por esa fuente.

def generar_mensaje(N, alfabeto, probabilidades):
    simbolos = random.choices(
        alfabeto, # que simbolos usar
        weights=probabilidades, # que probabilidad tiene cada uno
        k=N # cuantas veces
    )
    mensaje = "".join(simbolos) # convierte la lista en una cadena
    return mensaje


# Obtener alfabeto codigo y longitudes 

def obtener_alfabeto_codigo(codigo):
    alfabeto = []
    for palabra in codigo:
        for caracter in palabra:
            if caracter not in alfabeto:
                alfabeto.append(caracter)
    return alfabeto

def obtener_longitudes(codigo):
    return [len(palabra) for palabra in codigo]


# Conseguir vector estacionario

def vector_estacionario(matriz):
    n = len(matriz)
    # Arrancamos suponiendo todos los estados equiprobables
    vector = [1 / n for i in range(n)]
    for j in range(10000):
        # Acá guardamos M * vector
        nuevo_vector = [0 for i in range(n)]
        # Multiplicación matriz por vector
        for fila in range(n):
            for columna in range(n):
                nuevo_vector[fila] += (
                    matriz[fila][columna]
                    * vector[columna]
                )
        # Buscamos cuánto cambió el vector
        diferencia = max(
            abs(nuevo_vector[i] - vector[i])
            for i in range(n)
        )
        # Si prácticamente no cambia, llegamos al estacionario
        if diferencia < 0.000001:
            return nuevo_vector
        # Seguimos iterando
        vector = nuevo_vector
    return vector

# Calcular la entropia de markov

def entropia_markov(matriz):
    # Primero calculamos la distribución estacionaria
    vector = vector_estacionario(matriz)
    n = len(matriz)
    h_total = 0
    # Cada columna representa las transiciones posibles desde un estado
    for columna in range(n):
        probabilidades = []
        # Construimos la distribución de probabilidades correspondiente a ese estado
        for fila in range(n):
            probabilidades.append(
                matriz[fila][columna]
            )
        # Entropía estando en ese estado
        h_estado = entropia(probabilidades)
        # La ponderamos por la probabilidad estacionaria de encontrarnos en dicho estado
        h_total += vector[columna] * h_estado
    return h_total


# Genera el alfabeto y la matriz de trancision 
def obtener_fuente_markov(mensaje):
    # Generamos el alfabeto sin repetir símbolos
    alfabeto = []
    for simbolo in mensaje:
        if simbolo not in alfabeto:
            alfabeto.append(simbolo)
    n = len(alfabeto)

    # Creamos una matriz n x n inicialmente llena de ceros
    matriz = [
        [0 for columna in range(n)]
        for fila in range(n)
    ]

    # Contamos las transiciones del mensaje
    for i in range(len(mensaje) - 1):
        actual = mensaje[i]
        siguiente = mensaje[i + 1]
        columna = alfabeto.index(actual)
        fila = alfabeto.index(siguiente)
        matriz[fila][columna] += 1

    # Convertimos las cantidades en probabilidades
    for columna in range(n):
        total = 0
        # Cantidad total de transiciones que salen de ese estado
        for fila in range(n):
            total += matriz[fila][columna]
        # Si existen transiciones desde ese estado, dividimos cada cantidad por el total
        if total > 0:
            for fila in range(n):
                matriz[fila][columna] /= total
    return alfabeto, matriz

# Compruebo si es memoria nula o no
def tiene_memoria(matriz, tolerancia):
    n = len(matriz)
    # Comparamos todas las columnas contra la primera
    for columna in range(1, n):
        for fila in range(n):
            diferencia = abs(
                matriz[fila][columna]
                - matriz[fila][0]
            )
            # Si alguna diferencia supera la tolerancia, el estado anterior sí afecta las probabilidades
            if diferencia > tolerancia:
                return True
    # Si todas las columnas son prácticamente iguales, es una fuente de memoria nula
    return False


# Verifica clasificaciones

def verifica_no_singular(codigo):
    for i in range(len(codigo)):
        for j in range(1 + i, len(codigo)):
            if codigo[i] == codigo[j]:
                return False
    return True

def verifica_instantaneo(codigo):
    for i in range(len(codigo)):
        for j in range(len(codigo)):
            if i != j and codigo[j].startswith(codigo[i]):
                return False
    return True

# verifica que sea univoco unicamente con orden 2
def verifica_univoco(codigo):
    palabras_generadas = []
    for i in range(len(codigo)):
        for j in range(len(codigo)):
            palabra = codigo[i] + codigo[j]
            if palabra in palabras_generadas:
                return False
            palabras_generadas.append(palabra)
    return True

def calcula_kraft(codigo):
    suma = 0
    longitudes = obtener_longitudes(codigo)
    alfabeto = obtener_alfabeto_codigo(codigo)
    r = len(alfabeto)
    for longitud in longitudes:
        suma += r ** (-longitud)
    return suma

def calcular_longitud_media(codigo, probabilidades):
    suma = 0
    longitudes = obtener_longitudes(codigo)
    for i in range(len(longitudes)):
        suma += probabilidades[i] * longitudes[i]
    return suma

def verificar_compacta(codigo, probabilidades):
    alfabeto = obtener_alfabeto_codigo(codigo)
    longitudes = obtener_longitudes(codigo)
    r = len(alfabeto)
    for i in range(len(longitudes)):
        if probabilidades[i] != r ** (-longitudes[i]):
            return False
    return True

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

# Primera parte (mensajes)

mensaje = ".;.:.:.::;:,::.;:,::,;,:;.:.;.;;:,.::.:,.:.;:::::."

alfabeto, probabilidades = obtener_fuente(mensaje)
print("Alfabeto:")
print(alfabeto)
print("Probabilidades:")
print(probabilidades)

alfabeto, matriz = obtener_fuente_markov(mensaje)

print("Alfabeto:")
print(alfabeto)
print("Matriz:")
print(matriz)

tieneMemoria = tiene_memoria(matriz,0.000000001)
print("Tiene memoria:")
print(tieneMemoria)

print("Entropia:")
if (tieneMemoria):
    print(entropia_markov(matriz)) # si tiene memoria
else :
    print(entropia(probabilidades)) # si no tiene memoria

extension, probabilidades_extension = extension_fuente(alfabeto, probabilidades, 2)

print("Extension:")
print(extension)
print("Probabilidades extension:")
print(probabilidades_extension)

print("Entropia extension:")
print(entropia(probabilidades_extension))

print("Alfabeto:")
print(alfabeto)
print("Vector estacionario:")
print(vector_estacionario(matriz))


# Segunda parte (codificacion)

alfabeto_codigo = ["/+", "*", "+-", "-", "*/"]
probabilidades = [0.15, 0.25, 0.05, 0.45, 0.1]
r = len(obtener_alfabeto_codigo(alfabeto_codigo))

print("Entropia:")
print(entropia(probabilidades,r))

print("Longitud media:")
print(calcular_longitud_media(alfabeto_codigo,probabilidades))

print("Suma de Kraft:")
print(calcula_kraft(alfabeto_codigo))

print("Es no singular:")
print(verifica_no_singular(alfabeto_codigo))

print("Es instantaneo:")
print(verifica_instantaneo(alfabeto_codigo))

print("Es univoco:")
print(verifica_univoco(alfabeto_codigo))

print("Es compacto:")
print(verificar_compacta(alfabeto_codigo,probabilidades))