from modules import myModule
from modules import menuModule
import os, sys

def sumarParametros (n1, n2, n3, n4, n5):
    return n1+n2+n3+n4+n5

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
            myModule.pausar()
        else:
            suma = 0;
            for i in range (0, 5):
                suma+= numeros[i]
            print("\n\tLa suma de los cinco números es " + str(suma))
            myModule.pausar()
            return

def sumarNumerosParametro():
    while True:
        os.system("cls")
        print("1. Introducir cinco números y mostrar el resultado de la suma.\n")
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
            myModule.pausar()
        else:
            suma = sumarParametros(n1, n2, n3, n4, n5)
            print("\n\tLa suma de los cinco números es " + str(suma))
            myModule.pausar()
            return

def volumenCilindro():
    while True:
            os.system("cls")
            print("2. Calcular el volumen de un cilindro dados el radio de la base y la altura.\n")
            try:
                radio = int(input("\tIntroduce el radio de la base: "))
                altura = int(input("\tIntroduce la altura: "))
            except ValueError:
                print("\n\tError: introduce números enteros.")
                myModule.pausar()
            else:
                volumen = 3.141692 * radio * radio * altura;
                print("\n\tEl volumen del cilindro es " + str(volumen) + " cm^3.")
                myModule.pausar()
                return
def main():
    while True:
        os.system("cls")
        print("Relación de problemas de Python. Funciones.")
        print("-------------------------------------------\n")
        menu = [
            "0. Salir",
            "1. Introducir cinco números enteros y mostrar el resultado de la suma.",
            "3. Calcular el volumen de un cilindro."
        ]
        menuModule.imprimirMenu(menu)
        try:  
            opcion = int(input("\nIntroduce una opción: "))
            if opcion not in range (0,4):
                print("\nError: introduce un numero entre 0 y 4.")
                myModule.pausar()
                continue
        except ValueError:
            print("\tError: introduce un número.")
            myModule.pausar()
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
    
if __name__ == "__main__":
    main()