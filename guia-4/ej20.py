import ej16
import ej19

m1 = "XXXYZZZZ"
m2 = "AAAABBBCCDAA"
m3 = "UUOOOOAAAIEUUUU"

c1 = ej19.comprimir_RLC(m1)
c2 = ej19.comprimir_RLC(m2)
c3 = ej19.comprimir_RLC(m3)

print("Tasa de compresion:")
print(ej16.tasa_compresion(m1, c1))
print(ej16.tasa_compresion(m2, c2))
print(ej16.tasa_compresion(m3, c3))
