class Vehiculo:
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return "Color: {} ; Ruedas: {}.".format(self.color, self.ruedas)
    
class Auto(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        
    def __str__(self):
        return super().__str__() + " ; Velocidad: " + str(self.velocidad)
    
    

    
    