#Se importa la clase "Animal" de "animal.py" 
from animal import Animal

class Gallina(Animal):
    def __init__ (self,idAnimal, edad, peso):
        super().__init__(idAnimal, edad, peso)