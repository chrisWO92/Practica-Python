from banco_cliente import *
from getter_setter import *
from herencia import *

def main():
    
    banco = Banco()
    banco.operar()
    banco.depositos_totales()
    
    auto1 = Auto("Negro", 4, 180)
    auto2 = Auto("Rojo", 6, 180)

    print(auto1)
    print(auto2)
    
    bebidas = ListadoBebidas()
    print(bebidas.bebida)

    bebidas.bebida = 'Manzana'
    print(bebidas.bebida)
    
    perro1 = Perro("Orión", 20)
    print(perro1.nombre)
    perro1.nombre = "Canela"
    print(perro1.nombre)
    

if __name__ == "__main__":
    main()