import sys
from pathlib import Path
carpeta_funciones = (Path(__file__).resolve().parent.parent / "segundo-parcial")
sys.path.insert(0, str(carpeta_funciones))
import funciones

def obtener_canal_reducido(matriz_canal):
    # Copiamos la matriz para no modificar la original.
    matriz_reducida = [fila[:] for fila in matriz_canal]
    hubo_reduccion = True
    while hubo_reduccion:
        hubo_reduccion = False
        cantidad_columnas = len(matriz_reducida[0])
        for columna_1 in range(cantidad_columnas):
            for columna_2 in range(columna_1 + 1, cantidad_columnas):
                if funciones.verificar_reduccion_suficiente(matriz_reducida, columna_1, columna_2):
                    matriz_determinista = funciones.obtener_canal_determinista(matriz_reducida, columna_1, columna_2)
                    matriz_reducida = funciones.obtener_matriz_canal_compuesto(matriz_reducida, matriz_determinista)
                    hubo_reduccion = True
                    break
            if hubo_reduccion:
                break
    return matriz_reducida