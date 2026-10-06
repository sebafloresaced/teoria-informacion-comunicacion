dmin = min d(ci, cj)
detecta = dmin - 1
corrige = piso((dmin - 1) / 2)

palabras = ["Rojo", "Amarillo", "Verde", "Azul"]

codigo1 = ["00", "01", "10", "11"]

d(00,01)=1
d(00,10)=1
d(00,11)=2
d(01,10)=2
d(01,11)=1
d(10,11)=1

dmin = 1
detecta = 0
corrige = 0

codigo2 = ["000", "100", "101", "111"]

dmin = 1
detecta = 0
corrige = 0

codigo3 = ["0000", "0011", "1010", "0101"]

dmin = 2
detecta = 1
corrige = 0