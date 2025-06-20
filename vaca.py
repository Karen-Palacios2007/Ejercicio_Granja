#Se importa la clase "Animal" de "animal.py" 
from animal import Animal

# Se Crea la clase "Vaca" con atributos heredados de la super clase "Animal"
class Vaca(Animal):
    def __init__ (self,idAnimal, edad, peso):
        super().__init__(idAnimal, edad, peso)

# Se agregan metodos propios de la clase         
    def ordeñar(self):
        print (f"Se esta ordeñanddo a la vaca {self.idAnimal}")
        