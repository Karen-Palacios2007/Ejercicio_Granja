#Se importa la clase "Animal" de "animal.py" 
from animal import Animal

#Se crea la clase "Corral" con sus atributos
class Corral():
    def __init__(self,_idCorral,capacidad,estado):
        self._idCorral=_idCorral
        self.capacidad=capacidad
        self.estado=estado
# Se agregan metodos de la clase   
    def limpiar(self):
        print (f" El corral {self._idCorral} ha sido limpiado")
    def asignarAnimal(self,animal):
        self.animales.append(animal)    
    def verificarEstado(self,animal):
        pass
    
    