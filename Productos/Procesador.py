from Productos import Producto


class Procesador(Producto):
    generacion = None
    nucleos = None
    noHilos = None
    cache = None
    graficosIntegrados = None

    def __init__(
        self,
        nombre,
        precio,
        codigo,
        marca,
        modelo,
        cantidadInventario,
        existencia,
        generacion,
        nucleos,
        noHilos,
        cache,
        graficosIntegrados,
    ):
        super().__init__(
            nombre, precio, codigo, marca, modelo, cantidadInventario, existencia
        )
        self.generacion = generacion
        self.noHilos = noHilos
        self.nucleos = nucleos
        self.cache = cache
        self.graficosIntegrados = graficosIntegrados
