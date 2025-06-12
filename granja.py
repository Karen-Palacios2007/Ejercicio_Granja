
class Granja:
    def __init__(self,nombre,tamaño,cant_corral,cant_empleados):
        self._nombre=nombre
        self._tamaño=tamaño
        self._corrales=[]
        self._empleados=[]

    def registrarEmpleado(self,empleado):
        self.empleados.append(empleado)
        print (f"Empleado {self._nombre}")
    def asignarAnimal(self,corral,Animal):
        self.corral.append(corral)
        self.animal.append(Animal)

    

