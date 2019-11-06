# Alumno: Fran Gálvez. 2º ASIR

import os, sys
import claseNominas  

def main():
    os.system("cls")
    print("Este programa calcula las nóminas de los trabajadores de una empresa sabiendo que el salario mínimo es de 1000 \u20AC.")
    print("Además existen 2 categorías: una a 500 y otra a 250 \u20AC.")
    print("Por hijo se cobra 100 \u20AC (no se le aplican retencioness).\n")
    print("Comisión variable y retenciones.")
    print("--------------------------------")
    print("-> IRPF: 10\u0025 hasta 1499 \u20AC.")
    print("-> IRPF: 14\u0025 hasta 1699 \u20AC.")
    print("-> IRPF: 20\u0025 hasta 1700 \u20AC.")
    
    while True:
        try:
            # Pido los datos del empleado y la nómina
            empleado = str(input("\n\tIntroduce el nombre del empleado: "))
            sueldo = float(input("\n\tIntroduce el sueldo bruto: "))
            if sueldo <= 0:
                print("\n\tEl sueldo no puede ser menor o igual a cero.")
                continue
            hijos = int(input("\n\tIntroduce el número de hijos. Si no tiene, introducir cero: "))
            cat = int(input("\n\tIntroduce la categoría del empleado (1 o 2): "))
            if cat not in range(1, 3):
                print("\n\tEscoge una categoría entre 1 y 2.")
                continue
            comision = int(input("\n\tIntroduce las comisiones. Si no hay, introduce cero: "))
        except ValueError:
            print("\n\tError: tipo de dato incorrecto.")
            continue
        else:
            # Defino variables.
            irpf = 0
            extra_hijos = 100 * hijos
            extra_cat = 500

             # Según la categoría, así aumento el sueldo
            if cat == 2:
                extra_cat = 250

            # Comprobar el IRPF a aplicar
            if sueldo < 1500: irpf = 0.1
            if sueldo >= 1500 and sueldo < 1700: irpf = 0.14 
            if sueldo >= 1700: irpf = 0.2

            # Calculo las retenciones de IRPF
            bruto = sueldo + comision
            irpf *= bruto
            bruto_irpf = bruto - irpf

            # Calculo el sueldo neto
            neto = bruto_irpf + extra_hijos + extra_cat

            # Creo el objeto empleado y nomina
            objeto_empleado = claseNominas.Empleado(empleado, sueldo, hijos, cat)
            objeto_nomina = claseNominas.Nomina(objeto_empleado, neto, irpf, extra_hijos)

            # Imprimo el objeto empleado
            print(objeto_nomina)
            
            
            while True:
                continuar = str(input("\n\t¿Deseas calcular la nómina de otro empleado? (S/N): "))
                if continuar == 'N': 
                    sys.exit()
                    os.system("cls")
                elif continuar == 'S':
                    break
                else:
                    print("Error: escoge una de las opciones dadas")
                    continue
                    
    
if __name__ == "__main__":
    main()