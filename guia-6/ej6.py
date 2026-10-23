import ej7

alfabeto_entrada = ['a', 'b', 'c']
alfabeto_salida = [1, 2, 3]
probabilidades_a_priori = [0.3, 0.3, 0.4]
matriz_canal = [
    [0.4, 0.4, 0.2],
    [0.3, 0.2, 0.5],
    [0.3, 0.4, 0.3]
]

print("Alfabeto entrada: ", alfabeto_entrada)
print("Alfabeto salida: ", alfabeto_salida)

print("Probabilidades de simbolos de salida: ", ej7.obtener_probabilidades_salida(probabilidades_a_priori, matriz_canal))

matriz_posteriori = ej7.obtener_probabilidades_a_posteriori(probabilidades_a_priori, matriz_canal)
print("Probabilidades a posteriori:")
for fila in matriz_posteriori:
    print([round(probabilidad, 4) for probabilidad in fila])

print("Probabilidades simultaneos:")
matriz_simultaneos = ej7.obtener_matriz_simultaneos(probabilidades_a_priori, matriz_canal)
for fila in matriz_simultaneos:
    print([round(probabilidad, 4) for probabilidad in fila])
