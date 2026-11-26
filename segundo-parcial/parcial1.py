import math

def obtener_probabilidades_a_priori(entrada):
    alfabeto = []
    for simbolo in entrada:
        if simbolo not in alfabeto:
            alfabeto.append(simbolo)
    probabilidades = [
        entrada.count(simbolo) / len(entrada)
        for simbolo in alfabeto
    ]
    return alfabeto, probabilidades

def obtener_longitudes(codigo):
    return [len(palabra) for palabra in codigo]

def calcular_longitud_media(codigo, probabilidades):
    suma = 0
    longitudes = obtener_longitudes(codigo)
    for i in range(len(longitudes)):
        suma += probabilidades[i] * longitudes[i]
    return suma

def obtener_entropia_a_priori(probabilidades_a_priori):
    entropia = 0
    for p in probabilidades_a_priori:
        if (p > 0):
            entropia += p * math.log(1 / p, 2)
    return entropia

def rendimiento(probabilidades, codificacion):
    return obtener_entropia_a_priori(probabilidades) / calcular_longitud_media(codificacion, probabilidades)

def redundancia(probabilidades, codificacion, r = 2):
    return 1 - rendimiento(probabilidades, codificacion)

def obtener_extension(alfabeto, probabilidades, orden):
    extension = [[]]
    probabilidades_extension = [1]
    for _ in range(orden):
        nueva_extension = []
        nuevas_probabilidades = []
        for i in range(len(extension)):
            for j in range(len(alfabeto)):
                nueva_extension.append(extension[i] + [alfabeto[j]])
                nuevas_probabilidades.append(probabilidades_extension[i] * probabilidades[j])
        extension = nueva_extension
        probabilidades_extension = nuevas_probabilidades
    return extension, probabilidades_extension

def obtener_codigo_huffman(probabilidades):
    codigos = ["" for _ in probabilidades]
    # Cada grupo contiene: [probabilidad total, lista de índices de sus símbolos]
    grupos = [[probabilidades[i], [i]] for i in range(len(probabilidades))]
    while len(grupos) > 1:
        # Busco y saco el grupo menos probable.
        menor = 0
        for i in range(1, len(grupos)):
            if grupos[i][0] < grupos[menor][0]:
                menor = i
        grupo_1 = grupos.pop(menor)
        # Busco y saco el segundo menos probable.
        menor = 0
        for i in range(1, len(grupos)):
            if grupos[i][0] < grupos[menor][0]:
                menor = i
        grupo_2 = grupos.pop(menor)
        # Agrego un bit por delante de cada código.
        for indice in grupo_1[1]:
            codigos[indice] = "0" + codigos[indice]
        for indice in grupo_2[1]:
            codigos[indice] = "1" + codigos[indice]
        # Uno ambos grupos.
        nuevo_grupo = [grupo_1[0] + grupo_2[0], grupo_1[1] + grupo_2[1]]
        grupos.append(nuevo_grupo)
    return codigos

mensaje = "111110111011111011001111110111"
codigo = ["0", "1"]

alfabeto, probabilidades = obtener_probabilidades_a_priori(mensaje)

print("Entropia: ", obtener_entropia_a_priori(probabilidades)) 
print("Longitud media: ", calcular_longitud_media(codigo, probabilidades))
print("Rendimiento: ", rendimiento(probabilidades, codigo))
print("Redundancia: ", redundancia(probabilidades, codigo))

# Extension de orden 2
print()

extension_2, probabilidades_2 = obtener_extension(alfabeto, probabilidades, 2)
codigo_2 = obtener_codigo_huffman(probabilidades_2)

print("Entropia de extension 2: ", obtener_entropia_a_priori(probabilidades_2))
print("Longitud media de extension 2: ", calcular_longitud_media(codigo_2, probabilidades_2))
print("Rendimiento de extension 2: ", rendimiento(probabilidades_2, codigo_2))
print("Redundancia de extension 2: ", redundancia(probabilidades_2, codigo_2))

# Extension de orden 3
print()

extension_3, probabilidades_3 = obtener_extension(alfabeto, probabilidades, 3)
codigo_3 = obtener_codigo_huffman(probabilidades_3)

print("Entropia de extension 3: ", obtener_entropia_a_priori(probabilidades_3))
print("Longitud media de extension 3: ", calcular_longitud_media(codigo_3, probabilidades_3))
print("Rendimiendo de extension 3: ", rendimiento(probabilidades_3, codigo_3))
print("Redundancia de extension 3: ", redundancia(probabilidades_3, codigo_3))