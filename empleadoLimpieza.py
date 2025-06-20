#Se importa la clase "Empleado" de "empleao.py" 
from empleado import Empleado

# Se Crea la clase "empleadoLimpieza" con atributos heredados de la super clase "Empleado"
class empleadoLimpieza(Empleado):
    def __init__(self,idEmpleado,nombre,cargo):
        super().__init__(idEmpleado,nombre,cargo)