from Producto import Producto

class Monitor(Producto):
    def __init__(self, codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor, resolucion, tamano_monitor, conectividad, frecuencia):
        super().__init__(codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)
        self._resolucion = resolucion
        self._tamano_monitor = tamano_monitor
        self._conectividad = conectividad
        self._frecuencia = frecuencia