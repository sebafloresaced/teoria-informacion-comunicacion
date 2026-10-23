def obtener_probabilidad_error(probabilidades_a_priori, matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    probabilidad_acierto = 0
    for j in range(cantidad_salidas):
        mayor_probabilidad_conjunta = 0
        for i in range(cantidad_entradas):
            probabilidad_conjunta = (probabilidades_a_priori[i] * matriz_canal[i][j])
            if probabilidad_conjunta > mayor_probabilidad_conjunta:
                mayor_probabilidad_conjunta = probabilidad_conjunta
        probabilidad_acierto += mayor_probabilidad_conjunta
    return 1 - probabilidad_acierto