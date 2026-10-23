import sys
from pathlib import Path
carpeta_funciones = (Path(__file__).resolve().parent.parent / "segundo-parcial")
sys.path.insert(0, str(carpeta_funciones))
import funciones

def estimar_capacidad_canal_binario(matriz_canal, paso = 0.01):
    if len(matriz_canal) != 2:
        raise ValueError("El canal debe tener dos entradas")
    if not (0 < paso <= 1):
        raise ValueError("El paso debe estar entre 0 y 1")
    capacidad = -1
    mejor_probabilidad = 0
    i = 0
    while True:
        # Incluimos p = 1 aunque el paso no divida exactamente a 1.
        p = min(i * paso, 1.0)
        probabilidades = [p, 1 - p]
        informacion_mutua = funciones.obtener_informacion_mutua(probabilidades, matriz_canal)
        if informacion_mutua > capacidad:
            capacidad = informacion_mutua
            mejor_probabilidad = p
        if p == 1:
            break
        i += 1
    return capacidad, mejor_probabilidad