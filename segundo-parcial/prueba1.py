# Para importar este archivo desde la guia:
import sys
from pathlib import Path
carpeta_funciones = (Path(__file__).resolve().parent.parent / "segundo-parcial")
sys.path.insert(0, str(carpeta_funciones))
import funciones

mensaje = "1100111001111001"
codigo = ["11", "01", "00", "10"]

mensaje_codificado = "1100111001111001"

# Cada palabra de dos bits representa un símbolo de la fuente.
mensaje = [mensaje_codificado[i:i + 2] for i in range(0, len(mensaje_codificado), 2)]

alfabeto, probabilidades = funciones.obtener_probabilidades_a_priori(mensaje)
entropia = funciones.obtener_entropia_a_priori(probabilidades)

print("Alfabeto:", alfabeto)
print("Probabilidades:", probabilidades)
print(f"Entropía: {entropia:.4f} bits/símbolo")
print(f"Longitud promedio del código: {funciones.calcular_longitud_media(codigo, probabilidades):.4f} bits/símbolo")
print(f"Rendimiento de la fuente: {funciones.rendimiento(probabilidades, codigo, 2):.4f} bits/símbolo")
print(f"Redundancia del código: {funciones.redundancia(probabilidades, codigo, 2):.4f} bits/símbolo")

print("\n--- Extensión de orden 3 ---")

orden = 3
extension, probabilidades_extension = funciones.obtener_extension(codigo, probabilidades, orden)
codigos_extension = funciones.obtener_codigo_huffman(probabilidades_extension)

print(f"Entropia de la fuente de la extensión: {funciones.obtener_entropia_a_priori(probabilidades_extension):.4f} bits/símbolo")
print(f"Longitud promedio del código de la extensión: {funciones.calcular_longitud_media(codigos_extension, probabilidades_extension):.4f} bits/símbolo")
print(f"Rendimiento de la fuente de la extensión: {funciones.rendimiento(probabilidades_extension, codigos_extension, 2):.4f} bits/símbolo")
print(f"Redundancia del código de la extensión: {funciones.redundancia(probabilidades_extension, codigos_extension, 2):.4f} bits/símbolo")

# Explicaciones 
# a) La entropía de la fuente se calculó en base a las frecuencias relativas de los símbolos tomados de a 2, 
# bajo la fórmula de que la entropía es el promedio ponderado de las cantidades de información. 
# b) El código binario óptimo se hizo mediante la codificación de Huffman, que sigue este algoritmo, basándose
# en la extensión de orden 3 y en la nueva distribución de probabilidades: 
#     1. Se inicia un árbol binario vacío con aristas ponderadas. Para hijos izquierdos, las aristas se ponderan 
#         con 0 y, para hijos derechos, se ponderan con 1. 
#     2. Mientras el árbol no contenga a todo el alfabeto:    
#         a. Ordenar alfabeto según probabilidades    
#         b. Unificar los 2 símbolos o grupos de símbolos menos probables y sumar sus probabilidades.    
#         c. Crear un nodo vacío cuyos hijos sean éstos 2 grupos de símbolos. El hijo izquierdo será el menos probable. 
#     3. La codificación de cada símbolo será la concatenación de los 1s y 0s recorridos del árbol desde la raíz hasta donde esté alojado el símbolo. 
# c) El rendimiento se calculó con la siguiente fórmula: η=(H_r(S))/L (1) 
# Por otro lado, la redundancia se calcula restándole la eficiencia a 1: R=1-η (2) 
# El algoritmo siguió estos pasos: 
#     1. Se calcula la entropía de la fuente Hr(S) con una función implementada en la primera parte. 
#     2. Se calcula la longitud media L con una función implementada para el primer parcial. 
#     3. Se calcula el rendimiento a partir de la ecuación (1). 
#     4. Se devuelve la eficiencia y la redundancia, calculada con la ecuación (2), en una tupla. 
# Interpretación 
# d) Vemos que, a mayor sea n, la longitud media cada vez más se acerca a la entropía. 
# Esto va un poco en línea con el Primer Teorema de Shannon, que nos dice que la longitud media 
# de una extensión está acotada por su entropía. Es por esto que tiene mayor rendimiento la extensión 
# que la fuente. Sin embargo, tampoco hay que abusar porque si n es muy grande, la complejidad algorítmica 
# aumenta para decodificar.