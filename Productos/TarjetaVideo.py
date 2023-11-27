from Productos import Producto


class TarjetaVideo(Producto):
    capacidad = None
    serie = None
    conectividad = None

    def __init__(
        self,
        nombre,
        precio,
        codigo,
        marca,
        modelo,
        cantidadInventario,
        existencia,
        capacidad,
        serie,
        conectividad,
    ):
        super().__init__(
            nombre, precio, codigo, marca, modelo, cantidadInventario, existencia
        )
        self.capacidad = capacidad
        self.conectividad = conectividad
        self.serie = serie
