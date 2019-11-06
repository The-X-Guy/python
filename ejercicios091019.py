#Ejercicios de Python 10-09-2019
# Alumno: Fran Gálvez. 2º ASIR.

import math, os, sys
from modules import operaciones, listas, menu, varios

#Ejercicio 1
def comprobar1y10():
    while True:
        try:
            os.system("cls")
            print("1.Comprobar si un número está comprendido entre 1 y 10.")
            numero = int(input("\n\tIntroduce un número: "))
        except ValueError:
            print("\n\tError: introduce un número entero.")
            varios.pausar()
            continue
        else:
            if numero in range (0, 11):
                print("\n\tEl numero " + str(numero) + " está comprendido entre 1 y 10.")
            else:
                print("\n\tEl numero " + str(numero) + " no está comprendido entre 1 y 10.")
        varios.pausar()
        return

#Ejercicio 2        
def comprobarNegativo():
    while True:
        try:
            os.system("cls")
            print("2. Comprobar si un numero es positivo o negativo.")
            numero = int(input("\n\tIntroduce un número: "))
        except ValueError:
            print("\n\tError: introduce un número.")
            varios.pausar()
            continue
        else:
            if(operaciones.esNegativo(numero)):
                print("\n\tEl número " + str(numero) + " es negativo.")
            else:  
                print("\n\tEl numero " + str(numero) + " es positivo.")
        varios.pausar()
        return

#Ejercicio 3
def comprobarMayor():
    while True:
        try:
            os.system("cls")
            print("3. Se introducen tres números y se comprueba cuál es el mayor")
            i = 0
            numeros = []
            while i < 3:
                numero = int(input("\n\tIntroduce el número " + str(i+1) +": " ))
                numeros.append(numero)
                i+=1
        except ValueError:
            print("\n\tError: introduce un número.")
            varios.pausar()
            continue
        else:
            salida = operaciones.ordenarMayorMenor(numeros)
            print("\n\tEl número más grande es " + str(salida[0]))
        varios.pausar()
        return

#Ejercicio 4
def ordenarNumeros():
    while True:
        try:
            os.system("cls")
            print("4. Ordenar números de mayor a menor.")
            cantidad_numeros = int(input("\n\tIntroduce la cantidad de números a ordenar: "))
            i = 0
            numeros = []
            while i < cantidad_numeros:
                numero = int(input("\n\tIntroduce el numero " + str(i+1) +": " ))
                numeros.append(numero)
                i+=1
        except ValueError:
            print("\n\tError: introduce un número.")
            varios.pausar()
            continue
        else:
            salida = operaciones.ordenarMayorMenor(numeros)
            print("\n\tLos números ordenados de mayor a menor son: " + str(listas.imprimirLista(numeros)))
        varios.pausar()
        return

#Ejercicio 5
def obtenerCalificacion():
    while True:
        try:
            os.system("cls")
            print("5. Dada una nota numérica, se devulve insuficiente, suficiente, bien, notable o sobresaliente.")
            nota = int(input("\n\tIntroduce una nota: "))
        except ValueError:
            print("\n\tError: introduce un número.")
            varios.pausar()
            continue
        else:
            if nota not in range (0,11):
                print("\n\tError: introduce una nota entre 0 y 10.")
            else:
                calificacion = ""
                if nota < 5:
                    calificacion = "insuficiente."
                elif nota >= 5 and nota < 6:
                    calificacion = "suficiente."
                elif nota >= 6 and nota < 7:
                    calificacion = "bien"
                elif nota >= 7 and nota < 8:
                    calificacion = "notable."
                elif nota >= 9 and nota <= 10:
                    calificacion = "sobresaliente."
                print("\n\tUn " + str(nota) + " es un " + calificacion)
        varios.pausar()
        return

#Ejercicio 6
def imprimirImpares100_200():
    os.system("cls")
    print("6. Imprimir los números impares entre 100 y 200.")
    input("\n\tPresiona intro para ver los números.")
    impares = [101]
    i = 0
    cont = 2
    while impares[len(impares)-1] < 199:
        impares.append(100 + (2*cont-1))
        cont += 1
        i += 1
    print("\n\tLos números impares entre 100 y 200 son: " + str(listas.imprimirLista(impares)))
    varios.pausar()

