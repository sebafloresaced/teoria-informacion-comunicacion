import ej6

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

r = 2
probabilidades = [0.5, 0.2, 0.3]
c1 = ["11", "010", "00"]

c2 = ["10", "001", "110", "010", "0000", "0001", "111", "0110", "0111"]
_ , probabilidades_extension = extension_fuente(c1, probabilidades, 2)

print("Codigo 1:")
print("\nRendimiento: ")
print(ej6.rendimiento(probabilidades, c1, r))
print("\nRedundancia: ")
print(ej6.redundancia(probabilidades, c1, r))

print("Codigo 2:")
print("\nRendimiento: ")
print(ej6.rendimiento(probabilidades_extension, c2, r))
print("\nRedundancia: ")
print(ej6.redundancia(probabilidades_extension, c2, r))