def informacion(P) -> a partir de una lista de probabilidades devuele la informacion
def entropia(P) -> a partir de una lista de probabilidades devuele la entropia
def obtener_fuente(mensaje) -> a partir de un mensaje devuelve el alfabeto fuente y las probabilidades
def generar_mensaje(N, alfabeto, probabilidades) -> crea un mensaje de longitud N, con el alfabeto y las probabilidades indicadas
def obtener_alfabeto_codigo(codigo) -> a partir de un mensaje codificado, devuelve el alfabeto codigo en forma de lista
def obtener_longitudes(codigo) -> a partir de un mensaje codificado, devuelve las longitudes en forma de lista
def vector_estacionario(matriz) -> a partir de una matriz de transicion, devuelve el vector estacionario
def entropia_markov(matriz) -> a partir de una matriz de transicion, devuelve la entropia
def obtener_fuente_markov(mensaje) -> a partir de un mensaje, devuelve el alfabeto y la matriz de transicion
def tiene_memoria(matriz, tolerancia) -> devuelve true/false dependiendo de si tiene memoria

def verifica_no_singular(codigo)
def verifica_instantaneo(codigo)
def verifica_univoco(codigo) -> las tres devuelven true/false dependiendo si cumplen con la clasificacion

def calcula_kraft(codigo) -> calcula la suma de kraft
def calcular_longitud_media(codigo, probabilidades) -> calcula la longitud media
def verificar_compacta(codigo, probabilidades) -> verifica si el codigo es compacto
def extension_fuente(alfabeto, probabilidades, N) -> devuelve la extension y las probabilidades de extension de orden N