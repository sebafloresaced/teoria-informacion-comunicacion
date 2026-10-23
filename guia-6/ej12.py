import sys
from pathlib import Path
carpeta_funciones = (Path(__file__).resolve().parent.parent / "segundo-parcial")
sys.path.insert(0, str(carpeta_funciones))
import funciones

entrada = "abcacaabbcacaabcacaaabcaca"
salida = "01010110011001000100010011"

alfabeto_entrada, probabilidades_a_priori = funciones.obtener_probabilidades_a_priori(entrada)
_, alfabeto_salida, matriz_canal = funciones.obtener_matriz_canal(entrada,salida)

print("Alfabeto salida: ", alfabeto_salida)
print("Entropia a priori: ", funciones.obtener_entropia_a_priori(probabilidades_a_priori))
print("Entropias a posteriori: ", funciones.obtener_entropias_a_posteriori(probabilidades_a_priori, matriz_canal))

print()

entrada = "1101011001101010010101010100011111"
salida = "1001111111100011101101010111110110"

alfabeto_entrada, probabilidades_a_priori = funciones.obtener_probabilidades_a_priori(entrada)
_, alfabeto_salida, matriz_canal = funciones.obtener_matriz_canal(entrada,salida)

print("Alfabeto salida: ", alfabeto_salida)
print("Entropia a priori: ", funciones.obtener_entropia_a_priori(probabilidades_a_priori))
print("Entropias a posteriori: ", funciones.obtener_entropias_a_posteriori(probabilidades_a_priori, matriz_canal))

print()

entrada = "110101100110101100110101100111110011"
salida = "110021102110022010220121122100112011"

alfabeto_entrada, probabilidades_a_priori = funciones.obtener_probabilidades_a_priori(entrada)
_, alfabeto_salida, matriz_canal = funciones.obtener_matriz_canal(entrada,salida)

print("Alfabeto salida: ", alfabeto_salida)
print("Entropia a priori: ", funciones.obtener_entropia_a_priori(probabilidades_a_priori))
print("Entropias a posteriori: ", funciones.obtener_entropias_a_posteriori(probabilidades_a_priori, matriz_canal))

print()

alfabeto_entrada = ['a', 'b', 'c']
alfabeto_salida = ['1', '2', '3']
probabilidades_a_priori = [0.3, 0.3, 0.4]
matriz_canal = [
    [0.4, 0.4, 0.2],
    [0.3, 0.2, 0.5],
    [0.3, 0.4, 0.3]
]

print("Alfabeto salida: ", alfabeto_salida)
print("Entropia a priori: ", funciones.obtener_entropia_a_priori(probabilidades_a_priori))
print("Entropias a posteriori: ", funciones.obtener_entropias_a_posteriori(probabilidades_a_priori, matriz_canal))