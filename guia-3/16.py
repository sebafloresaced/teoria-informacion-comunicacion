import random

def generar_mensaje(codigo, probabilidades, n):
    mensaje = ""
    for i in range(n):
        palabra = random.choices(codigo, weights=probabilidades, k=1)[0]
        mensaje += palabra
    return mensaje