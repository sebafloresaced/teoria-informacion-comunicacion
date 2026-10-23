import math
import sys
from pathlib import Path
carpeta_funciones = (Path(__file__).resolve().parent.parent / "segundo-parcial")
sys.path.insert(0, str(carpeta_funciones))
import funciones

probabilidades_a_priori = [0.14, 0.52, 0.34]
matriz_canal = [
    [0.5, 0.3, 0.2],
    [0, 0.4, 0.6],
    [0.2, 0.8, 0]
]

probabilidades_salida = funciones.obtener_probabilidades_salida(probabilidades_a_priori, matriz_canal)
entropia_entrada = funciones.obtener_entropia_a_priori(probabilidades_a_priori)
# La misma función sirve para calcular H(B)
entropia_salida = funciones.obtener_entropia_a_priori(probabilidades_salida)

print("Entropia a priori: ", entropia_entrada)
print("Entropia de salida: ", entropia_salida)
print("Ruido: ", funciones.obtener_ruido(probabilidades_a_priori,matriz_canal))
print("Perdida: ", funciones.obtener_perdida(probabilidades_a_priori,matriz_canal))
print("Entropia afin: ", funciones.obtener_entropia_afin(probabilidades_a_priori,matriz_canal))

informacion_ab = entropia_entrada - funciones.obtener_ruido(probabilidades_a_priori, matriz_canal)
informacion_ba = entropia_salida - funciones.obtener_perdida(probabilidades_a_priori, matriz_canal)
print("I(A;B):", informacion_ab)
print("I(B;A):", informacion_ba)

print()

probabilidades_a_priori = [0.25, 0.25, 0.50]
matriz_canal = [
    [0.25, 0.25, 0.25, 0.25],
    [0.25, 0.25, 0, 0.5],
    [0.5, 0, 0.5, 0]
]

probabilidades_salida = funciones.obtener_probabilidades_salida(probabilidades_a_priori, matriz_canal)
entropia_entrada = funciones.obtener_entropia_a_priori(probabilidades_a_priori)
# La misma función sirve para calcular H(B)
entropia_salida = funciones.obtener_entropia_a_priori(probabilidades_salida)

print("Entropia a priori: ", entropia_entrada)
print("Entropia de salida: ", entropia_salida)
print("Ruido: ", funciones.obtener_ruido(probabilidades_a_priori,matriz_canal))
print("Perdida: ", funciones.obtener_perdida(probabilidades_a_priori,matriz_canal))
print("Entropia afin: ", funciones.obtener_entropia_afin(probabilidades_a_priori,matriz_canal))

informacion_ab = entropia_entrada - funciones.obtener_ruido(probabilidades_a_priori, matriz_canal)
informacion_ba = entropia_salida - funciones.obtener_perdida(probabilidades_a_priori, matriz_canal)
print("I(A;B):", informacion_ab)
print("I(B;A):", informacion_ba)

print()

probabilidades_a_priori = [0.12, 0.24, 0.14, 0.50]
matriz_canal = [
    [0.25, 0.15, 0.3, 0.3],
    [0.23, 0.27, 0.25, 0.25],
    [0.1, 0.4, 0.25, 0.25],
    [0.34, 0.26, 0.2, 0.2]
]

probabilidades_salida = funciones.obtener_probabilidades_salida(probabilidades_a_priori, matriz_canal)
entropia_entrada = funciones.obtener_entropia_a_priori(probabilidades_a_priori)
# La misma función sirve para calcular H(B)
entropia_salida = funciones.obtener_entropia_a_priori(probabilidades_salida)

print("Entropia a priori: ", entropia_entrada)
print("Entropia de salida: ", entropia_salida)
print("Ruido: ", funciones.obtener_ruido(probabilidades_a_priori,matriz_canal))
print("Perdida: ", funciones.obtener_perdida(probabilidades_a_priori,matriz_canal))
print("Entropia afin: ", funciones.obtener_entropia_afin(probabilidades_a_priori,matriz_canal))

informacion_ab = entropia_entrada - funciones.obtener_ruido(probabilidades_a_priori, matriz_canal)
informacion_ba = entropia_salida - funciones.obtener_perdida(probabilidades_a_priori, matriz_canal)
print("I(A;B):", informacion_ab)
print("I(B;A):", informacion_ba)