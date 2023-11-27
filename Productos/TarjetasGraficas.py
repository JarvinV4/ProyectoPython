from Producto import Producto
class TarjetaGrafica(Producto):
    def __init__(self, codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor, vram, salida, frecuencia_gpu):
        super().__init__(codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)
        self._vram = vram
        self._salida = salida
        self._frecuencia_gpu = frecuencia_gpu


    def __str__(self):
        return f"Tarjeta Grafica: {self._marca},Modelo: {self._modelo}, VRAM: {self._vram}, Salida: {self._salida}, Frecuencia GPU: {self._frecuencia_gpu}, Precio: {self._precio}"
