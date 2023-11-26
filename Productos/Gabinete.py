from Producto import Producto

class Gabinete(Producto):
    def __init__(self, codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor, material, color, tamano_gabinete, peso, dimensiones, capacidad_de_ventiladores):
        super().__init__(codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)
        self._material = material
        self._color = color
        self._tamano_gabinete = tamano_gabinete
        self._peso = float(peso)
        self._dimensiones = dimensiones
        self._capacidad_de_ventiladores = capacidad_de_ventiladores