def distancia_hamming(palabra1, palabra2):
    distancia = 0
    for i in range(len(palabra1)):
        if palabra1[i] != palabra2[i]:
            distancia += 1
    return distancia

def analizar_codigo(codigo):
    distancia_minima = len(codigo[0])
    for i in range(len(codigo)):
        for j in range(i + 1, len(codigo)):
            distancia = distancia_hamming(codigo[i], codigo[j])
            if distancia < distancia_minima:
                distancia_minima = distancia

    errores_detectables = distancia_minima - 1
    errores_corregibles = (distancia_minima - 1) // 2

    return distancia_minima, errores_detectables, errores_corregibles