from Personal import Personal

class Vendedor(Personal):
    def __init__(self, nombre, apellido, identidad, telefono, no_empleado, salario, ventasRealizadas):
        super().__init__(nombre, apellido, identidad, telefono, no_empleado, salario)
        self.ventasRealizadas=ventasRealizadas

    def generarFactura(self):
        print("facrura")

    def VenderProducto(self):
        print("Vendr")

    def CalculoSalario(self):
        return super().CalculoSalario()