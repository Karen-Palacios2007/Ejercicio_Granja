# Se Crea la clase "Cerdo" con sus atributos
class Animal:
    def __init__(self,idAnimal, edad, peso):
        self.idAnimal=idAnimal
        self.edad=edad
        self.peso=peso

# Se agregan metodos de la clase
    def alimentar(self):
        print (f"{self.tipo} ha sido alimentado")
    def vacunar(self):
        print (f"{self.tipo} ha sido vacunado")
    def registrarPeso(self):
        print (f"{self.tipo}: {self.peso} kg")
        
# Se retornan los datos haciendo uso de "get_"    
    def get_tipo(self):
        return self.tipo
    def get_edad(self):
        return self.edad
    def get_sexo(self):
        return self.sexo
    
# Se reciben los datos retornados haciendo uso de "set_"
    def set_tipo(self,tipoAnimal):
        self.tipo=tipoAnimal
    def set_edad(self,tipoAnimal):
        self.tipo=tipoAnimal
    def get_sexo(self,tipoAnimal):
        self.sexo=tipoAnimal
    

