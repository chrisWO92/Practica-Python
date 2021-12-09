class Animal:
    def hablar(self):
        pass
    
class Gato(Animal):
    def hablar(self):
        print("Miau")
        
class Perro(Animal):
    def hablar(self):
        print("Guau!")
        
for animal in Perro(), Gato():
    animal.hablar() 