from animal import Animal
class corral():
    def __init__(self,id):
        self.id=id
        self.animales=[]
    
    def limpiar(self):
        print (f" El corral {self.numero} ha sido limpiado")
    def agregarAnimales(self,animal):
        self.animales.append(animal)    
    def mostrarAnimal(self,animal):
        for animal in self.animales:
            print (f"Animal: {animal}")
