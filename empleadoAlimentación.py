#Se importa la clase "Empleado" de "empleao.py" 
from empleado import Empleado

# Se Crea la clase "empleadoAlimnetación" con atributos heredados de la super clase "Empleado"
class empleadoAlimnetación(Empleado):
    def __init__(self,idEmpleado,nombre,cargo):
        super().__init__(idEmpleado,nombre,cargo)