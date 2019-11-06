class Motos:
    def __init__ (self, marca, color):
        self.marca = marca
        self.color = color
    
    def __str__ (self):
        return "\n\t-> Marca: " + self.marca + "\n\t-> Color: " + self.color