import sys
from pathlib import Path
carpeta_funciones = (Path(__file__).resolve().parent.parent / "segundo-parcial")
sys.path.insert(0, str(carpeta_funciones))
import funciones

matriz_canal = [
    [0.6, 0.4],
    [0.2, 0.8]
]

capacidad, mejor_probabilidad = funciones.estimar_capacidad_canal_binario(matriz_canal)
print("Capacidad: ", capacidad)
print(f"Mejor probabilidad: {mejor_probabilidad:.4f}", )

print()

matriz_canal = [
    [0.25, 0.75],
    [0.9, 0.1]
]

capacidad, mejor_probabilidad = funciones.estimar_capacidad_canal_binario(matriz_canal)
print("Capacidad: ", capacidad)
print(f"Mejor probabilidad: {mejor_probabilidad:.4f}", )

print()

matriz_canal = [
    [0.51, 0.49],
    [0.72, 0.28]
]

capacidad, mejor_probabilidad = funciones.estimar_capacidad_canal_binario(matriz_canal)
print("Capacidad: ", capacidad)
print(f"Mejor probabilidad: {mejor_probabilidad:.4f}", )

print()

matriz_canal = [
    [0.77, 0.23],
    [0.2, 0.8]
]

capacidad, mejor_probabilidad = funciones.estimar_capacidad_canal_binario(matriz_canal)
print("Capacidad: ", capacidad)
print(f"Mejor probabilidad: {mejor_probabilidad:.4f}", )