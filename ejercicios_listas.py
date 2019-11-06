# Ejercicios de listas en Python.
# Fran Gálvez. 2º ASIR.

import os, sys
from modules import menu, listas, varios
from modules.operaciones import generarAleatorios, ordenarMayorMenor
from random import randint

# Ejercicio 1
def cargarNumeros():
    os.system("cls")
    print("1. Cargar 10 números entre el 1 y el 1000 (random).")
    carga = generarAleatorios(10)
    print("\n\t" + listas.imprimirLista(carga))
    varios.pausar()
    return

# Ejercicio 2
def invertirLista():
    os.system("cls")
    print("2. Invertir una lista.")

    carga = generarAleatorios(10)
    print("\n\tLa lista a invertir es: " + listas.imprimirLista(carga))

    carga.reverse()
    print("\n\tY la lista invertida es: " + listas.imprimirLista(carga))

    varios.pausar()
    return

# Ejercicio 3
def posicionesPares():
    os.system("cls")
    print("2. Extraer las posiciones pares de una lista.")

    carga = generarAleatorios(10)
    print("\n\tLa lista a procesar es: " + listas.imprimirLista(carga))

    pares = listas.posicionesPares(carga)
    print("\n\tY las posiciones pares de la lista son: " + listas.imprimirLista(pares))

    varios.pausar()
    return

# Ejercicio 4
def posicionesImpares():
    os.system("cls")
    print("2. Extraer las posiciones impares de una lista.")
    carga = generarAleatorios(10)
    print("\n\tLa lista a procesar es: " + listas.imprimirLista(carga))
    impares = listas.posicionesImpares(carga)
    print("\n\tY las posiciones impares de la lista son: " + listas.imprimirLista(impares))
    varios.pausar()
    return

# Ejercicio 5
def sumarParesImpares():
    os.system("cls")
    print("3. Sumar las posiciones pares e impares de una lista, y decir que resultado es mayor.")
    
    carga = generarAleatorios(10)
    print("\n\tLa lista a procesar es: " + listas.imprimirLista(carga))

    impares = sum(listas.posicionesImpares(carga))
    print("\n\tLa suma de las posiciones impares de la lista es " + str(impares) + ".")

    pares = sum(listas.posicionesPares(carga))
    print("\n\tLa suma de las posiciones pares de la lista es " + str(pares) + ".")

    salida = ("mayor", "menor")[impares > pares]
    print("\n\tLa suma de los pares es " + salida + " que la de los impares.")
    varios.pausar()
    return

# Ejercicio 6
def esMayor():
    os.system("cls")
    print("6. Dada una lista, indicar que elemento es mayor y cual menor.")
    
    carga = generarAleatorios(10)
    print("\n\tLa lista a procesar es: " + listas.imprimirLista(carga))

    ordenados = ordenarMayorMenor(carga)
    print("\n\tEl elemento mayor es " + str(ordenados[0]) + " y el elemento menor es " + str(ordenados[len(ordenados)-1]))

    varios.pausar()
    return

# Ejercicio 8
def sumarListas():
    os.system("cls")
    print("8. Crear 3 listas de 10 posiciones, 2 con números al azar y otro donde guardar los resultados de las sumas de las posiciones.")
    carga1 = generarAleatorios(10)
    carga2 = generarAleatorios(10)

    print("\n\tLa primera lista es: " + listas.imprimirLista(carga1))
    print("\n\tLa segunda lista es: " + listas.imprimirLista(carga2))
    
    suma = listas.sumarPosicionesDosListas(carga1, carga2)
    print("\n\tLa suma de las posiciones de ambas listas es " + listas.imprimirLista(suma))

    varios.pausar()
    return

# Ejercicio 9
def dividirListaParImpar():
    os.system("cls")
    print("9. Crear un array y dividirlo en dos nuevos, uno con las posiciones pares y otro con las impares.")
    carga = generarAleatorios(10)
    print("\n\tLa lista a procesar es: " + listas.imprimirLista(carga))

    pares = listas.posicionesPares(carga)
    impares = listas.posicionesImpares(carga)
    print("\n\tLas posiciones pares son: " + listas.imprimirLista(pares))
    print("\n\tLas posiciones impares son: " + listas.imprimirLista(impares))

    varios.pausar()
    return

# Ejercicios 10 y 11.
def imprimirNombres():
    os.system("cls")
    print("10. Crear una lista con nombres de personas y otro con el sexo, y sacar el nombre de las mujeres.")

    nombres = ["María", "Antonio", "Marta", "Victoria", "Carlos"]
    sexos = ["F", "M", "F", "F", "M"]

    print("\n\tLa lista de nombres es: " + listas.imprimirLista(nombres))
    print("\n\tLa lista de sexos es: " + listas.imprimirLista(sexos))

    mujeres = []
    i = 0
    while i < len(nombres):
        if sexos[i] == "F":
            mujeres.append(nombres[i]) 
        i += 1

    print("\n\tLos nombres de las mujeres son: " + listas.imprimirLista(mujeres))
    varios.pausar()
    return

