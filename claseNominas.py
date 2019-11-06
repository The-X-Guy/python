class Empleado:
    def __init__ (self, nombre, sueldo, hijos, cat):
        self.nombre = nombre
        self.sueldo = sueldo
        self.hijos = hijos
        self.cat = cat  

class Nomina:
    def __init__ (self, empleado, neto, irpf, extra_hijos):
        self.nombre = empleado.nombre
        self.sueldo = empleado.sueldo
        self.hijos = empleado.hijos
        self.categoria = empleado.cat
        self.irpf = irpf
        self.neto = neto
        self.extra_hijos = extra_hijos

    def __str__ (self):
        return """\nLos datos de la nómina son:
            \n\tNombre: """+ str(self.nombre) + """
            \n\tSueldo bruto: """ + str(self.sueldo) + """
            \n\tNumero de hijos: """ + str(self.hijos) + """
            \n\tCategoría: """ + str(self.categoria) + """
            \n\tRetenciones: """ + str(self.irpf) + """
            \n\tCuantía extra por hijos: """ + str(self.extra_hijos) + """
            \n\tSueldo neto: """ + str(self.neto)
            