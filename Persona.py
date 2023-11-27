from abc import ABC,abstractmethod
class Persona(ABC):
    def __init__(self, nombre, apellido, identidad, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.identidad = identidad
        self.telefono = telefono
