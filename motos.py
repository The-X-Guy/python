import os, claseMotos

def main():
    os.system("cls")

    print("Ejercicio de compra de motos.")
    print("-----------------------------")

    # Defino los colores y las marcas de motos disponibles.
    colores_arr = ["verde", "rojo", "azul", "amarillo", "blanco", "negro"]
    marcas_arr= ["Ducati", "Suzuki", "Kawasaki", "BMW", "KTM"]
    
    # Array donde guardo cada objeto de tipo moto y los clientes
    motos = []
    clientes = []

    # Imprimos los arrays.
    print("\nLas marcas disponibles son: ")
    for i in range(0, len(marcas_arr)):
        print("\t-> " + marcas_arr[i])
    print("\nLos colores disponibles son: ")
    for i in range(0, len(colores_arr)):
        print("\t-> " + colores_arr[i])

    while True:
        try:
            cantidad = int(input("\nIntroduce la cantidad de motos a comprar: "))
            if cantidad <= 0:
                print("Error: introduce una cantidad válida.")
                continue
            cont = 0
            for i in range(cantidad):
                print("Introduce los datos de la moto " + str(i+1))
                nombre = str(input("\nIntroduce el nombre del cliente: "))
                marca = str(input("\nIntroduce la marca: "))
                # Compruebo si la marca está disponible
                if marca not in marcas_arr:
                    print("La marca no está disponible, selecciona otra.")
                    continue

                color = str(input("\nSelecciona el color: "))
                # Compruebo si el color está disposible.
                if color not in colores_arr:
                    print("El color no está disponible, selecciona otra.")
                    continue
                clientes.append(nombre)
                motos.append(claseMotos.Motos(marca, color))
                # cont += 1
        except ValueError:
            print("Error: introduce una cantidad, marca y color correctos.")
            continue
        else:
            # Imprimo las motos que se han comprado
            # n es la longitud de uno de los arrays, para imprimir el cliente y la moto comprada
            n = len(clientes)
            for i in range(n):
                print("El nombre de cliente es " + clientes[i])
                print(motos[i])
            break
        
if __name__ == "__main__":
    main()
