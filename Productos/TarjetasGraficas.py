from Producto import Producto

class TarjetaGrafica(Producto):
    def __init__(self,nombre_producto, codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor, vram, salida, frecuencia_gpu):
        super().__init__(nombre_producto, codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)
        self._vram = vram
        self._salida = salida
        self._frecuencia_gpu = frecuencia_gpu
    
    def __str__(self):
        return f"[Nombre Producto: {self.nombre_producto} Codigo Producto: {self._codigo_producto} Modelo: {self._modelo} Marca: {self._marca} Precio: {self._precio}]"