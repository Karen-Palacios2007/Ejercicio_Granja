from animal import Animal

class animalAereo(Animal):
    def __init__(self,tipo, edad,sexo):
        super().__init__(self,tipo, edad,sexo)
    def volar(self):
        print (f"{self._tipo} esta volando")