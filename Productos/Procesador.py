from Producto import Producto

class Procesador(Producto):
    def __init__(self, codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor, generacion, nucleos, cache, zocalo_cpu, frecuencia_cpu):
        super().__init__(codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)
        self._generacion = generacion
        self._nucleos = nucleos
        self._cache = cache
        self._zocalo_cpu = zocalo_cpu
        self._frecuencia_cpu = frecuencia_cpu

    def __str__(self):
        return (f"Procesador: {self._marca} {self._modelo}, Generacion: {self._generacion}, Nucleos: {self._nucleos}, Cache: {self._cache}, Zocalo CPU: {self._zocalo_cpu}, Frecuencia CPU: {self._frecuencia_cpu}, Precio: {self._precio}")
