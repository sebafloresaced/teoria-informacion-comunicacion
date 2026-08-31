import random

# Dada una cadena de caracteres que representa un mensaje emitido por una fuente de memoria nula, devolver dos listas paralelas que contengan: 
# el alfabeto de la fuente y las probabilidades de cada símbolo
mensaje = "ABACA"

def obtener_fuente(mensaje):
    alfabeto = []
    for caracter in mensaje:
        if caracter not in alfabeto:
            alfabeto.append(caracter)

    probabilidades = [ mensaje.count(simbolo) / len(mensaje) for simbolo in alfabeto]
    return alfabeto, probabilidades

# Dados un número entero N, una lista que contenga el alfabeto de una fuente y otra con las probabilidades de cada símbolo, 
# simular la generación de una cadena de caracteres de longitud N emitida por esa fuente.
alfabeto = ['A', 'B', 'C']
probabilidades = [0.6, 0.2, 0.2]
N = 10

def generar_mensaje(N, alfabeto, probabilidades):
    simbolos = random.choices(
        alfabeto, # que simbolos usar
        weights=probabilidades, # que probabilidad tiene cada uno
        k=N # cuantas veces
    )
    mensaje = "".join(simbolos) # convierte la lista en una cadena
    return mensaje