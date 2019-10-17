import math

def imprimirArray (array):
    cadena = "\n\t"
    for i in range(0, len(array) - 3):
        cadena += str(array[i]) + ", "
    cadena += "" + str(array[len(array) - 2])
    cadena += " y " + str(array[len(array) - 1])
    return cadena

def pausar():
    input("\n\tPulse intro para continuar...\n")
    # se pausa la ejecucion del programa.

def esNegativo(numero):
    if numero < 0:
        return True
    else:
        return False

def ordenarMayorMenor(numeros):
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