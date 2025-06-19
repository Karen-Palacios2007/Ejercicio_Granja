from animal import Animal

#Se crea la clase "Corral" con sus atributos
class Corral():
    def __init__(self,id):
        self._id=id
        self.animales=[]
        
# Se agregan metodos de la clase   
    def limpiar(self):
        print (f" El corral {self.id} ha sido limpiado")
    def agregarAnimales(self,animal):
        self.animales.append(animal)    
    def mostrarAnimal(self,animal):
        for animal in self.animales:
            print (f"Animal: {animal}")
    
    