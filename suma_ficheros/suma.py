# Alumno: Fran Gálvez. 2º ASIR
import os

def main():
    if os.path.exists("nombres.dat"):
        os.remove("nombres.dat")

    mujeres = open("mujeres.dat", "r")
    hombres = open("hombres.dat", "r")
    nombres = open("nombres.dat", "a")

    for line in mujeres:
        nombres.write(line)
    for line in hombres:
        nombres.write(line)
    
    nombres = open("nombres.dat", "r")
    nombres_arr = []
    for i in nombres:
        nombres_arr.append(i)

    for i in range(len(nombres_arr) - 2):
        aux = ""
        if nombres_arr[i] > nombres_arr[i+1]:
            aux = nombres_arr[i]
            nombres_arr[i] = nombres_arr[i+1]
        nombres_arr[i+1] = nombres_arr[i]

    nombres = open("nombres.dat", "a")
    for i in range(len(nombres_arr) - 1):
        nombres.write(nombres_arr[0])
    
    nombres.close()
    hombres.close()
    mujeres.close()

if __name__ == "__main__":
    main()