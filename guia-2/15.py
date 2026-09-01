import random

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
        # Cantidad total de transiciones
        # que salen de ese estado
        for fila in range(n):
            total += matriz[fila][columna]

        # Si existen transiciones desde ese estado,
        # dividimos cada cantidad por el total
        if total > 0:
            for fila in range(n):
                matriz[fila][columna] /= total

    return alfabeto, matriz


def generar_mensaje_markov(n, alfabeto, matriz):
    # Elegimos aleatoriamente el primer símbolo
    actual = random.choice(alfabeto)
    mensaje = actual
    # Ya tenemos un símbolo, por eso generamos n - 1 más
    for _ in range(n - 1):
        # Buscamos qué columna corresponde
        # al símbolo actual
        columna = alfabeto.index(actual)

        probabilidades = []

        # Extraemos la columna de la matriz
        for fila in range(len(alfabeto)):
            probabilidades.append(
                matriz[fila][columna]
            )

        # Elegimos el próximo símbolo según
        # esas probabilidades
        siguiente = random.choices(
            alfabeto,
            weights=probabilidades,
            k=1
        )[0]

        mensaje += siguiente

        # El siguiente pasa a ser el estado actual
        actual = siguiente

    return mensaje


def tiene_memoria(matriz, tolerancia):
    n = len(matriz)

    # Comparamos todas las columnas
    # contra la primera
    for columna in range(1, n):
        for fila in range(n):
            diferencia = abs(
                matriz[fila][columna]
                - matriz[fila][0]
            )
            # Si alguna diferencia supera la tolerancia,
            # el estado anterior sí afecta las probabilidades
            if diferencia > tolerancia:
                return True

    # Si todas las columnas son prácticamente iguales,
    # es una fuente de memoria nula
    return False