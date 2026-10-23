import ej2

entrada1 = "1101011001101010010101010100011111"
salida1 = "1001111111100011101101010111110110"

alfabeto1, probabilidades_a_priori1 = ej2.obtener_probabilidades_a_priori(entrada1)
print("Alfabeto 1:")
print(alfabeto1)

print("Probabilidades:")
print(probabilidades_a_priori1)

alfabeto_entrada1, alfabeto_salida1, matriz1 = ej2.obtener_matriz_canal(entrada1,salida1)

print("Filas:", alfabeto_entrada1)
print("Columnas:", alfabeto_salida1)

for fila in matriz1:
    print([round(probabilidad, 4) for probabilidad in fila])

print("")

entrada2 = "110101100110101100110101100111110011"
salida2 = "110021102110022010220121122100112011"

alfabeto2, probabilidades_a_priori2 = ej2.obtener_probabilidades_a_priori(entrada2)
print("Alfabeto 2:")
print(alfabeto2)

print("Probabilidades 2:")
print(probabilidades_a_priori2)

alfabeto_entrada2, alfabeto_salida2, matriz2 = ej2.obtener_matriz_canal(entrada2,salida2)

print("Filas:", alfabeto_entrada2)
print("Columnas:", alfabeto_salida2)

for fila in matriz2:
    print([round(probabilidad, 4) for probabilidad in fila])