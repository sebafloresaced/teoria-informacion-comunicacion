import math
import sys
from pathlib import Path
carpeta_funciones = (Path(__file__).resolve().parent.parent / "segundo-parcial")
sys.path.insert(0, str(carpeta_funciones))
import funciones

def verifica_uniforme(matriz_canal):
    primera_fila = sorted(matriz_canal[0])
    for fila in matriz_canal[1:]:
        fila_ordenada = sorted(fila)
        for j in range(len(primera_fila)):
            if not math.isclose(primera_fila[j], fila_ordenada[j], abs_tol=1e-10):
                return False
    return True

def obtener_capacidad(probabilidades_a_priori, matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    if (funciones.verifica_sin_ruido(matriz_canal)):
        return math.log(cantidad_entradas, 2)
    elif (funciones.verifica_determinante(matriz_canal)):
        return math.log(cantidad_salidas, 2)
    elif funciones.verifica_uniforme(matriz_canal):
        return math.log(len(matriz_canal[0]), 2) - funciones.obtener_entropia_a_priori(matriz_canal[0])
    else:
        # calculo maximo aproximado
        return 0