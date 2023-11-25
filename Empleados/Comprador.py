from Personal import Personal

class Comprador(Personal):
    def __init__(self, nombre, apellido, identidad, telefono, no_empleado, salario):
        super().__init__(nombre, apellido, identidad, telefono, no_empleado, salario)

    def ComprarInventario():
        print("Comprando producot")


    def AgregarNuevoProducto():
        print("Agregar nuevo producto")

    def CalculoSalario(self):
        return super().CalculoSalario()