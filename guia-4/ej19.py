def comprimir_RLC(mensaje):
    if not mensaje:
        return bytearray()

    resultado = bytearray()
    contador = 1
    simbolo_anterior = mensaje[0]

    for simbolo in mensaje[1:]:
        if simbolo == simbolo_anterior and contador < 255:
            contador += 1
        else:
            # Primero guardamos el simbolo y despues el contador
            
            # Guardamos el ASCII del simbolo
            resultado.append(ord(simbolo_anterior))

            # Guardamos la cantidad
            resultado.append(contador)

            simbolo_anterior = simbolo
            contador = 1

    # Agregamos el ultimo grupo
    resultado.append(ord(simbolo_anterior))
    resultado.append(contador)

    return resultado