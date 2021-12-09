class cliente:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0
        
    def depositar(self, monto):
        self.monto = self.monto + monto
        
    def extraer(self, monto):
        self.monto = self.monto - monto
        
    def retornar_monto(self):
        return self.monto
    
    def imprimir(self):
        print("{} tiene depositados {}".format(self.nombre, self.monto))
        

class Banco:
    
    def __init__(self):
        self.cliente1 = cliente("Juan")
        self.cliente2 = cliente("Cesar")
        self.cliente3 = cliente("Francisco")
        
    def operar(self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(500)
        self.cliente3.depositar(100)
        self.cliente2.depositar(1000)
        self.cliente1.extraer(100)
        
    def depositos_totales(self):
        total = self.cliente1.retornar_monto() + self.cliente2.retornar_monto() + self.cliente3.retornar_monto()
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()
        print("El total es de {}".format(total))
    

    
        
        
        