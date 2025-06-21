#Se importa la clase "Empleado" de "empleao.py" 
from empleado import Empleado

# Se Crea la clase "empleadoSanidad" con atributos heredados de la super clase "Empleado"
class empleadoSanidad(Empleado):
    def __init__(self,idEmpleado,nombre,cargo,especialidad):
        super().__init__(idEmpleado,nombre,cargo)
        self.especialidad=especialidad
        
# Se agregan metodos de la clase
    def aplicarVacuna(self):
        pass
    
    def realizarChequeo(self):
        pass
