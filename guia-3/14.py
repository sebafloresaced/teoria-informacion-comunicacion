def obtener_alfabeto_codigo(codigo):
    alfabeto = []
    for palabra in codigo:
        for caracter in palabra:
            if caracter not in alfabeto:
                alfabeto.append(caracter)
    return alfabeto

def obtener_longitudes(codigo):
    return [len(palabra) for palabra in codigo]

def verificar_compacta(codigo, probabilidades):
    alfabeto = obtener_alfabeto_codigo(codigo)
    longitudes = obtener_longitudes(codigo)
    r = len(alfabeto)
    for i in range(len(longitudes)):
        if probabilidades[i] != r ** (-longitudes[i]):
            return False
    return True