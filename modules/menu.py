# Librería que coniene métodos referentes a la creación de menús.

# Alumno: Fran Gálvez. 2º ASIR.

# imprimirMenu -> dada una matriz de elementos, los imprime en forma de menú.

def imprimirMenu(menu):
    for i in range(len(menu)):
        print("\t" + menu[i])