#Ejercicio 7
def imprimirMultiplos3_1y100():
    os.system("cls")
    print("7. Imprimir los múltiplos de 3 entre 1 y 100.")
    input("\n\tPresiona intro para ver los números.")
    multiplos = [1]
    i = 0
    cont = 1
    while multiplos[len(multiplos)-1] < 99:
        multiplos.append(3*cont)
        cont += 1
        i += 1
    print("\n\tLos múltiplos de 3 entre 1 y 100 son: " + str(listas.imprimirLista(multiplos)))
    varios.pausar()

#Ejercicio 8
def sumaMultiplos5_1y100():
    os.system("cls")
    print("8. Imprimir la suma de los múltiplos de 5 entre 1 y 100.")
    input("\n\tPresiona intro para ver los números.")
    multiplos = [1]
    i = 0
    cont = 1
    suma = 0
    while multiplos[len(multiplos)-1] < 99:
        multiplos.append(5*cont)
        cont += 1
        i += 1
    while i > 0:
        suma += multiplos[i]
        i -= 1
    print("\n\tLa suma de los múltiplos de 5 entre 1 y 100 es: " + str(suma))
    varios.pausar()

#Ejercicio 9
def sumaPares_1y1000():
    os.system("cls")
    print("9. Cacular la suma de todos los pares entre 1 y 1000.")
    input("\n\tPresiona intro para ver los números.")
    pares = [2]
    i = 0
    cont = 1
    suma = 0
    while pares[len(pares)-1] < 999:
        pares.append(2*cont)
        cont += 1
        i += 1
    while i > 0:
        suma += pares[i]
        i -= 1
    print("\n\tLa suma de los pares entre 1 y 100 es: " + str(suma))
    varios.pausar()

#Ejercicio 10
def sumaNumerosTeclado():
    while True:
        try:
            os.system("cls")
            print("10. Calcular la suma de todos los números entre dos números introducidos por teclado.")
            numero1 = int(input("\n\tIntroduce en primer número: "))
            numero2 = int(input("\n\tIntroduce el segundo número: "))
        except ValueError:
            print("\n\tError: introduce un número.")
            varios.pausar()
            continue
        else:
            aux = numero1
            suma = 0
            while aux <= numero2:
                suma += aux
                aux += 1
            print("\n\tLa suma de todos los numeros entre " + str(numero1) + " y " + str(numero2) + " es " + str(suma))
            varios.pausar()
            return

#Ejercicio 11
def calcularParImparBucles():
    while True:
        try:
            os.system("cls")
            print("11. Caclular sin un número es par o impar.")
            numero = int(input("\n\tIntroduce un número: "))
        except ValueError:
            print("Error: introduce un número.")
            varios.pausar()
            continue
        else:
            if operaciones.esPar(numero):
                print("\n\tEl número es par.")
            else:
                print("\n\tEl número es impar.")
            varios.pausar()
            return

#Ejercicio 12
def potenciaBucles():
    while True:
        try:
            os.system("cls")
            print("12. Se calcula la potencia de un número mediante bucles.")
            numero = int(input("\n\tIntroduce un número: "))
            exp = int(input("\n\tIntroduce un exponente: "))
        except ValueError:
            print("\n\tError: introduce números enteros.")
            varios.pausar()
            continue
        else:
            resultado = operaciones.calcularPotenciaBucles(numero, exp)
            print("\n\t" + str(numero) + " elevado a " + str(exp) + " es " + str(resultado))
            varios.pausar()
            return

#Ejercicio 13
def sumarNumeros():
    while True:
        numeros = []
        try:
            os.system("cls")
            print("13. Leer todos los números hasta introducir un cero, y sumarlos.")
            while True:
                numero = int(input("\n\tIntroduce un número: "))
                if numero != 0:
                    numeros.append(numero)
                else:
                    break
        except ValueError:
            print("\n\tError: introduce números enteros.")
            varios.pausar()
            continue
        else:
            suma = 0
            for i in range(0, len(numeros)):
                suma += numeros[i]
                i += 1
            print("\n\tLa suma de todos los números es " + str(suma))
            varios.pausar()
            return

#Ejercicio 14
def mediaNumeros():
    while True:
        numeros = []
        try:
            os.system("cls")
            print("14. Leer todos los números hasta introducir un cero, y calcular su media.")
            while True:
                numero = int(input("\n\tIntroduce un número: "))
                if numero != 0:
                    numeros.append(numero)
                else:
                    break
        except ValueError:
            print("\n\tError: introduce números enteros.")
            varios.pausar()
            continue
        else:
            suma = 0
            for i in range(0, len(numeros)):
                suma += numeros[i]
                i += 1
            media = suma / len(numeros)
            print("\n\tLa media de todos los números es " + str(media))
            varios.pausar()
            return

