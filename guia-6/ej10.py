import ej11

probabilidades_a_priori = [2/5, 3/5]
matriz_canal = [
    [3/5, 2/5],
    [1/3, 2/3],
]

print("Entropia a priori: ", ej11.obtener_entropia_a_priori(probabilidades_a_priori))
print("Entropias a posteriori: ", ej11.obtener_entropias_a_posteriori(probabilidades_a_priori, matriz_canal))