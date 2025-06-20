#Se importa la clase "Animal" de "animal.py" 
from animal import Animal

# Se Crea la clase "Gallina" con atributos heredados de la super clase "Animal"
class Gallina(Animal):
    def __init__ (self,idAnimal, edad, peso):
        super().__init__(idAnimal, edad, peso)
        
# Se agregan metodos propios de la clase      
    def recolectarHuevos(self):
        print (f"Recolectando huevos de la gallina {self.idAnimal}")