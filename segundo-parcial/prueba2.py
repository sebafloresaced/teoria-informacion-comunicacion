import sys
from pathlib import Path
carpeta_funciones = (Path(__file__).resolve().parent.parent / "segundo-parcial")
sys.path.insert(0, str(carpeta_funciones))
import funciones

mensaje_recibido = "000010011111111011010111"
matriz_canal = [
    [0.0, 0.0, 1.0],  # Entrada 0
    [0.4, 0.4, 0.2]   # Entrada 1
]

# a) Obtener la distribución óptima de entrada.
capacidad, p_0 = funciones.estimar_capacidad_canal_binario(matriz_canal)
p_1 = 1 - p_0
probabilidades_a_priori = [p_0, p_1]

print("Distribución óptima:")
print(f"P(0) = {p_0:.4f}")
print(f"P(1) = {p_1:.4f}")

ruido = funciones.obtener_ruido(probabilidades_a_priori, matriz_canal)
perdida = funciones.obtener_perdida(probabilidades_a_priori, matriz_canal)
informacion_mutua = funciones.obtener_informacion_mutua(probabilidades_a_priori, matriz_canal)

print(f"H(A/B) = {ruido:.4f} bits")
print(f"H(B/A) = {perdida:.4f} bits")
print(f"I(A,B) = {informacion_mutua:.4f} bits")

# Construir la matriz: una fila cada 8 bits.
matriz = []

for i in range(0, len(mensaje_recibido), 8):
    fila = []
    for bit in mensaje_recibido[i:i + 8]:
        fila.append(int(bit))
    matriz.append(fila)

print("\nMatriz recibida:")
funciones.mostrar_matriz(matriz)

print("Se localizo un error en la segunda fila, tercera columna. Cambio ese bit de 1 a 0.")
matriz[1][2] = 0
print("\nMatriz con error corregido:")
funciones.mostrar_matriz(matriz)

print("\nLa matriz del canal indica que si se recibe C, se puede asegurar que se envio un 0. Por lo tanto, no puede ocurrir un error 0 -> 1")
print("Sin embargo, la paridad indica que el bit recibido como 1 deberia haber sido 0. El mensaje no es compatible con este canal.")

# Explicaciones:
# a) Obtener la distribución óptima de entrada:
#     Se probaron distribuciones de entrada de la forma P(0)=p y P(1)=1-p, variando p entre 0 y 1 con un paso de 0.0001. 
#     Para cada distribución se calculó la información mutua y se conservó aquella que produjo el mayor valor.
#     P(0)=0.5643; P(1)=0.4357
# b) Para calcular la equivocación H(A/B), primero se obtuvieron las probabilidades de salida y luego las probabilidades a posteriori mediante Bayes. 
#     A partir de ellas se calculó la entropía correspondiente a cada salida y se realizó un promedio ponderado por las probabilidades de salida.
#     El resultado H(A/B) = 0.3698 bits representa la incertidumbre promedio que queda sobre la entrada después de conocer la salida. 
#     Si se recibe A o B, se sabe que se transmitió un 1. Si se recibe C, existe incertidumbre porque puede provenir tanto de un 0 como de un 1.
#     Para calcular la pérdida H(B/A), se obtuvo la entropía de cada fila de la matriz del canal y se ponderó por la probabilidad de entrada correspondiente. 
#     El resultado H(B/A) = 0.6631 bits representa la incertidumbre promedio sobre la salida cuando se conoce la entrada. 
#     Si se transmite un 0, siempre se recibe C. Si se transmite un 1, pueden recibirse A, B o C con probabilidades 0.4, 0.4 y 0.2.
#     La información mutua se calculó como I(A,B) = H(A) - H(A/B), obteniendo 0.6182 bits. Como se utilizó la distribución óptima, 
#     este valor coincide con la capacidad estimada. 
# c) El mensaje recibido es 000010011111111011010111. Se organiza en filas de 8 bits, considerando 7 bits ASCII y un bit de paridad por carácter. 
#     Se utiliza paridad par, con los bits de paridad de fila en la última columna y los de paridad de columna en la última fila.
#     La matriz recibida es:
#         00001001
#         11111110
#         11010111
#     Se verificó que cada fila y cada columna tuviera una cantidad par de unos, incluyendo los bits de paridad. 
#     La segunda fila tiene 7 unos y la tercera columna tiene 1 uno, por lo que ambas incumplen la paridad. Las demás filas y columnas la cumplen.
#     Suponiendo un único error, el bit incorrecto se encuentra en la intersección de la segunda fila y la tercera columna. Se cambia ese bit de 1 a 0 y se obtiene:
#         00001001
#         11011110
#         11010111
#     Después de la corrección, todas las filas y columnas cumplen la paridad par. El mensaje corregido, incluyendo los bits de paridad, es 000010011101111011010111.
# d) La regla de decisión asigna la entrada 1 cuando se recibe A o B, porque esas salidas solo pueden provenir de un 1. Cuando se recibe C, 
#     se decide 0, ya que P(0)P(C/0) = 0.5643 es mayor que P(1)P(C/1) = 0.08714.
#     Por lo tanto, un 0 transmitido siempre produce C y se recupera como 0. Un 1 transmitido puede producir C y recuperarse incorrectamente como 0. 
#     Bajo esta regla, el canal permite errores de 1 a 0, pero no de 0 a 1.
#     La corrección por paridad indica que se recibió un 1 donde debería haber un 0. Esto implicaría que durante la transmisión ocurrió un cambio de 0 a 1, 
#     que es imposible para este canal. Por lo tanto, bajo la hipótesis de un único error utilizada para la corrección, 
#     el mensaje recibido no pudo haberse transmitido por este canal y recuperado mediante la regla de decisión indicada.