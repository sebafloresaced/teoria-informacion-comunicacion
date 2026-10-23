import sys
from pathlib import Path
carpeta_funciones = (Path(__file__).resolve().parent.parent / "segundo-parcial")
sys.path.insert(0, str(carpeta_funciones))
import funciones

probabilidades_a_priori = [1/4, 1/4, 1/4, 1/4]
matriz_canal = [
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
    [0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0]
]

print("Capacidad: ", funciones.obtener_capacidad(probabilidades_a_priori,matriz_canal))

print()

probabilidades_a_priori = [1/3, 1/3, 1/3]
matriz_canal = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.2, 0.0, 0.8],
    [0.0, 0.0, 1.0, 0.0]
]

print("Capacidad: ", funciones.obtener_capacidad(probabilidades_a_priori,matriz_canal))

print()

probabilidades_a_priori = [1/3, 1/3, 1/3]
matriz_canal = [
    [0.3, 0.5, 0.2],
    [0.2, 0.3, 0.5],
    [0.5, 0.2, 0.3]
]

print("Capacidad: ", funciones.obtener_capacidad(probabilidades_a_priori,matriz_canal))

print()

probabilidades_a_priori = [1/4, 1/4, 1/4, 1/4]
matriz_canal = [
    [0.0, 0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0]
]

print("Capacidad: ", funciones.obtener_capacidad(probabilidades_a_priori,matriz_canal))