#Ejercicio 15
def minimoMaximoNumeros():
    while True:
        numeros = []
        try:
            os.system("cls")
            print("15. Leer todos los números hasta introducir un cero, y calcular el máximo y el mínimo.")
            while True:
                numero = int(input("\n\tIntroduce un número: "))
                if numero != 0:
                    numeros.append(numero)
                else:
                    break
        except ValueError:
            print("\n\tError: introduce números enteros.")
            varios.pausar()
            continue
        else:
            resultado = operaciones.ordenarMayorMenor(numeros)
            print("\n\tEl mínimo es " + str(resultado[len(numeros)-1]) + " y el máximo es " + str(resultado[0]))
            varios.pausar()
            return

#Ejercicio 16
def divisionRestasSucesivas():
    while True:
        try:
            os.system("cls")
            print("16. Calcular la división de dos números mediante restas sucesivas.")
            dividendo = int(input("\n\tIntroduce el dividendo: "))
            divisor = int(input("\n\tIntroduce el divisor: "))
        except ValueError:
            print("\n\tError: introduce números enteros.")
            varios.pausar()
            continue
        else:
            if dividendo == 0 and divisor != 0:
                print("\n\t0 entre " + str(divisor) + " es 0.")
            elif dividendo < divisor:
                print("\n\tLa operación no se puede realizar, el dividendo es menor que el divisor.")
            else:
                resultado = operaciones.divisionRestasSucesivas(dividendo, divisor)
                print("\n\t" + str(dividendo) + " entre " + str(divisor) + " es " + str(resultado[0]) + ", y el resto es " + str(resultado[1]))
            varios.pausar()
            return

#Ejercicio 17
def contarNegativosPositivos():
    while True:
        try:
            os.system("cls")
            print("17. Introducir número por teclado, contar positivos y negativos hasta introducir cero, y mostrar resultado.")
            numeros = []
            while True:
                numero = int(input("\n\tIntroduce un número: "))
                if numero != 0:
                    numeros.append(numero)
                else:
                    break
        except ValueError:
            print("\n\tError: introduce números enteros.")
            varios.pausar()
            continue
        else:
            i = 0
            positivos = 0
            negativos = 0
            for i in range(0, len(numeros)):
                if numeros[i] < 0:
                    negativos += 1
                elif numeros[i] > 0:
                    positivos += 1
            print("\n\tSe han introducido " + str(positivos) + " números positivos y " + str(negativos) + " números negativos.")
            varios.pausar()
            return

#Ejercicio 18
def rangoCuadrados():
    while True:  
        try:
            os.system("cls")
            print("18. Calcular el cuadrado de todos los números comprendido entre dos números introducidos.")
            numero1 = int(input("\n\tIntroduce el primer número: "))
            numero2 = int(input("\n\tIntroduce el segundo número: "))
        except ValueError:
            print("\n\tError: introduce un número.")
            varios.pausar()
            continue
        else:
            i = 0
            cuadrados = []
            while numero2 >= numero1:
                cuadrados.append(numero2*numero2)
                numero2 -= 1
            print("\n\tLos cuadrados de los números son " + str(listas.imprimirLista(cuadrados)))
            varios.pausar()
            return

#Ejercicio 19
def multiplicarSumasSucesivas():
     while True:
        try:
            os.system("cls")
            print("19. Calcular la multiplicación de dos números mediante sumas sucesivas.")
            factor1 = int(input("\n\tIntroduce el primer factor: "))
            factor2 = int(input("\n\tIntroduce el segundo factor: "))
        except ValueError:
            print("\n\tError: introduce números enteros.")
            varios.pausar()
            continue
        else:
            resultado = operaciones.multiplicacionSumasSucesivas(factor1, factor2)
            print("\n\t" + str(factor1) + " por " + str(factor2) + " es " + str(resultado))
            varios.pausar()
            return

#Ejercicio 20
def imprimir5_1y20():
    os.system("cls")
    print("20. Imprimir 5 veces los números comprendidos entre 1 y 20 usando dos bucles")
    numeros = []
    i = 0
    j = 0

    #se crea una matriz con los numeros del 1 al 20
    for j in range(1, 21):
            numeros.append(j)
    
    #se convierte la latriz en cadea y se imprime 5 veces.
    for i in range(1, 6):
        print(listas.imprimirLista(numeros))
    varios.pausar()
    return

