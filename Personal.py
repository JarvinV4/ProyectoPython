from Persona import Persona
from abc import ABC,abstractmethod

class Personal(Persona, ABC):
    def __init__(self, nombre, apellido, identidad, telefono, no_empleado, salario):
        super().__init__(nombre, apellido, identidad, telefono)
        self.no_empleado = no_empleado
        self.salario = salario
    
    @abstractmethod
    def CalculoSalario(self):
        pass