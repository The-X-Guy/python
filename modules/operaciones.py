# Librería que contiene métodos referentes a operaciones matemáticas.

# Alumno: Fran Gálvez. 2º ASIR.

# generarAleatorios -> dado un parametro, genera N numeros aleatorios entre 0 y 100 y los devuleve en una lista.
# esNegativo -> verifica si un número es negativo o no.
# ordearMayorMenor -> ordena una serie de números contenidos en una lista de mayor a menor.
# esPar -> verifica si un número es par o no.
# calcularPotenciaBucles -> calcula la potencia de un número usando bucles-
# divisionRestasSucesivas -> calcula la división de dos números mediante restas sucesivas.
# multiplicacionSumasSucesivas -> calcula el producto de dos números mediante sumas sucesivas.
# esPrimo -> verifica si un número es primo o no.
# factorial -> calcula el factorial de un número.
# esMultiplo -> verrifica si un número es múltiplo de otro.

import math
from random import randint

def generarAleatorios(n):
    numeros = []
    for i in range (0, n):
        numeros.append(randint(0, 1000))
    return numeros

def esNegativo(numero):
    if numero < 0:
        return True
    else:
        return False

def ordenarMayorMenor(numeros):
    numeros = list(numeros)
    aux = 0
    i = 0
    while i < len(numeros):
        j = i+1
        while j < len(numeros):
            if numeros[j] > numeros[i]:
                aux = numeros[i]
                numeros[i] = numeros[j]
                numeros[j] = aux
            j+=1
        i+=1
    return numeros

def esPar (numero):
    if numero % 2 == 0:
        return True
    else :
        return False

def calcularPotenciaBucles(numero, exp):
    resultado = numero
    while exp > 1:
        resultado *= numero
        exp -= 1
    return resultado

def divisionRestasSucesivas(dividendo, divisor):
    resultado = [0, 0] # resultado[0] es el cociente y resultado[1] el resto.
    while dividendo >= divisor:
        dividendo -= divisor
        resultado[0] += 1
    resultado[1] = dividendo
    return resultado

def multiplicacionSumasSucesivas(factor1, factor2):
    resultado = 0
    while factor2 > 0:
        resultado += factor1
        factor2-= 1
    return resultado

def esPrimo(numero):
    cont = 2
    while cont < numero:
        if numero%cont == 0: # Si el resultado es cero, el número no tiene más divisores que el mismo y la unidad.
            return False
        cont += 1
    return True

def factorial(numero):
    fact = 1
    for i in range (1, numero + 1):
        fact *= i
    return fact

def esMultiplo(numero1, numero2):
    if numero1%numero2 == 0:
        return [numero1, numero2]
    elif numero2%numero1 == 0:
        return [numero2, numero1]
    else:
        return []