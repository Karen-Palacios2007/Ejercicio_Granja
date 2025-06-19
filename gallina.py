#Se importa la clase "Animal" del archivo "animal"
from animal import Animal

# Se Crea la clase "Cerdo" con sus atributos, aplicando la herencia de la clase "Animal"
class Gallina(Animal):
    def __init__(self, tipo, edad, sexo):
        super().__init__(tipo, edad, sexo)
