import ej6

r = 2 # todos son binarios
alfabeto = ["A", "B", "C", "D", "E"]
probabilidades = [0.2, 0.15, 0.1, 0.3, 0.25]

c1 = ["01", "111", "110", "101", "100"]
c2 = ["00", "01", "10", "110", "111"]
c3 = ["0110", "010", "0111", "1", "00"]
c4 = ["11", "001", "000", "10", "01"]

print("Codigo 1:")
print("Rendimiento: ")
print(ej6.rendimiento(probabilidades, c1, r))
print("Redundancia: ")
print(ej6.redundancia(probabilidades, c1, r))

print("\nCodigo 2:")
print("Rendimiento: ")
print(ej6.rendimiento(probabilidades, c2, r))
print("Redundancia: ")
print(ej6.redundancia(probabilidades, c2, r))

print("\nCodigo 3:")
print("Rendimiento: ")
print(ej6.rendimiento(probabilidades, c3, r))
print("Redundancia: ")
print(ej6.redundancia(probabilidades, c3, r))

print("\nCodigo 4:")
print("Rendimiento: ")
print(ej6.rendimiento(probabilidades, c4, r))
print("Redundancia: ")
print(ej6.redundancia(probabilidades, c4, r))