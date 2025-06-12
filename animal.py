class Animal:
    def __init__(self,tipo, edad, sexo):
        self._tipo=tipo
        self._edad=edad
        self._sexo=sexo
    def alimentar(self):
        print (f"{self._tipo} ha sido alimentado")
    def vacunar(self):
        print (f"{self._tipo} ha sido vacunado")
    def registrarPeso(self,peso):
        print (f"{self._tipo}: {peso} kg")
