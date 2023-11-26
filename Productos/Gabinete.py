from Productos import Producto


class Gabinete(Producto):
    altura = None
    anchura = None
    color = None

    def __init__(
        self,
        nombre,
        precio,
        codigo,
        marca,
        modelo,
        cantidadInventario,
        existencia,
        altura,
        anchura,
        color,
    ):
        super().__init__(
            nombre, precio, codigo, marca, modelo, cantidadInventario, existencia
        )
        self.altura = altura
        self.color = color
        self.anchura = anchura
