def agregar_paridad(caracter):
    ascii = ord(caracter)
    binario = bin(ascii)[2:].zfill(7)
    cantidad_unos = binario.count("1")

    if cantidad_unos % 2 == 0:
        paridad = 0
    else:
        paridad = 1

    byte = (ascii << 1) | paridad

    return byte

def verificar_paridad(byte):
    paridad = byte & 1
    ascii = byte >> 1
    binario = bin(ascii)[2:].zfill(7)
    cantidad_unos = binario.count("1")

    if cantidad_unos % 2 == 0:
        paridad_esperada = 0
    else:
        paridad_esperada = 1

    return paridad == paridad_esperada