from Personal import Personal

class Administrador(Personal):
    def __init__(self, nombre, apellido, identidad, telefono, no_empleado, salario):
        super().__init__(nombre, apellido, identidad, telefono, no_empleado, salario)
        self.nivelAcceso = 1
    

    def CalculoSalario(self):
        return super().CalculoSalario()
    
    def __str__(self):
        return (f"Administrador: {self.nombre} {self.apellido}, ID: {self.identidad}, Telefono: {self.telefono}, No. Empleado: {self.no_empleado}, Salario: {self.salario}")