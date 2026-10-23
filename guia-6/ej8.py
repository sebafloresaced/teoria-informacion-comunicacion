import sys
from pathlib import Path
carpeta_funciones = (Path(__file__).resolve().parent.parent / "segundo-parcial")
sys.path.insert(0, str(carpeta_funciones))
import funciones

entrada = "abcacaabbcacaabcacaaabcaca"
salida = "01010110011001000100010011"

# probabilidad de salida a partir de las secuencias de salida
alfabeto_salida, probabilidades_salida_secuencias = funciones.obtener_probabilidades_a_priori(salida)

#probabilidad de salida a partir de las probabilidades a priori y la matriz del canal
alfabeto_entrada, probabilidades_a_priori = funciones.obtener_probabilidades_a_priori(entrada)
_, _, matriz_canal = funciones.obtener_matriz_canal(entrada, salida)
probabilidades_salida_completa = funciones.obtener_probabilidades_salida(probabilidades_a_priori, matriz_canal)

print("Alfabeto entrada: ", alfabeto_entrada)
print("Alfabeto salida: ", alfabeto_salida)
print("Probabilidades de salida a partir de las secuencias de salida: ", probabilidades_salida_secuencias)
print("Probabilidades de salida a partir de las probabilidades a priori y la matriz del canal: ", probabilidades_salida_completa)

print()

entrada = "1101011001101010010101010100011111"
salida = "1001111111100011101101010111110110"

# probabilidad de salida a partir de las secuencias de salida
alfabeto_salida, probabilidades_salida_secuencias = funciones.obtener_probabilidades_a_priori(salida)

#probabilidad de salida a partir de las probabilidades a priori y la matriz del canal
alfabeto_entrada, probabilidades_a_priori = funciones.obtener_probabilidades_a_priori(entrada)
_, _, matriz_canal = funciones.obtener_matriz_canal(entrada, salida)
probabilidades_salida_completa = funciones.obtener_probabilidades_salida(probabilidades_a_priori, matriz_canal)

print("Alfabeto entrada: ", alfabeto_entrada)
print("Alfabeto salida: ", alfabeto_salida)
print("Probabilidades de salida a partir de las secuencias de salida: ", probabilidades_salida_secuencias)
print("Probabilidades de salida a partir de las probabilidades a priori y la matriz del canal: ", probabilidades_salida_completa)

print()

entrada = "110101100110101100110101100111110011"
salida = "110021102110022010220121122100112011"

# probabilidad de salida a partir de las secuencias de salida
alfabeto_salida, probabilidades_salida_secuencias = funciones.obtener_probabilidades_a_priori(salida)

#probabilidad de salida a partir de las probabilidades a priori y la matriz del canal
alfabeto_entrada, probabilidades_a_priori = funciones.obtener_probabilidades_a_priori(entrada)
_, _, matriz_canal = funciones.obtener_matriz_canal(entrada, salida)
probabilidades_salida_completa = funciones.obtener_probabilidades_salida(probabilidades_a_priori, matriz_canal)

print("Alfabeto entrada: ", alfabeto_entrada)
print("Alfabeto salida: ", alfabeto_salida)
print("Probabilidades de salida a partir de las secuencias de salida: ", probabilidades_salida_secuencias)
print("Probabilidades de salida a partir de las probabilidades a priori y la matriz del canal: ", probabilidades_salida_completa)