# suma impar -> 1
# suma par -> 0

a = [
    [0,0,1,0,0,0,0,1], # ✓
    [1,0,0,0,0,1,1,1], # ✓
    [1,0,0,0,0,0,1,0], # ✓
    [1,0,1,0,0,1,1,0], # ✓
    [1,0,0,0,0,0,1,0]  # ✓
   # ✓✓✓✓✓✓✓✓
]

# No hay errores: la matriz corregida queda igual
a_corregida = [
    [0,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,1,1],
    [1,0,0,0,0,0,1,0],
    [1,0,1,0,0,1,1,0],
    [1,0,0,0,0,0,1,0]
]

a_bits = ["1000011", "1000001", "1010011", "1000001"]
a_caracteres = ["C", "A", "S", "A"]
# Mensaje: CASA

b = [
    [0,0,1,0,1,1,0,1], # ✓
    [1,0,0,1,1,0,0,1], # ✓
    [1,0,0,0,1,0,1,0], # ✖
    [1,0,0,1,1,1,0,0], # ✓
    [1,0,0,0,0,0,1,0]  # ✓
   # ✓✓✖✓✓✓✓✓
]

# Falla la fila 2 y la columna 2 . Se corrige b[2][2]: 0 -> 1
b_corregida = [
    [0,0,1,0,1,1,0,1],
    [1,0,0,1,1,0,0,1],
    [1,0,1,0,1,0,1,0],
    [1,0,0,1,1,1,0,0],
    [1,0,0,0,0,0,1,0]
]

b_bits = ["1001100", "1010101", "1001110", "1000001"]
b_caracteres = ["L", "U", "N", "A"]
# Mensaje: LUNA

c = [
    [0,0,1,0,1,0,1,0], # ✖
    [1,0,0,0,0,0,1,0], # ✓
    [1,0,0,1,1,0,1,0], # ✓
    [1,0,0,1,1,1,1,1], # ✓
    [1,0,1,0,0,1,0,1]  # ✓
   # ✓✓✓✓✖✓✓✓✓
]

# El error esta en la fila de control, columna 4. Se corrige c[0][4]: 1 -> 0
c_corregida = [
    [0,0,1,0,0,0,1,0],
    [1,0,0,0,0,0,1,0],
    [1,0,0,1,1,0,1,0],
    [1,0,0,1,1,1,1,1],
    [1,0,1,0,0,1,0,1]
]

c_bits = ["1000001", "1001101", "1001111", "1010010"]
c_caracteres = ["A", "M", "O", "R"]
# Mensaje: AMOR

d = [
    [0,0,0,1,0,1,0,0], # ✓
    [1,0,0,1,0,0,0,0], # ✓
    [1,0,0,1,1,1,1,0], # ✖
    [1,0,0,1,1,0,0,1], # ✓
    [1,0,0,0,0,0,1,0]  # ✓
   # ✓✓✓✓✓✓✓✖
]

# El error esta en un bit de paridad: d[2][7].
# Se corrige 0 -> 1
d_corregida = [
    [0,0,0,1,0,1,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,1,1,1,1],
    [1,0,0,1,1,0,0,1],
    [1,0,0,0,0,0,1,0]
]

d_bits = ["1001000", "1001111", "1001100", "1000001"]
d_caracteres = ["H", "O", "L", "A"]
# Mensaje: HOLA

e = [
    [0,0,1,1,0,1,0,1], # ✓
    [1,0,0,1,1,0,1,0], # ✓
    [1,0,1,0,1,0,1,1], # ✖
    [1,0,1,0,0,1,0,0], # ✖
    [1,0,0,0,0,0,1,0]  # ✓
   # ✓✓✖✓✓✓✖✓
]

# Fallan dos filas y dos columnas.
# No existe una correccion unica.
e_corregida = None

# Lo recibido, sin poder asegurar que sea el mensaje original:
e_bits_recibidos = ["1001101", "1010101", "1010010", "1000001"]
e_caracteres_recibidos = ["M", "U", "R", "A"]
# Mensaje recibido: MURA

# Una correccion posible:
e_corregida_posible_1 = [
    [0,0,1,1,0,1,0,1],
    [1,0,0,1,1,0,1,0],
    [1,0,0,0,1,0,1,1],
    [1,0,1,0,0,1,1,0],
    [1,0,0,0,0,0,1,0]
]
e_bits_posible_1 = ["1001101", "1000101", "1010011", "1000001"]
e_caracteres_posible_1 = ["M", "E", "S", "A"]
# Posible mensaje: MESA

f = [
    [0,0,0,0,1,0,0,1], # ✓
    [1,0,1,0,1,0,0,1], # ✓
    [1,0,1,0,0,1,0,1], # ✓
    [1,0,0,0,1,0,1,1], # ✓
    [1,0,1,0,0,1,1,0]  # ✓
    # ✓✓✖✓✖✓✓✓
]

# No fallan filas, pero fallan dos columnas.
# Puede haber dos errores en una misma fila, pero no sabemos en cual.
# Por lo tanto no se puede corregir univocamente.
f_corregida = None

f_bits_recibidos = ["1010100", "1010010", "1000101", "1010011"]
f_caracteres_recibidos = ["T", "R", "E", "S"]
# Mensaje recibido: TRES
# No se puede asegurar que sea el mensaje original.

g = [
    [0,0,0,1,1,1,0,1], # ✓
    [1,0,0,1,0,0,1,1], # ✓
    [1,0,0,1,1,1,0,1], # ✖
    [1,0,0,0,1,1,0,0], # ✖
    [1,0,0,1,1,1,1,1]  # ✓
    # ✓✓✓✓✓✓✓✓
]

# Fallan dos filas, pero no falla ninguna columna.
# Puede haber dos errores en una misma columna, pero no sabemos cual.
# Por lo tanto no se puede corregir univocamente.
g_corregida = None

g_bits_recibidos = ["1001001", "1001110", "1000110", "1001111"]
g_caracteres_recibidos = ["I", "N", "F", "O"]
# Mensaje recibido: INFO
# No se puede asegurar que sea el mensaje original.

h = [
    [0,0,1,1,1,1,1,0], # ✖
    [1,0,0,0,0,1,1,1], # ✓
    [1,0,0,1,0,0,0,0], # ✓
    [1,0,0,0,0,0,1,0], # ✓
    [1,0,1,0,1,0,1,0]  # ✓
    # ✓✓✓✓✓✓✓✖
]

# El error esta en el bit de paridad cruzada h[0][7].
# Se corrige 0 -> 1
h_corregida = [
    [0,0,1,1,1,1,1,1],
    [1,0,0,0,0,1,1,1],
    [1,0,0,1,0,0,0,0],
    [1,0,0,0,0,0,1,0],
    [1,0,1,0,1,0,1,0]
]

h_bits = ["1000011", "1001000", "1000001", "1010101"]
h_caracteres = ["C", "H", "A", "U"]
# Mensaje: CHAU