#Ejercicio 21
def comprobarPrimo():
    while True:
        try:
            os.system("cls")
            print("21. Determinar si un número es primo.")
            numero = int(input("\n\tIntroduce un número entero positivo: "))
            if numero < 0 or numero == 0:
                print("\n\tError: introduce un número.")
                continue
        except ValueError:
            print("\n\tError: introduce un número.")
            varios.pausar()
            continue
        else:
            primo = operaciones.esPrimo(numero)
            if primo:
                print("\n\tEl número es primo.")
            else:
                print("\n\tEl número no es primo.")
            varios.pausar()
            return

#Ejercicio 22
def tablaMultiplicar():
    while True:
        try:
            os.system("cls")
            print("22. Calcular la tabla de multiplicar de un número dado.")
            numero = int(input("\n\tIntroduce un número entre 1 y 10: "))
            if numero < 1 or numero > 10:
                print("\n\tError: introduce un número entre 1 y 10.")
                continue
        except ValueError:
            print("\n\tError: introduce un número.")
            varios.pausar()
            continue
        else:
            i = 0
            for i in range (0, 11):
                print("\t" + str(numero) + " x " + str(i) + " = " + str(numero*i))
            varios.pausar()
            return

#Ejercicio 23
def imprimirFrase():
    while True:
        try:
            os.system("cls")
            print("23. Introducir un número y una frase. La frase se mostrará tantas veces como diga el número.")
            frase = str(input("\n\tIntroduce una frase: "))
            numero = int(input("\n\tIntroduce un numero: "))
            if numero <= 0 or frase == "":
                print("\n\tError: introduce un numero distinto y mayor de cero.")
                continue
        except ValueError:
            print("\n\tError: introduce un número.")
            varios.pausar()
            continue
        else:
            while numero > 0:
                print("\n\t" + frase)
                numero -= 1
            varios.pausar()
            return

#Ejercicio 24
def factorial():
    while True:
        try:
            os.system("cls")
            print("24. Calcular el factorial de un número.")
            numero = int(input("\n\tIntroduce un número: "))
            if numero < 0:
                print("\n\tError: introduce un número mayor o igual a cero.")
                varios.pausar()
                continue
        except ValueError:
            print("\n\tError: introduce un número.")
            varios.pausar()
            continue
        else:
            factorial = operaciones.factorial(numero)
            print("\n\tEl factorial de " + str(numero) + " es " + str(factorial))
            varios.pausar()
            return

#Ejercicio 25
def imprimirPrecios():
    while True:
        try:
            os.system("cls")
            print("""25. Tomando del teclado el precio por unidad de un determinado producto, se pretende
    imprimir un listado con los precios para unidades desde 1 a 100. Se deben aplicar 
    una serie de descuentos, a saber: 10% a partir de 15 unidades, 15% a partir de 30 
    unidades, 20% a partir de 50 unidades.""")
            precio = int(input("\n\tIntroduce un precio: "))
        except ValueError:
            print("\n\tError: introduce un número.")
            varios.pausar()
            continue
        else:
            unidades = 1
            for unidades in range(1, 101):
                if unidades in range(1, 15):
                    print("\n\t" + str(unidades) + " unidades: " + str(precio*unidades) + " euros.")
                    unidades += 1
                if unidades in range(16, 30):
                    print("\n\t" + str(unidades) + " unidades: " + str(precio*unidades-(precio*unidades*0.1)) + " euros.")
                    unidades += 1
                if unidades in range(31, 50):
                    print("\n\t" + str(unidades) + " unidades: " + str(precio*unidades-(precio*unidades*0.15)) + " euros.")
                    unidades += 1
                if unidades in range(51, 101):
                    print("\n\t" + str(unidades) + " unidades: " + str(precio*unidades-(precio*unidades*0.2)) + " euros.")
                    unidades += 1
            varios.pausar()
            return

