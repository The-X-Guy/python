# Ejercicio de Python 16-10-2019
# Alumno: Fran Gálvez. 2º ASIR.

from modules import listas, numeros, varios, menu
import os, sys

def sumarParametros (n1, n2, n3, n4, n5):
    return n1+n2+n3+n4+n5

# Ejercicio 1
def sumarNumeros():
    while True:
        os.system("cls")
        print("1. Introducir cinco números y mostrar el resultado de la suma.\n")
        numeros = []
        i = 0
        try:
            while i < 5:
                numeros.append(int(input("\tIntroduce el número " + str((i+1)) + ": ")))
                i += 1
        except ValueError:
            print("\nError: introduce un número entero.")
            varios.pausar()
        else:
            suma = 0;
            for i in range (0, 5):
                suma+= numeros[i]
            print("\n\tLa suma de los cinco números es " + str(suma))
            varios.pausar()
            return

# Ejercicio 2
def sumarNumerosParametro():
    while True:
        os.system("cls")
        print("2. Introducir cinco números y mostrar el resultado de la suma.\n")
        numeros = []
        i = 0
        try:
            n1 = int(input("\tIntroduce el primer número: "))
            n2 = int(input("\tIntroduce el segundo número: "))
            n3 = int(input("\tIntroduce el tercer número: "))
            n4 = int(input("\tIntroduce el cuarto número: "))
            n5 = int(input("\tIntroduce el quinto número: "))
        except ValueError:
            print("\nError: introduce un número entero.")
            varios.pausar()
        else:
            suma = sumarParametros(n1, n2, n3, n4, n5)
            print("\n\tLa suma de los cinco números es " + str(suma))
            varios.pausar()
            return

# Ejercicio 3
def volumenCilindro():
    while True:
            os.system("cls")
            print("2. Calcular el volumen de un cilindro dados el radio de la base y la altura.\n")
            try:
                radio = int(input("\tIntroduce el radio de la base: "))
                altura = int(input("\tIntroduce la altura: "))
            except ValueError:
                print("\n\tError: introduce números enteros.")
                varios.pausar()
            else:
                volumen = 3.141692 * radio * radio * altura;
                print("\n\tEl volumen del cilindro es " + str(volumen) + " cm^3.")
                varios.pausar()
                return

def main():
    while True:
        os.system("cls")
        print("Relación de problemas de Python. Funciones.")
        print("-------------------------------------------\n")
        menu_items = [
            "0. Salir",
            "1. Introducir cinco números enteros y mostrar el resultado de la suma.",
            "2. Introduce cinco números como parámetros y se calcula su suma",
            "3. Calcular el volumen de un cilindro."
        ]
        menu.imprimirMenu(menu_items)
        try:  
            opcion = int(input("\nIntroduce una opción: "))
            if opcion not in range (0,4):
                print("\nError: introduce un numero entre 0 y 3.")
                varios.pausar()
                continue
        except ValueError:
            print("\tError: introduce un número.")
            varios.pausar()
        else:
            if opcion == 0:
                os.system("cls")
                sys.exit()
            elif opcion == 1:
                sumarNumeros()
            elif opcion == 2:
                sumarNumerosParametro()
            elif opcion == 3:
                volumenCilindro()

# Se comprueba si el script está en ejecución.  
if __name__ == "__main__":
    main()