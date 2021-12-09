class Persona:
    piernas=2
    
    def __init__(self, nombre):
        self.nombre=nombre
        
    def imprimir(self):
        print("Nombre: {}".format(self.nombre))
        

persona1 = Persona("Cristian")
persona2 = Persona("Ricardo")

persona1.imprimir()
persona2.imprimir()


class Alumno:
    
    piernas = 2
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def __del__(self):
        print("Método delete llamado")
        
    def imprimir(self):
        print("Nombre: {}; Nota: {};".format(self.nombre, self.nota))
        
    def mostrar_estado(self):
        if self.nota >= 4:
            print("regular")
        else:
            print("desaprobado")
    
alumno1 = Alumno("Cristian", 10)
alumno2 = Alumno("Ricardo", 3)

alumno1.imprimir()
alumno2.imprimir()

alumno1.mostrar_estado()
alumno2.mostrar_estado()

print(alumno1.piernas)


class Punto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __del__(self):
        print("Método delete llamado")
        
    def imprimit(self):
        print("({}, {})".format(self.x, self.y))
        
    def imprimir_cuadrante(self):
        
        if self.x > 0 and self.y > 0: print("El punto está en el primer cuadrante")
        elif self.x > 0  and self.y < 0: print("El punto está en el segundo cuadrante")
        elif self.x < 0 and self.y < 0: print("El punto está en el tercer cuadrante")
        elif self.x < 0 and self.y > 0: print("El punto está en el cuarto cuadrante")
        
punto = Punto(10, -30)
punto.imprimit()
punto.imprimir_cuadrante()

        