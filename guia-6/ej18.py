def verifica_sin_ruido(matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    for j in range(cantidad_salidas):
        elem_no_cero = False
        for i in range(cantidad_entradas):
            if (matriz_canal[i][j] > 0):
                if (elem_no_cero == False):
                    elem_no_cero = True
                else:
                    return False
    return True

def verifica_determinante(matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    for i in range(cantidad_entradas):
        elem_no_cero = False
        for j in range(cantidad_salidas):
            if (matriz_canal[i][j] > 0):
                if (elem_no_cero == False):
                    elem_no_cero = True
                else:
                    return False
    return True