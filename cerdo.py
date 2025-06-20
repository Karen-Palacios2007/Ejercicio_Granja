#Se importa la clase "Animal" de "animal.py" 
from animal import Animal

# Se Crea la clase "Cerdo" con atributos heredados de la super clase "Animal"
class Cerdo(Animal):
    def __init__ (self,idAnimal, edad, peso):
        super().__init__(idAnimal, edad, peso)

# Se agregan metodos propios de la clase      
    def controlPeso(self):
        print (f"Controlando peso del cerdo {self.idAnimal}")