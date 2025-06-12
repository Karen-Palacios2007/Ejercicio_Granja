from animal import Animal

class animalAcuatico(Animal):
    def __init__(self,tipo, edad,sexo):
        super().__init__(self,tipo, edad,sexo)
    def nadar(self):
        print (f"{self._tipo} esta nadando")