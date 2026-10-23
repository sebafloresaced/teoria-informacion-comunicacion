import sys
from pathlib import Path
carpeta_funciones = (Path(__file__).resolve().parent.parent / "segundo-parcial")
sys.path.insert(0, str(carpeta_funciones))
import funciones

# Primer canal: entradas equiprobables
probabilidades_a_priori_c1 = [1/2, 1/2]
matriz_canal_1 = [
    [0.7, 0.0, 0.3, 0.0],
    [0.2, 0.6, 0.0, 0.2]
]

matriz_canal_2 = [
    [0.9, 0.0, 0.1],
    [0.0, 1.0, 0.0],
    [0.1, 0.1, 0.8],
    [0.0, 0.5, 0.5]
]
# Las entradas del segundo canal son las salidas del primero
probabilidades_a_priori_c2 = funciones.obtener_probabilidades_salida(probabilidades_a_priori_c1, matriz_canal_1)

print("Equivocacion canal 1: ", funciones.obtener_ruido(probabilidades_a_priori_c1, matriz_canal_1))
print("Informacion mutua canal 1: ", funciones.obtener_informacion_mutua(probabilidades_a_priori_c1, matriz_canal_1))

print()

print("Equivocacion canal 2: ", funciones.obtener_ruido(probabilidades_a_priori_c2, matriz_canal_2))
print("Informacion mutua canal 2: ", funciones.obtener_informacion_mutua(probabilidades_a_priori_c2, matriz_canal_2))

print()

matriz_canal_compuesto = funciones.obtener_matriz_canal_compuesto(matriz_canal_1, matriz_canal_2)
probabilidades_a_priori_compuesto = probabilidades_a_priori_c1

print("Matriz del canal compuesto: ")
funciones.mostrar_matriz(matriz_canal_compuesto)
print("Equivocacion canal compuesto: ", funciones.obtener_ruido(probabilidades_a_priori_compuesto, matriz_canal_compuesto))
print("Informacion mutua canal compuesto: ", funciones.obtener_informacion_mutua(probabilidades_a_priori_compuesto, matriz_canal_compuesto))