#Ejercicio 26
def comprobarMultiplo():
    while True:
        try:
            os.system("cls")
            print("26. Comprobar si un número es múltiplo de otro.")
            numero1 = int(input("\n\tIntroduce el primer número: "))
            numero2 = int(input("\n\tIntroduce el segundo número: "))
        except ValueError:
            print("\n\tError: introduce números enteros.")
            varios.pausar()
            continue
        else:
            resultado = operaciones.esMultiplo(numero1, numero2)
            if resultado == []:
                print("\n\tNingún múmero es multiplo del otro.")
                varios.pausar()
                return
            else:
                print("\n\t" + str(resultado[0]) + " es múltiplo de " + str(resultado[1]))
                varios.pausar()
                return

def main():
    while True:
        os.system("cls")
        print("Relación de problemas de Python. Estructuras de control.")
        print("--------------------------------------------------------\n")
        menu_items = [
            "0. Salir.",
            "1. Comprobar si un número esta entre 1 y 10.",
            "2. Comprobar si un número es positivo o negativo.",
            "3. Determinar que número es el mayor.",
            "4. Ordenar números de mayor a menor",
            "5. Dada una nota numérica, se muestra si es un insuficiente, suficiente, ...",
            "6. Imprimir los números impares entre 100 y 200.",
            "7. Imprimir los múltiplos de 3 entre 1 y 100",
            "8. Calcular la suma de los múltiplos de 5 entre 1 y 100.",
            "9. Calcular la suma de todos los pares comprendidos entre 1 y 1000.",
            "10. Calcular la suma de todos los numeros entre dos numeros introducidos.",
            "11. Calcular si un número es par o impar.",
            "12. Calcular la potencia de un número (con bucles)",
            "13. Leer todos los números hasta introducir un cero y sumarlos.", 
            "14. Leer todos los números hasta introducir un cero y hacer la media.",
            "15. Leer todos los números hasta introducir un cero y calcular el máximo y el mínimo.",
            "16. Calcular la división de dos números introducidos mediante restas sucesivas.",
            "17. Introducir número por teclado, contar positivos y negativos hasta introducir cero, y mostrar resultado.",
            "18. Calcular cuadrado de todos los números comprendido entre dos números introducidos.",
            "19. Calcular la multiplicación de dos números mediante sumas sucesivas.",
            "20. Imprimir 5 veces los números comprendidos entre 1 y 20 usando dos bucles",
            "21. Determinar si un número es primo.",
            "22. Calcular la tabla de multiplicar de un número dado.",
            "23. Introducir un número y una frase. La frase se mostrará tantas veces como diga el número.",
            "24. Factorial de un número.",
            "25. A partir de un precio de producto, imprimir precios de unidades con descuento.",
            "26. Calcular si un número es múltiplo de otro."
        ]
        menu.imprimirMenu(menu_items)
        try:
            opcion = int(input("\nSelecciona una opción: "))
            if opcion not in range (0,28):
                print("Error: introduce un numero entre 1 y 27.")
                varios.pausar()
                continue
        except ValueError:
            print("\tError: Introduce un numero.")
            varios.pausar()
        else:
            if opcion == 0:
                os.system("cls")
                sys.exit()
            elif opcion == 1:
                comprobar1y10()
            elif opcion == 2:
                comprobarNegativo()
            elif opcion == 3:
                comprobarMayor()
            elif opcion == 4:
                ordenarNumeros()
            elif opcion == 5:
                obtenerCalificacion()
            elif opcion == 6:
                imprimirImpares100_200()
            elif opcion == 7:
                imprimirMultiplos3_1y100()
            elif opcion == 8:
                sumaMultiplos5_1y100()
            elif opcion == 9:
                sumaPares_1y1000()
            elif opcion == 10:
                sumaNumerosTeclado()
            elif opcion == 11:
                calcularParImparBucles()
            elif opcion == 12:
                potenciaBucles()
            elif opcion == 13:
                sumarNumeros()
            elif opcion == 14:
                mediaNumeros()
            elif opcion == 15:
                minimoMaximoNumeros()
            elif opcion == 16:
                divisionRestasSucesivas()
            elif opcion == 17:
                contarNegativosPositivos()
            elif opcion == 18:
                rangoCuadrados()
            elif opcion == 19:
                multiplicarSumasSucesivas()
            elif opcion == 20:
                imprimir5_1y20()
            elif opcion == 21:
                comprobarPrimo()
            elif opcion == 22: 
                tablaMultiplicar()
            elif opcion == 23:
                imprimirFrase()
            elif opcion == 24:
                factorial()
            elif opcion == 25:
                imprimirPrecios()
            elif opcion == 26:
                comprobarMultiplo()
if __name__ == "__main__":
    main()