# Ejercicio 12. En este ejercicio si se introduce un número no da error, debido a que lo
# convierte a cadena sin dar errores. No he podido elevar una excepción para tal caso.
def analisisCadena():
    os.system("cls")
    print("12. Introducir una cadena y sacar el número de vocales y cuántas hay de cada una, el número de consonantes, el número de palabras y la cadena entera en mayúsculas")
    cadena =  str(input("\n\tIntroduce un texto: "))
    print("\n\tError: introduce una cadena.")

    vocales = []
    consonantes = []

    #contadores
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    nbsp = 0
    consonantes = 0
    numeros = 0
    j = 0

    while j < len(cadena):
        if cadena[j] == "a":
            vocales.append(cadena[j])
            a += 1
        elif cadena[j] == "e":
            vocales.append(cadena[j])
            e += 1
        elif cadena[j] == "i":
            vocales.append(cadena[j])
            i += 1
        elif cadena[j] == "o":
            vocales.append(cadena[j])
            o += 1
        elif cadena[j] == "u":
            vocales.append(cadena[j])
            u += 1
        elif cadena[j] == " ":
            nbsp += 1
        elif cadena[j] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            numeros += 1
        else:
            consonantes += 1
        j += 1

    analisis = [
        "El análisis de la cadena es: \n",
        "\tNúmero de 'a': " + str(a),
        "\tNúmero de 'e': " +  str(e),
        "\tNúmero de 'i': " +  str(i),
        "\tNúmero de 'o': " +  str(o),
        "\tNúmero de 'u': " +  str(u),
        "\tCantidad de números: " + str(numeros),
        "\tNúmero de consonantes: " + str(consonantes),
        "\tNúmero de palabras: " + str(nbsp),
        "\tLa cadena en mayúsculas es: " + str(cadena.upper())
    ]
    menu.imprimirMenu(analisis)
    varios.pausar()
    return

# Ejericicio 13
def esCapicua():
    while True:
        try:
            os.system("cls")
            print("14. Dado un número, decir si es capicúa o no.")
            n = int(input("\n\tIntroduce un número: "))
        except ValueError:
            print("\n\tError: introduce un valor válido.")
        else:
            i = 1
            invertido = []
            aux = str(n)
            index = len(aux)
            while i <= len(aux):
                invertido.append(aux[index - i])
                i += 1
            n1 = listas.convertInt(invertido)

            # if n == n[::-1] -> [comienzo::final]
            # Comprobar si el número es igual el número invertido

            # Utilizando tuplas, si la condición es falsa, se devuelve el primer elemento.
            resultado = ("no", "sí")[n == n1]

            print("\n\tEl número " + resultado + " es capicúa.")
            varios.pausar()
            return

        

# Ejercicio 14
def esPalindromo():
    while True:
        try:
            os.system("cls")
            print("14. Dado un núemero,  se dice si es capicúa o no.")
            cadena = str(input("\n\tIntroduce una cadena: "))
        except ValueError:
            print("\n\tError: introduce un valor válido.")
        else:
            i = 1
            invertido = []
            index = len(cadena)
            while i <= len(cadena):
                invertido += cadena[index - i]
                i += 1
            invertido = ''.join(invertido)
            resultado = ("no", "sí")[cadena == invertido]
            print("\n\tLa cadena " + resultado + " es capicúa.")
            varios.pausar()
            return

# def separarLetras():
#     os.system("cls")
#     print("13. Dada una cadena, introducir las consonantes en una lista, las vocales en otra, y unir ambas en una nueva lista que tenga primero las consonantes y luego las vocales.")
         
def main():
    while True:
        os.system("cls")
        print("Relación de problemas de Python. Listas.")
        print("----------------------------------------\n")
        menu_items = [
            "0. Salir.",
            "1. Cargar 10 números entre el 1 y el 1000 (random).",
            "2. Sacar dicha lista de forma inversa",
            "3. Imprimir las posiciones impares.",
            "4. Imprimir las posiciones impares",
            "5. Sumar el contenido de las posiciones pares e impares, y decir cuál es mayor", 
            "6. Indicar los elementos mayor y menor de una lista.",
            "8. Crear 3 listas de 10 posiciones, 2 con números al azar y otro donde guardar los resultados de las sumas de las posiciones.",
            "9. Crear un array y dividirlo en dos nuevos, uno con las posiciones pares y otro con las impares.",
            "10-11. Crear una lista con nombres de personas y otro con el sexo, guardarlos en una lista e imprimirlo por pantalla.",
            "12. Introducir una cadena y realizar un análisis de la misma ...",
            "13. Introducir una número y comprobar si es capicúa.",
            "14. Introducir una cadena y comprobar si es palíndromo."
        ]
        try:
            menu.imprimirMenu(menu_items)
            opcion = int(input("\nSelecciona una opcion: "))
            if opcion not in range (0, 16) or opcion == 7:
                print("Error: introduce una opcion entre 0 y 15 (excluyendo el 7).")
                varios.pausar()
                continue
        except ValueError:
            print("\nError: introduce un numero.")
            varios.pausar()
        else:
            if opcion == 0:
                os.system("cls")
                sys.exit()
            elif opcion == 1:
                cargarNumeros()
            elif opcion == 2:
                invertirLista()
            elif opcion == 3:
                posicionesPares()
            elif opcion == 4:
                posicionesImpares()
            elif opcion == 5:
                sumarParesImpares()
            elif opcion == 6:
                esMayor()
            elif opcion == 8:
                sumarListas()
            elif opcion == 9:
                dividirListaParImpar()
            elif opcion == 10:
                imprimirNombres()
            elif opcion == 11:
                imprimirNombres()
            elif opcion == 12:
                analisisCadena()
            elif opcion == 13:
                esCapicua()
            elif opcion == 14:
                esPalindromo()

#Se comprueba si es script está en ejecución.
if __name__ == "__main__":
    main()