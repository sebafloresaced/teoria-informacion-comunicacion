import ej22

colores = ["Rojo", "Amarillo", "Verde", "Azul"]
codificacion1 = ["0100100", "0101000", "0010010", "0100000"]
codificacion2 = ["0100100", "0010010", "0101000", "0100001"]
codificacion3 = ["0110000", "0000011", "0101101", "0100110"]

distancia1, detectables1, corregibles1 = ej22.analizar_codigo(codificacion1)
distancia2, detectables2, corregibles2 = ej22.analizar_codigo(codificacion2)
distancia3, detectables3, corregibles3 = ej22.analizar_codigo(codificacion3)

print("Código 1:")
print("Distancia mínima:", distancia1)
print("Errores detectables:", detectables1)
print("Errores corregibles:", corregibles1)

print("\nCódigo 2:")
print("Distancia mínima:", distancia2)
print("Errores detectables:", detectables2)
print("Errores corregibles:", corregibles2)

print("\nCódigo 3:")
print("Distancia mínima:", distancia3)
print("Errores detectables:", detectables3)
print("Errores corregibles:", corregibles3)