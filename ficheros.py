import os

def main():
    if os.path.exists("mujeres.dat"):
        os.remove("mujeres.dat")
    hombres = []
    nombres = open("nombres.dat", "r")
    mujeres = open("mujeres.dat", "x")
    # print(nombres.read())

    for line in nombres:
        if "mujer" in line:
            mujeres.write(line)
        else:
            hombres.append(line)
    
    print("Nombres de hombre: ")
    for i in hombres:
        print(i)

    mujeres = open("mujeres.dat", "r")
    print("Nombres de mujer: ")
    for i in mujeres:
        print(i)
    
    nombres.close()
    mujeres.close()

if __name__ == "__main__":
    main()