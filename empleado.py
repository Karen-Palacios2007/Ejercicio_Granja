
# Se Crea la clase "Empleado" con sus atributos
class Empleado:
    def __init__(self,idEmpleado,nombre,cargo):
        self._idEmpleado=idEmpleado
        self._nombre=nombre
        self._cargo=cargo 
        
# Se agregan metodos de la clase
    def AlimentarAnimales(self):
        print (f"{self._nombre} esta alimentanddo a los animales \n")     
        self.tipoAlimento=input("Tipo de alimento que le proporcionara al animal: ")
        self.cantAlimento=input("Cantidad del alimento a proporcionar: ")
        print (f"{self._nombre} esta alimentando...")

    def registrarAsistencial(self):
        print ("Se ha registrado el asistencial...")

    def reportarIncidencias(self):
        print (f"{self._nombre} ha reportado una incidencia")
# Se retornan los datos haciendo uso de "get_" 
    def get_cedula(self):
        return self._cedula
    def get_nombre(self):
        return self._nombre
    def get_cargo(self):
        return self._cargo

# Se reciben los datos retornados haciendo uso de "set_"
    def set_cedula(self,cedula):
        self._cedula=cedula
    def set_nombre(self,nombre):
        self._nombre=nombre
    def set_cargo(self,cargo):
        self._cargo=cargo
