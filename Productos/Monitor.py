from Productos import Producto


class Monitor(Producto):
    cantidadHercios = None
    resolucion = None
    tamaño = None
    tipoPantalla = None

    def __init__(
        self,
        nombre,
        precio,
        codigo,
        marca,
        modelo,
        cantidadInventario,
        existencia,
        cantidadHercios,
        resolucion,
        tamaño,
        tipoPantalla,
    ):
        super().__init__(
            nombre, precio, codigo, marca, modelo, cantidadInventario, existencia
        )
        self.cantidadHercios = cantidadHercios
        self.tamaño = tamaño
        self.resolucion = resolucion
        self.tipoPantalla = tipoPantalla
