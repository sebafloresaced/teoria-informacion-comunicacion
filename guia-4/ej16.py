# TC = tamanio original / tamanio comprimido

def tasa_compresion(mensaje, codificado):
    return len(mensaje) / len(codificado)