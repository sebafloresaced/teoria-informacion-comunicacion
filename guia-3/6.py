def verifica_no_singular(codigo):
    for i in range(len(codigo)):
        for j in range(1 + i, len(codigo)):
            if codigo[i] == codigo[j]:
                return False
    return True

def verifica_instantaneo(codigo):
    for i in range(len(codigo)):
        for j in range(len(codigo)):
            if i != j and codigo[j].startswith(codigo[i]):
                return False
    return True

# verifica que sea univoco unicamente con orden 2
def verifica_univoco(codigo):
    palabras_generadas = []
    for i in range(len(codigo)):
        for j in range(len(codigo)):
            palabra = codigo[i] + codigo[j]
            if palabra in palabras_generadas:
                return False
            palabras_generadas.append(palabra)
    return True
