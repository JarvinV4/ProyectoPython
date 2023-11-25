from Personal import Personal

class Consultor(Personal):
    def __init__(self, nombre, apellido, identidad, telefono, no_empleado, salario, historial_consultas):
        super().__init__(nombre, apellido, identidad, telefono, no_empleado, salario)
        self.historial_consultas = historial_consultas


    def CalculoSalario(self):
        return super().CalculoSalario()