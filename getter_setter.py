class ListadoBebidas():
    def __init__(self):
         self.__bebida = 'Naranja'
         self.__bebidas_validas = ['Naranja','Manzana']
         
    @property
    def bebida(self):
        return "La bebida oficial es: {}".format(self.__bebida)
    
    @bebida.setter
    def bebida(self, bebida):
        self.__bebida = bebida
        



class Perro:
    def __init__(self, nombre, peso):
        self.__nombre = nombre
        self.__peso = peso
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        


         