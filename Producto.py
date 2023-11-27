from abc import ABC, abstractmethod
from typing import List

class Producto(ABC):
    _productos_registrados = set()

    def __init__(self, codigo_producto,  modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor):
        #Verifica si el codigo del producto ya existe
        while codigo_producto in Producto._productos_registrados:
            print("Advertencia: El codigo ya esta en uso.")
            #Solicitar un nuevo codigo
            codigo_producto = input("Ingrese un nuevo codigo de producto: ")

        
        self._codigo_producto = int(codigo_producto)
        self._modelo = modelo
        self._numero_de_serie = numero_de_serie
        self._marca = marca
        self._fabricante = fabricante
        self._precio = float(precio)
        self._cantidad_en_inventario = int(cantidad_en_inventario)
        self._fecha_de_compra = fecha_de_compra
        self._fecha_de_fabricacion = fecha_de_fabricacion
        self._proveedor = proveedor

        # Registrar el nuevo código de producto
        Producto._productos_registrados.add(codigo_producto)
"""
    #Método abstracto para calcular el precio del producto
    @abstractmethod
    def precio_producto(self):
        pass
        
    @classmethod
    def eliminar_producto(cls, codigo_producto):
        # Método de clase para eliminar un producto del inventario
        if codigo_producto in cls._productos_registrados:
            cls._productos_registrados.remove(codigo_producto)
            print(f"Producto con código {codigo_producto} eliminado.")
        else:
            print(f"No se encontró ningún producto con código {codigo_producto}.")

    def __str__(self):
        return f"Codigo: {self._codigo_producto} Nombre del Producto: {self._nombre_producto} Modelo: {self._modelo} Marca: {self._marca} Fabricante: {self._fabricante} Precio: {self._precio} Cantidad en Inventario: {self._cantidad_en_inventario}"

    def str_para_administrador(self):
        return f"{self.__str__()} Numero de Serie: {self._numero_de_serie} Fecha de fabricacion: {self._fecha_de_fabricacion} Fecha de Compra: {self._fecha_de_compra} Proveedor: {self._proveedor}"

    def eliminar_producto(self):
        # Método para eliminar un producto del inventario
        Producto._productos_registrados.remove(self._codigo_producto)

class ProductoIndividual(Producto):
    def __init__(self, codigo_producto, nombre_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor):
        super().__init__(codigo_producto, nombre_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)

class ProductoCombo(Producto):        
    def __init__(self, codigo_producto, nombre_combo, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor, productos_incluidos: List[Producto]):
        super().__init__(codigo_producto, nombre_combo, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)
        self._productos_incluidos = productos_incluidos

    #Obtiene la lista de productos incluidos en el combo.
    @property
    def obtener_productos_incluidos(self):
        return self._productos_incluidos
    
    #Calcula el precio total del combo.
    def precio_producto(self):
        return sum(producto.precio for producto in self._productos_incluidos)
        
        """
