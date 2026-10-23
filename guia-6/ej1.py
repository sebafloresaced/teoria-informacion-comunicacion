import ej2

entrada = "abcacaabbcacaabcacaaabcaca"
salida = "01010110011001000100010011"

alfabeto, probabilidades_a_priori = ej2.obtener_probabilidades_a_priori(entrada)
print("Alfabeto:")
print(alfabeto)

print("Probabilidades:")
print(probabilidades_a_priori)

alfabeto_entrada, alfabeto_salida, matriz = ej2.obtener_matriz_canal(entrada,salida)
print("Matriz:")
# Muestra la matriz con formato
for fila in matriz:
    print("  ".join(f"{valor}" for valor in fila))