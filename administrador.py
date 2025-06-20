#Se importa la clase "Empleado" de "empleado.py" 
from empleado import Empleado

# Se Crea la clase "Administrador" con atributos heredados de la super clase "Empleado"
class Administrador(Empleado):
    def __init__ (self,idEmpleado,nombre,cargo):
        super().__init__(idEmpleado,nombre,cargo)
    
    def supervisarCorrales(self):
        pass
    def registrarAsistencias(self):
        pass
    def generarReportes(self):
        pass