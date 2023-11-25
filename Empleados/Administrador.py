from Personal import Personal

class Administrador(Personal):
    def __init__(self, nombre, apellido, identidad, telefono, no_empleado, salario):
        super().__init__(nombre, apellido, identidad, telefono, no_empleado, salario)

    def ContratarPersonal():
        print("Contratando gente")

    def CalculoSalario(self):
        return super().CalculoSalario()