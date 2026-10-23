import sys
from pathlib import Path
carpeta_funciones = (Path(__file__).resolve().parent.parent / "segundo-parcial")
sys.path.insert(0, str(carpeta_funciones))
import funciones

probabilidades_a_priori = [1/3, 1/3, 1/3]
matriz_canal = [
    [0.4, 0.6, 0.0, 0.0],
    [0.0, 0.0, 0.5, 0.5],
    [0.0, 0.0, 0.7, 0.3]
]

matriz_canal_reducido = funciones.obtener_canal_reducido(matriz_canal)
funciones.mostrar_matriz(matriz_canal_reducido)
print("Informacion mutua: ", funciones.obtener_informacion_mutua(probabilidades_a_priori, matriz_canal_reducido))
print("Es determinante: ", funciones.verifica_determinante(matriz_canal_reducido))

print()

probabilidades_a_priori = [1/3, 1/3, 1/3]
matriz_canal = [
    [0.2, 0.3, 0.5],
    [0.0, 0.0, 1.0],
    [0.0, 0.0, 1.0]
]

matriz_canal_reducido = funciones.obtener_canal_reducido(matriz_canal)
funciones.mostrar_matriz(matriz_canal_reducido)
print("Informacion mutua: ", funciones.obtener_informacion_mutua(probabilidades_a_priori, matriz_canal_reducido))
print("Es determinante: ", funciones.verifica_determinante(matriz_canal_reducido))

print()

probabilidades_a_priori = [1/3, 1/3, 1/3]
matriz_canal = [
    [0.4, 0.0, 0.2, 0.4],
    [0.4, 0.3, 0.2, 0.1],
    [0.0, 0.3, 0.0, 0.7]
]

matriz_canal_reducido = funciones.obtener_canal_reducido(matriz_canal)
funciones.mostrar_matriz(matriz_canal_reducido)
print("Informacion mutua: ", funciones.obtener_informacion_mutua(probabilidades_a_priori, matriz_canal_reducido))
print("Es determinante: ", funciones.verifica_determinante(matriz_canal_reducido))

print()

probabilidades_a_priori = [1/4, 1/4, 1/4, 1/4]
matriz_canal = [
    [0.0, 0.5, 0.0, 0.5],
    [0.8, 0.0, 0.2, 0.0],
    [0.0, 0.5, 0.0, 0.5],
    [0.8, 0.0, 0.2, 0.0]
]

matriz_canal_reducido = funciones.obtener_canal_reducido(matriz_canal)
funciones.mostrar_matriz(matriz_canal_reducido)
print("Informacion mutua: ", funciones.obtener_informacion_mutua(probabilidades_a_priori, matriz_canal_reducido))
print("Es determinante: ", funciones.verifica_determinante(matriz_canal_reducido))