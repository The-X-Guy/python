import os, sys, math
while True:
    os.system("cls")
    print("Calcular las soluciones de una ecuación de segundo grado.")
    print("---------------------------------------------------------")
    try:
        a = int(input("\n\tIntroduce el primer término: "))
        b = int(input("\n\tIntroduce el segundo término: "))
        c = int(input("\n\tIntroduce el tercer término: "))
        d = 1/a # Fuerzo la excepción ZeroDivisionError si a = 0
    except ValueError:
        print("\n\tError: introduce números enteros.")
        input("\n\tPulse intro para continuar...\n")
        continue
    except ZeroDivisionError:
        print("\n\tError: no se puede dividir entre cero (a <> 0).")
        input("\n\tPulse intro para continuar...\n")
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
        break