class Alumno:
    def __init__ (self, nombre):
        self.nombre = nombre
    
    def suma(self, n1, n2):
        self.suma = str(n1) + " + " +  str(n2) + " = " + str(n1+n2)
        return self.suma

    def diferencia(self, n1, n2):
        self.diferencia = str(n1) + " - " + str(n2) + " = " + str(n1-n2)
        return self.diferencia

    def producto(self, n1, n2):
        self.producto = str(n1) + " * " + str(n2) + " = " + str(n1*n2)
        return self.producto

    def cociente(self, n1, n2):
        self.cociente = str(n1) + " / " + str(n2) + " = " + str(n1/n2)
        return self.cociente