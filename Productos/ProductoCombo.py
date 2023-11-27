from Productos import Producto


class Producto_combo(Producto):
    productos = []
    nombreCombo = None
    precioBruto = None
    precioNeto = None

    def __init__(
        self,
        nombre,
        precio,
        codigo,
        marca,
        modelo,
        cantidadInventario,
        existencia,
        productos,
        nombreCombo,
        precioBruto,
        precioNeto,
    ):
        super().__init__(
            nombre, precio, codigo, marca, modelo, cantidadInventario, existencia
        )
        self.productos = productos
        self.nombreCombo = nombreCombo
        self.precioBruto = precioBruto
        self.precioNeto = precioNeto
