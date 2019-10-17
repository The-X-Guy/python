import os, sys
from modules import menuModule
from modules import myModule
import math

def eulerLeibniz():
    os.system("cls")
    print("1. Calcular el número e mediante las series de Leibniz.")
    input("\n\tPulse intro para calcular...")
    cont = 1
    e = 0
    while cont < 10000:
        e = (1 + 1/cont)**cont
        cont += 1
    print("\n\tEl valor aproximado del número e es " + str(e) + ".")
    myModule.pausar()

# Este ejercicio me da un resultado que parece sererróneo. 
# He aplicado la fórmula proporcionada en clase.
def eulerFactorial():
    os.system("cls")
    print("2. Calcular el número e mediante factoriales.")
    input("\n\tPulse intro para calcular...")
    cont = 1
    e = 0
    while cont <= 10:
        e += 1 / myModule.factorial(cont)
        cont += 1
    print("\n\tEl valor aproximado del número e es " + str(e) + ".")
    myModule.pausar()

def piSumatorio():
    os.system("cls")
    print("\n\t3. Calcular el número Pi.")
    input("\n\tPulsa intro para calcular...")
    cont = 0
    pi = 0
    while cont < 100000:
        pi += ((-1)**cont)/(2 * cont + 1)
        cont += 1
    print("\n\tEl valor aproximado del número Pi es " + str(4*pi) + ".")
    myModule.pausar()

def ecuacionSegundoGrado():
    while True:
        os.system("cls")
        print("4. Calcular las soluciones de una ecuación de segundo grado.")
        try:
            a = int(input("\n\tIntroduce el primer término: "))
            b = int(input("\n\tIntroduce el segundo término: "))
            c = int(input("\n\tIntroduce el tercer término: "))
        except ValueError:
            print("\n\tError: introduce números enteros.")
            continue
        else:
            if c < 0:
                ecuacion = str(a) + "x^2 + " + str(b) + "x " + str(c) + " = 0"
            else:
                ecuacion = str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0"

            discriminante = b*b - 4*a*c
            if discriminante < 0:
                print("\n\tLa ecuación " + ecuacion + " tiene soluciones complejas.")
            elif discriminante == 0:
                x = (-b + math.sqrt(discriminante))/(2*a)
                print("\n\tLa ecuación " + ecuacion + " tiene solución única: \n\tx = " + str(x))
            elif discriminante > 0:
                x1 = (-b + math.sqrt(discriminante))/(2*a)
                x2 = (-b - math.sqrt(discriminante))/(2*a)
                print("\n\tLa ecuación " + ecuacion + " tiene dos soluciones: \n\t\tx1 = " + str(x1) + "\n\t\tx2 = " + str(x2))
            myModule.pausar()
            return


def main():
    while True:
        try:
            os.system("cls")
            print("Ejercicios de Python. Números Pi y Euler.")
            print("-----------------------------------------\n")
            menu = [
                "0. Salir.",
                "1. Calcular el número e mediante las series de Leibniz.",
                "2. Calcular el número e mediante factoriales.",
                "3. Calcular el número Pi.",
                "4. Calcular ecuación segundo grado."
            ]
            menuModule.imprimirMenu(menu)
            opcion = int(input("\n\tEscoge una opción: "))
        except ValueError:
            print("\n\tError: introduce un número.")
        else:
            if opcion not in range(0, 5):
                print("\n\tError: introduce un número entre 0 y 3.")
                continue
            else:
                if opcion == 0:
                    os.system("cls")
                    sys.exit()
                elif opcion == 1:
                    eulerLeibniz()
                elif opcion == 2:
                    eulerFactorial()
                elif opcion == 3:
                    piSumatorio()
                elif opcion == 4:
                    ecuacionSegundoGrado()



if __name__ == "__main__":
    main()