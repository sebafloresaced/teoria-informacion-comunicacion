def huffman(alfabeto, probabilidades):
    codigos = [""] * len(alfabeto)

    # Cada grupo guarda: [probabilidad, índices de símbolos]
    grupos = []

    for i in range(len(alfabeto)):
        grupos.append([probabilidades[i], [i]])

    while len(grupos) > 1:
        # Ordenamos de menor a mayor probabilidad
        grupos.sort(key=lambda x: x[0])

        # Sacamos los dos menos probables
        grupo1 = grupos.pop(0)
        grupo2 = grupos.pop(0)

        # Agregamos 0 y 1 a sus códigos
        for i in grupo1[1]:
            codigos[i] = "0" + codigos[i]

        for i in grupo2[1]:
            codigos[i] = "1" + codigos[i]

        # Fusionamos ambos grupos
        nuevo_grupo = [
            grupo1[0] + grupo2[0],
            grupo1[1] + grupo2[1]
        ]

        grupos.append(nuevo_grupo)

    return codigos

def shannon_fano(alfabeto, probabilidades):
    codigos = [""] * len(alfabeto)

    # Ordenamos los indices de mayor a menor probabilidad
    indices = list(range(len(alfabeto)))
    indices.sort(key=lambda i: probabilidades[i], reverse=True)

    # Grupos que todavía tenemos que dividir
    grupos = [indices]
    while len(grupos) > 0:
        grupo = grupos.pop(0)
        # Si queda un solo simbolo, no se puede dividir mas
        if len(grupo) <= 1:
            continue
        # Calculamos la probabilidad total del grupo
        total = 0
        for i in grupo:
            total += probabilidades[i]
        # Buscamos el mejor punto de corte
        acumulado = 0
        mejor_corte = 1
        menor_diferencia = float("inf")
        for k in range(1, len(grupo)):
            acumulado += probabilidades[grupo[k - 1]]
            suma_izquierda = acumulado
            suma_derecha = total - acumulado
            diferencia = abs(suma_izquierda - suma_derecha)
            if diferencia < menor_diferencia:
                menor_diferencia = diferencia
                mejor_corte = k
        # Dividimos el grupo
        izquierda = grupo[:mejor_corte]
        derecha = grupo[mejor_corte:]
        # Asignamos los bits
        for i in izquierda:
            codigos[i] += "0"
        for i in derecha:
            codigos[i] += "1"
        # Estos grupos después deben volver a dividirse
        grupos.append(izquierda)
        grupos.append(derecha)
    return codigos

simbolos = ["S1", "S2", "S3", "S4"]
probabilidadesA = [0.2, 0.2, 0.3, 0.3]
probabilidadesB = [0.4, 0.25, 0.25, 0.1]

print("Fuente A:")
print("\nHuffman:")
print(huffman(simbolos,probabilidadesA))
print("\nShanno Fano:")
print(shannon_fano(simbolos,probabilidadesA))

print("\n\nFuente B:")
print("\nHuffman:")
print(huffman(simbolos,probabilidadesB))
print("\nShanno Fano:")
print(shannon_fano(simbolos,probabilidadesB))