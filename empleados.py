# Se Crea la clase "Empleado" con sus atributos
class Empleado:
    def __init__(self,cedula,nombre,cargo,cantAlimento,tipoAlimento):
        self._cedula=cedula
        self._nombre=nombre
        self._cargo=cargo 
        self.cantAlimento=cantAlimento
        self.tipoAlimento=tipoAlimento
# Se agregan metodos de la clase
    def realizarTarea(self):
        print (f"{self._nombre} esta realizando una tarea...")       
    def registrarAsistencial(self):
        print ("Se ha registrado el asistencial...")
    def registrarCantidadAlimento(self):
        print (f"Cantidad del alimento: {self.cantAlimento}")
    def registrarTipoAlimento(self):
        print (f"Tipo de alimento: {self.tipoAlimento}")
    def reportarIncidencias(self):
        print (f"{self._nombre} ha reportado una incidencia")
# Se retornan los datos haciendo uso de "get_" 
    def get_cedula(self):
        return self._cedula
    def get_nombre(self):
        return self._nombre
    def get_cargo(self):
        return self._cargo
    def get_tipoAlimento(self):
        return self.tipoAlimento
    def get_cantAlimento(self):
        return self.cantAlimento
# Se reciben los datos retornados haciendo uso de "set_"
    def set_cedula(self,cedula):
        self._cedula=cedula
    def set_nombre(self,nombre):
        self._nombre=nombre
    def set_cargo(self,cargo):
        self._cargo=cargo
    def set_tipoAlimento(self,tipoalimento):
        self.tipoAlimento=tipoalimento
    def set_cantAlimento(self,cantalimento):
        self.cantAlimento=cantalimento
