class Empleado:
    def __init__(self,cedula,nombre,cargo):
        self._cedula=cedula
        self._nombre=nombre
        self._cargo=cargo 
    def realizarTarea(self):
        print (f"{self._nombre} esta realizando una tarea...")       
    def registrarAsistencial(self):
        print ("Se ha registrado el asistencial...")
    def reportarIncidencias(self):
        print (f"{self._nombre} ha reportado una incidencia")
