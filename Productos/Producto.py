class Producto:
    def AgregarProducto(self):
        pass

    nombre: None
    precio: None
    codigo: None
    marca: None
    modelo: None
    cantidadInventario: None
    existencia: None

    def __init__(
        self, nombre, precio, codigo, marca, modelo, cantidadInventario, existencia
    ):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
        self.marca = marca
        self.modelo = modelo
        self.cantidadInventario = cantidadInventario
        self.existencia = existencia
