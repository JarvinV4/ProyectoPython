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
    
    def __str__(self):
        return (f"Vendedor: {self.nombre} {self.apellido}, ID: {self.identidad}, Telefono: {self.telefono}, No. Empleado: {self.no_empleado}, Salario: {self.salario}")
