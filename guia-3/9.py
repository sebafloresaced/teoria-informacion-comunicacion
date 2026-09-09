def obtener_alfabeto_codigo(codigo):
    alfabeto = []
    for palabra in codigo:
        for caracter in palabra:
            if caracter not in alfabeto:
                alfabeto.append(caracter)
    return alfabeto

def obtener_longitudes(codigo):
    return [len(palabra) for palabra in codigo]

def calcula_kraft(codigo):
    suma = 0
    longitudes = obtener_longitudes(codigo)
    alfabeto = obtener_alfabeto_codigo(codigo)
    r = len(alfabeto)
    for longitud in longitudes:
        suma += r ** (-longitud)
    return suma