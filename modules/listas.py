# Librería que contiene métodos para aplicar sobre listas.

# Alumno: Fran Gálvez. 2º ASIR.

# convertInt -> Dada una lista de enteros, se convierten en un único número.
# isList -> comprueba si un objeto es una lista. Si no lo es, lo convierte en una lista y lo devuelve.
# imprimirLista -> imprima una lista de la forma elemento1, elemento2, ... y elementoN.
# posicionesPares -> extrae y devuelve las posiciones pares de una lista (generador).
# posicionesImpares -> extrae y devuelve las posiciones imapres de una lista (generador).
# sumasElementosLista -> suma todos los elementos de una lista.
# sumarPosicionesDosListas -> dada dos listas, suma sus posiciones y las devuelve (generador). 

def convertInt(lista):
    # lista = isList(lista)
    salida = int(''.join(map(str, lista)))
    return salida

def isList (lista):
    if type(lista) is list:
        return lista
    else: 
        return list(lista)

def imprimirLista (lista):
    lista = isList(lista)
    cadena = ""
    for i in range(0, len(lista) - 2):
        cadena += str(lista[i]) + ", "
    cadena += "" + str(lista[len(lista) - 2])
    cadena += (" y " + str(lista[len(lista) - 1]) + ".")
    return cadena

def posicionesPares (lista):
    lista = isList(lista)
    i = 1
    while i < len(lista):
        yield(lista[i])
        i += 2

def posicionesImpares (lista):
    lista = isList(lista)
    i = 0
    while i < len(lista):
        yield(lista[i])
        i += 2

def sumarElementosLista (lista):
    lista = isList(lista)
    suma = 0
    for i in lista:
        suma += lista
    return suma

def sumarPosicionesDosListas(lista1, lista2):
    lista1 = isList(lista1)
    lista2 = isList(lista2)
    if len(lista1) != len(lista2):
        raise Exception("Ambas listas deben tener la misma longitud para ser sumadas.")
    i = 0
    while i < len(lista1):
        yield(lista1[i] + lista2[i])
        i += 1