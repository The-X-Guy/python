# Alumno: Fran Gálvez. 2º ASIR.
# Ejercicio de calculadora en Python.

# Importo las librerías necesarias.
import sys, os
from claseCalc import Alumno
from modules.menu import imprimirMenu
from modules.varios import pausar

# Defino una lista donde guardar los objetos alumnos y su identificador
alumnos = []

# Función para crear un alumno.
def nuevoAlumno():
    os.system("cls")
    while True:
        # Pido el nombre del alumno.
        nombre = str(input("Introduce el nombre del alumno a crear: "))
        
        # Compruebo si el alumno existe.
        exist = checkIfExists(nombre)
        if exist:
            print("Error: el alumno ya existe.")
            pausar()
            break
        # Si el alumno no existe, creo el objeto y lo almaceno.
        else:
            alumnos.append(Alumno(nombre))
            print("Alumno creado correctamente.")
            pausar()
        break

# Función para comprobar si un alumno existe o no.
def checkIfExists(nombre):
    for i in alumnos:
        if i.nombre == nombre:
            return True
        else:
            return False

# Función para realizar las operaciones del alumno.
def operaciones(alumno):
    os.system("cls")
    # Trabajando con el alumno seleccionado.
    while True:

        # Creo el menú y lo imprimo.
        print("Introduce la operación a realizar: ")
        menu_items = [
            "1. Suma",
            "2. Resta.",
            "3. Multiplicación.",
            "4. División."
        ]
        imprimirMenu(menu_items)

        # Seleccion que operación quiere realizar el alumno.
        opcion = int(input("Introduce una opcion:"))
        if opcion < 1 or opcion > 4:
            print("Error: escoge una opcion entre 1 y 4.")
            pausar()
            continue
        else:
            # Pido los datos y realizao la operación
            n1 = int(input("Introduce el primer numero: "))
            n2 = int(input("Introduce el segundo numero: "))
            if opcion == 1:
                print(alumno.nombre + ": " + str(alumno.suma(n1, n2)))
                pausar()
            if opcion == 2:
                print(alumno.nombre + ": " + str(alumno.diferencia(n1, n2)))
                pausar()
            if opcion == 3:
                print(alumno.nombre + ": " + str(alumno.producto(n1, n2)))
                pausar()
            if opcion == 4:
                if n2 == 0:
                    print("Error: no se puede dividir entre cero.")
                    pausar()
                else:
                    print(alumno.nombre + ": " + str(alumno.cociente(n1, n2)))
                    pausar()
        break

def trabajar():
    os.system("cls")
    while True:
        # Pido el nombre del alumno con el que trabajar.
        nombre = str(input("Introduce tu nombre: "))

        # Compruebo si el alumno existe, y si existe, busco el objeto
        if checkIfExists(nombre):
            # Cojo el objeto para trabajar con él.
            objeto = getAlumno(nombre)
            operaciones(objeto)
            break
        # Si el alumno no existe, lo indico al usuario.
        else:
            print("Error: el alumno no existe.")
            pausar()
            break
# Obtener el objeto alumno.
def getAlumno(nombre):
    for i in alumnos:
        if i.nombre == nombre:
            return i

def main():
    while True:
        os.system("cls")
        print("Programa de calculadora.")
        print("------------------------")
        menu_items = [
            "0. Salir",
            "1. Añadir alumno.",
            "2. Trabajar con alumno existente."
        ]
        imprimirMenu(menu_items)
        try:
            opcion = int(input("Introduce una opcion: "))
        except ValueError:
            print("Error: introduce una opción válida.")
            pausar()
        else:
            if opcion < 0 or opcion > 3:
                print("Error: escoge una opcion entre 0 y 3.")
                pausar()
                continue
            else:
                if opcion == 0:
                    sys.exit()
                elif opcion == 1:
                    nuevoAlumno()
                elif opcion == 2:
                    trabajar()

if __name__ == "__main__":
    main()
