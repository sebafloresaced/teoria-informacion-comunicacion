def extension_fuente(alfabeto, probabilidades, N):
    extension = [""]
    probabilidades_extension = [1]
    for _ in range(N):
        nuevas_palabras = []
        nuevas_probabilidades = []
        for i in range(len(extension)):
            for j in range(len(alfabeto)):
                nuevas_palabras.append(extension[i] + alfabeto[j])
                nuevas_probabilidades.append(
                    probabilidades_extension[i] * probabilidades[j]
                )
        extension = nuevas_palabras
        probabilidades_extension = nuevas_probabilidades
    return extension, probabilidades_extension

w = 0.8
probabilidades = [0.8 , 0.2]
alfabeto = [0 , 1]

extension, probabilidades_extension = extension_fuente(codigo, probabilidades, 3)
