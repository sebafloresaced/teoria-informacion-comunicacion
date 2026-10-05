# símbolos → palabras código → cadena de 0 y 1 → bytes
def codificar(alfabeto, codificacion, mensaje): 
    mensaje_binario = ""

    # Reemplazamos cada simbolo por su palabra codigo
    for simbolo in mensaje:
        posicion = alfabeto.index(simbolo)
        mensaje_binario += codificacion[posicion]
    
    # Calculamos cuantos bits faltan para completar el ultimo byte
    relleno = (8 - len(mensaje_binario) % 8) % 8
    # Agregamos ceros de relleno
    mensaje_binario += "0" * relleno
    
    # Creamos el bytearray
    resultado = bytearray()
    # El primer byte del resultado indica cuantos bits de relleno agregamos
    resultado.append(relleno)

    # Convertimos cada grupo de 8 bits en un numero
    for i in range(0, len(mensaje_binario), 8):
        bloque = mensaje_binario[i:i + 8]
        resultado.append(int(bloque, 2))
    
    return resultado

# bytes → cadena de 0 y 1 → palabras código → símbolos
def decodificar(alfabeto, codificacion, secuencia):
    # El primer byte contiene la cantidad de bits de relleno
    relleno = secuencia[0]
    mensaje_binario = ""

    # Convertimos cada byte nuevamente a 8 bits
    for i in range(1, len(secuencia)):
        binario = bin(secuencia[i])[2:]
        binario = binario.zfill(8)
        mensaje_binario += binario

    # Sacamos los ceros de relleno
    if relleno > 0:
        mensaje_binario = mensaje_binario[:-relleno]

    mensaje = ""
    palabra = ""

    # Vamos formando palabras codigo
    for bit in mensaje_binario:
        palabra += bit
        # si ya forme una palabra
        if palabra in codificacion:
            posicion = codificacion.index(palabra)
            mensaje += alfabeto[posicion]
            palabra = ""
    
    return mensaje