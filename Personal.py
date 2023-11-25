from Persona import Persona
class Personal(Persona):
    def __init__(self, nombre, apellido, identidad, telefono, no_empleado, salario):
        super().__init__(nombre, apellido, identidad, telefono)
        self.no_empleado = no_empleado
        self.salario = salario