# fila 0       → bits de paridad longitudinal + cruzada
# filas 1...n  → 7 bits ASCII + bit de paridad

def codificar(mensaje):
    if not mensaje:
        return bytearray()

    matriz = []
    # Generamos una fila por cada caracter
    for caracter in mensaje:
        ascii = ord(caracter)
        binario = bin(ascii)[2:].zfill(7)
        fila = []
        for bit in binario:
            fila.append(int(bit))
        # Bit de paridad de la fila
        paridad = sum(fila) % 2
        fila.append(paridad)
        matriz.append(fila)

    # Generamos la fila de control
    control = []
    for columna in range(7):
        suma = 0
        for fila in matriz:
            suma += fila[columna]

        control.append(suma % 2)

    # Bit de paridad cruzada
    paridad_cruzada = sum(control) % 2
    control.append(paridad_cruzada)

    # La fila de control va primera
    matriz.insert(0, control)

    # Convertimos cada fila de 8 bits en un byte
    resultado = bytearray()

    for fila in matriz:
        binario = ""
        for bit in fila:
            binario += str(bit)
        resultado.append(int(binario, 2))

    return resultado

def decodificar(secuencia):
    if not secuencia:
        return ""
    matriz = []
    # Convertimos cada byte nuevamente a 8 bits
    for byte in secuencia:
        binario = bin(byte)[2:].zfill(8)
        fila = []
        for bit in binario:
            fila.append(int(bit))
        matriz.append(fila)

    filas_error = []
    columnas_error = []
    # Verificamos las filas
    for i in range(len(matriz)):
        if sum(matriz[i]) % 2 != 0:
            filas_error.append(i)
    # Verificamos las columnas
    for columna in range(8):
        suma = 0
        for fila in range(len(matriz)):
            suma += matriz[fila][columna]
        if suma % 2 != 0:
            columnas_error.append(columna)

    # Caso 1: no hay errores
    if len(filas_error) == 0 and len(columnas_error) == 0:
        pass

    # Caso 2: un unico error -> se puede corregir
    elif len(filas_error) == 1 and len(columnas_error) == 1:
        fila = filas_error[0]
        columna = columnas_error[0]
        if matriz[fila][columna] == 0:
            matriz[fila][columna] = 1
        else:
            matriz[fila][columna] = 0

    # Caso 3: errores que no podemos corregir
    else:
        return ""

    # Recuperamos el mensaje ASCII
    mensaje = ""

    # Empezamos desde 1 porque la fila 0 es de control
    for i in range(1, len(matriz)):
        binario = ""
        # Solo los primeros 7 bits son ASCII
        for j in range(7):
            binario += str(matriz[i][j])
        numero = int(binario, 2)
        mensaje += chr(numero)

    return mensaje


mensaje = "CASA"

codificado = codificar(mensaje)

print("Codificado:")
print(list(codificado))

decodificado = decodificar(codificado)

print("Decodificado:")
print(decodificado)