from Personal import Personal

class Comprador(Personal):
    def __init__(self, nombre, apellido, identidad, telefono, no_empleado, salario):
        super().__init__(nombre, apellido, identidad, telefono, no_empleado, salario)
        self.nivelAcceso = 2

    def ComprarInventario():
        print("Comprando producot")


    def AgregarNuevoProducto():
        print("Agregar nuevo producto")

    def CalculoSalario(self):
        return super().CalculoSalario()
    
    def __str__(self):
        return (f"Comprador: {self.nombre} {self.apellido}, ID: {self.identidad}, Telefono: {self.telefono}, No. Empleado: {self.no_empleado}, Salario: {self.salario}")
