#Se importa la clase "Empleado" de "empleao.py" 
from empleado import Empleado

# Se Crea la clase "empleadoAlimnetación" con atributos heredados de la super clase "Empleado"
class empleadoAlimnetación(Empleado):
    def __init__(self,idEmpleado,nombre,cargo,tipoAlimento):
        super().__init__(idEmpleado,nombre,cargo)
        self.tipoAlimento=tipoAlimento

# Se agregan metodos propios de la clase     
    def registrarAlimentación(self):
        print (f"{self._nombre} esta alimentanddo a los animales \n")     
        self.tipoAlimento=input("Tipo de alimento que le proporcionara al animal: ")
        self.cantAlimento=input("Cantidad del alimento a proporcionar: ")
        print (f"{self._nombre} esta alimentando...")