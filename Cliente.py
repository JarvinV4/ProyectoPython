from Persona import Persona
class Cliente(Persona):
    def __init__(self, nombre, apellido, identidad, telefono, rtn):
        super().__init__(nombre, apellido, identidad, telefono)

        self.rtn = rtn

    def SeleccionarProductos(self):
        print("A")

    def __str__(self):
        return (f"Cliente: {self.nombre} {self.apellido}, ID: {self.identidad}, Teléfono: {self.telefono}, RTN: {self.rtn}")
