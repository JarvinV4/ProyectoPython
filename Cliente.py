from Persona import Persona
class Cliente(Persona):
    def __init__(self, nombre, apellido, identidad, telefono, compra, rtn):
        super().__init__(nombre, apellido, identidad, telefono)
        self.compra = compra
        self.rtn = rtn

    def SeleccionarProductos(self):
        print("A")
