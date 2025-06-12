from animal import Animal

class animalTerrestre(Animal):
    def __init__(self,tipo, edad,sexo):
        super().__init__(self,tipo, edad,sexo)
    def caminar(self):
        print (f"{self._tipo} esta caminando")