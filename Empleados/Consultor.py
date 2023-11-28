from Personal import Personal

class Consultor(Personal):
    def __init__(self, nombre, apellido, identidad, telefono, no_empleado, salario, historial_consultas):
        super().__init__(nombre, apellido, identidad, telefono, no_empleado, salario)
        self.historial_consultas = historial_consultas
        self.nivelAcceso = 3


    def CalculoSalario(self):
        return super().CalculoSalario()
    
    def __str__(self):
        return (f"Consultor: {self.nombre} {self.apellido}, ID: {self.identidad}, Telefono: {self.telefono}, No. Empleado: {self.no_empleado}, Salario: {self.salario}")
    