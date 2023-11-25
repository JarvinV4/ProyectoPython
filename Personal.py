from Persona import Persona
from abc import abstractmethod

class Personal(Persona):
    def __init__(self, nombre, apellido, identidad, telefono, no_empleado, salario):
        super().__init__(nombre, apellido, identidad, telefono)
        self.no_empleado = no_empleado
        self.salario = salario
    
    @abstractmethod
    def CalculoSalario(self):
        pass