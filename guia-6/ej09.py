import sys
from pathlib import Path
carpeta_funciones = (Path(__file__).resolve().parent.parent / "segundo-parcial")
sys.path.insert(0, str(carpeta_funciones))
import funciones

entrada = "abcacaabbcacaabcacaaabcaca"
salida = "01010110011001000100010011"

alfabeto_entrada, probabilidades_a_priori = funciones.obtener_probabilidades_a_priori(entrada)
_, alfabeto_salida, matriz_canal = funciones.obtener_matriz_canal(entrada, salida)
matriz_a_posteriori = funciones.obtener_matriz_a_posteriori(probabilidades_a_priori, matriz_canal)
matriz_simultaneos = funciones.obtener_matriz_simultaneos(probabilidades_a_priori, matriz_canal)

print("Alfabeto entrada: ", alfabeto_entrada)
print("Alfabeto salida: ", alfabeto_salida)
print("Matriz de probabilidades a posteriori: ")
for fila in matriz_a_posteriori:
    print([round(probabilidad, 4) for probabilidad in fila])
print("Matriz de probabilidades simultaneas: ")
for fila in matriz_simultaneos:
    print([round(probabilidad, 4) for probabilidad in fila])

print()

entrada = "1101011001101010010101010100011111"
salida = "1001111111100011101101010111110110"

alfabeto_entrada, probabilidades_a_priori = funciones.obtener_probabilidades_a_priori(entrada)
_, alfabeto_salida, matriz_canal = funciones.obtener_matriz_canal(entrada, salida)
matriz_a_posteriori = funciones.obtener_matriz_a_posteriori(probabilidades_a_priori, matriz_canal)
matriz_simultaneos = funciones.obtener_matriz_simultaneos(probabilidades_a_priori, matriz_canal)

print("Alfabeto entrada: ", alfabeto_entrada)
print("Alfabeto salida: ", alfabeto_salida)
print("Matriz de probabilidades a posteriori: ")
for fila in matriz_a_posteriori:
    print([round(probabilidad, 4) for probabilidad in fila])
print("Matriz de probabilidades simultaneas: ")
for fila in matriz_simultaneos:
    print([round(probabilidad, 4) for probabilidad in fila])

print()

entrada = "110101100110101100110101100111110011"
salida = "110021102110022010220121122100112011"

alfabeto_entrada, probabilidades_a_priori = funciones.obtener_probabilidades_a_priori(entrada)
_, alfabeto_salida, matriz_canal = funciones.obtener_matriz_canal(entrada, salida)
matriz_a_posteriori = funciones.obtener_matriz_a_posteriori(probabilidades_a_priori, matriz_canal)
matriz_simultaneos = funciones.obtener_matriz_simultaneos(probabilidades_a_priori, matriz_canal)

print("Alfabeto entrada: ", alfabeto_entrada)
print("Alfabeto salida: ", alfabeto_salida)
print("Matriz de probabilidades a posteriori: ")
for fila in matriz_a_posteriori:
    print([round(probabilidad, 4) for probabilidad in fila])
print("Matriz de probabilidades simultaneas: ")
for fila in matriz_simultaneos:
    print([round(probabilidad, 4) for probabilidad in fila])