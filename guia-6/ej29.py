import sys
from pathlib import Path
carpeta_funciones = (Path(__file__).resolve().parent.parent / "segundo-parcial")
sys.path.insert(0, str(carpeta_funciones))
import funciones

matriz_canal = [
    [0.6, 0.3, 0.1],
    [0.1, 0.8, 0.1],
    [0.3, 0.3, 0.4]
]

probabilidades_a_priori = [1/3, 1/3, 1/3]
print(f"Probabilidad de error: {funciones.obtener_probabilidad_error(probabilidades_a_priori, matriz_canal):.4f}")

print()

probabilidades_a_priori = [1/8, 3/8, 1/2]
print(f"Probabilidad de error: {funciones.obtener_probabilidad_error(probabilidades_a_priori, matriz_canal):.4f}")

print()

probabilidades_a_priori = [4/15, 1/5, 8/15]
print(f"Probabilidad de error: {funciones.obtener_probabilidad_error(probabilidades_a_priori, matriz_canal):.4f}")