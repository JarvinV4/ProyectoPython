from Producto import Producto

class Monitor(Producto):
    def __init__(self, nombre_producto, codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor, resolucion, tamano_monitor, conectividad, frecuencia):
        super().__init__(nombre_producto, codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)
        self._resolucion = resolucion
        self._tamano_monitor = tamano_monitor
        self._conectividad = conectividad
        self._frecuencia = frecuencia
    
    def __str__(self):
        return f"[Nombre Producto: {self.nombre_producto} Codigo Producto: {self._codigo_producto} Modelo: {self._modelo} Marca: {self._marca} Precio: {self._precio}]"