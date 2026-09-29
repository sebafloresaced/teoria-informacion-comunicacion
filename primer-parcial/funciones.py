import math
import random

# Obtener la informacion y entropia a partir de un vector de probabilidades

# generar una lista con la cantidad de informacion en bits de cada simbolo (utilizar comprension de listas).
def informacion(P, r=2):
    I = [math.log(1 / p, r) if p > 0 else 0 for p in P]
    return I

# obtener la entropia de la fuente (utilizar la funcion anterior).
def entropia(P, r=2):
    I = informacion(P,r)
    H = 0
    for i in range(len(P)):
        H += P[i] * I[i]
    return H


# Dada una cadena de caracteres que representa un mensaje emitido por una fuente de memoria nula, devolver dos listas paralelas que contengan: 
# el alfabeto de la fuente y las probabilidades de cada simbolo

def obtener_fuente(mensaje):
    alfabeto = []
    for caracter in mensaje:
        if caracter not in alfabeto:
            alfabeto.append(caracter)

    probabilidades = [ mensaje.count(simbolo) / len(mensaje) for simbolo in alfabeto]
    return alfabeto, probabilidades

# Dados un numero entero N, una lista que contenga el alfabeto de una fuente y otra con las probabilidades de cada simbolo, 
# simular la generacion de una cadena de caracteres de longitud N emitida por esa fuente.

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

def vector_estacionario(matriz,vector):
    n = len(matriz)
    for j in range(10000):
        # Aca guardamos M * vector
        nuevo_vector = [0 for i in range(n)]
        # Multiplicacion matriz por vector
        for fila in range(n):
            for columna in range(n):
                nuevo_vector[fila] += (
                    matriz[fila][columna]
                    * vector[columna]
                )
        # Buscamos cuanto cambio el vector
        diferencia = max(
            abs(nuevo_vector[i] - vector[i])
            for i in range(n)
        )
        # Si practicamente no cambia, llegamos al estacionario
        if diferencia < 0.000001:
            return nuevo_vector
        # Seguimos iterando
        vector = nuevo_vector
    return vector

# Calcular la entropia de markov

def entropia_markov(matriz, vector_estacionario):
    n = len(matriz)
    h_total = 0
    # Cada columna representa las transiciones posibles desde un estado
    for columna in range(n):
        probabilidades = []
        # Construimos la distribucion de probabilidades correspondiente a ese estado
        for fila in range(n):
            probabilidades.append(
                matriz[fila][columna]
            )
        # Entropia estando en ese estado
        h_estado = entropia(probabilidades)
        # La ponderamos por la probabilidad estacionaria de encontrarnos en dicho estado
        h_total += vector_estacionario[columna] * h_estado
    return h_total


# Genera el alfabeto y la matriz de trancision 
def obtener_fuente_markov(mensaje):
    # Generamos el alfabeto sin repetir simbolos
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
def tiene_memoria(matriz, tolerancia = 0.000000001):
    n = len(matriz)
    # Comparamos todas las columnas contra la primera
    for columna in range(1, n):
        for fila in range(n):
            diferencia = abs(
                matriz[fila][columna]
                - matriz[fila][0]
            )
            # Si alguna diferencia supera la tolerancia, el estado anterior afecta las probabilidades
            if diferencia > tolerancia:
                return True
    # Si todas las columnas son practicamente iguales, es una fuente de memoria nula
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
    if not verifica_univoco(codigo):
        return False
    r = len(obtener_alfabeto_codigo(codigo))
    longitudes = obtener_longitudes(codigo)
    for i in range(len(codigo)):
        limite = math.ceil(math.log(1 / probabilidades[i], r))
        if longitudes[i] > limite:
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
print("\nAlfabeto:")
print(alfabeto)
print("\nProbabilidades:")
print(probabilidades)

alfabeto, matriz = obtener_fuente_markov(mensaje)

print("\nAlfabeto:")
print(alfabeto)
print("Matriz:")
# Muestra la matriz con formato
for fila in matriz:
    print("  ".join(f"{valor:.3f}" for valor in fila))

tieneMemoria = tiene_memoria(matriz,0.000000001)
print("\nTiene memoria:")
print(tieneMemoria)

if (tieneMemoria):
    print("\nAlfabeto:")
    print(alfabeto)
    print("Vector estacionario:")
    print(vector_estacionario(matriz, probabilidades))

    print("\nEntropia:")
    print(entropia_markov(matriz,vector_estacionario(matriz, probabilidades))) # si tiene memoria
else :
    print("\nEntropia:")
    print(entropia(probabilidades)) # si no tiene memoria

extension, probabilidades_extension = extension_fuente(alfabeto, probabilidades, 2)

print("\nExtension:")
print(extension)
print("\nProbabilidades extension:")
print(probabilidades_extension)

print("\nEntropia extension:")
print(entropia(probabilidades_extension))


# Se obtuvo el alfabeto identificando los simbolos distintos del mensaje. 
# La probabilidad de cada simbolos se calculo dividiendo su cantidad de apariciones por la longitud total del mensaje.
# Luego se contaron las parejas de simbolos consecutivos para construir la matriz de transicion. 
# Cada columna representa el simbolos actual y cada fila el siguiente. Se dividio cada cantidad por el total de transiciones 
# que salen del simbolos correspondiente.
# Al comparar las columnas se encontraron diferencias, por lo que se la considero una fuente con memoria.

# Para el calculo del vector estacionario:
# Se tomo como vector inicial la distribucion de probabilidades obtenida del mensaje, calculada dividiendo las apariciones de 
# cada simbolo por la cantidad total de simbolos.
# Luego se multiplico sucesivamente la matriz de transicion por el vector:
# Despues de cada multiplicacion, se calculo la mayor diferencia absoluta entre las componentes del vector nuevo y del anterior. 
# Cuando esa diferencia fue menor que \(10^{-6}\), se tomo el resultado como una aproximacion del vector estacionario, 
# ya que cumple aproximadamente: M V^* = V^*
# Esto significa que las probabilidades de los estados practicamente no cambian al aplicar una nueva transicion.


# Segunda parte (codificacion)

alfabeto_codigo = ["(]", "]", "[)", ")", "(["]
probabilidades = [0.15, 0.25, 0.05, 0.45, 0.1]
r = len(obtener_alfabeto_codigo(alfabeto_codigo))

print("\nEntropia:")
print(entropia(probabilidades,r))

print("\nLongitud media:")
print(calcular_longitud_media(alfabeto_codigo,probabilidades))

print("\numa de Kraft:")
print(calcula_kraft(alfabeto_codigo))

print("\nEs no singular:")
print(verifica_no_singular(alfabeto_codigo))

print("\nEs instantaneo:")
print(verifica_instantaneo(alfabeto_codigo))

print("\nEs univoco:")
print(verifica_univoco(alfabeto_codigo))

print("\nEs compacto:")
print(verificar_compacta(alfabeto_codigo,probabilidades))

# Se identificaron cuatro simbolos en el alfabeto del codigo, por lo que se utilizo (r=4). 
# Las longitudes de las palabras son (2,1,2,1,2). Su promedio ponderado por las probabilidades da 1,3.
# El codigo es no singular porque sus palabras son distintas, e instantaneo porque ninguna es prefijo de otra. 
# Por ser instantaneo, tambien es univoco.