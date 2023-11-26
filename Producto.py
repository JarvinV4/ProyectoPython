from abc import ABC, abstractmethod
from typing import List

class Producto(ABC):
    _productos_registrados = set()

    def __init__(self, codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor):
        #Verifica si el codigo del producto ya existe
        while codigo_producto in Producto._productos_registrados:
            print("Advertencia: El codigo ya esta en uso.")
            #Solicitar un nuevo codigo
            codigo_producto = input("Ingrese un nuevo codigo de producto: ")

        self._codigo_producto = codigo_producto
        self._modelo = modelo
        self._numero_de_serie = numero_de_serie
        self._marca = marca
        self._fabricante = fabricante
        self._precio = float(precio)
        self._cantidad_en_inventario = cantidad_en_inventario
        self._fecha_de_compra = fecha_de_compra
        self._fecha_de_fabricacion = fecha_de_fabricacion
        self._proveedor = proveedor

        # Registrar el nuevo código de producto
        Producto._productos_registrados.add(codigo_producto)

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
        return f"Codigo: {self._codigo_producto} Modelo: {self._modelo} Marca: {self._marca} Fabricante: {self._fabricante} Precio: {self._precio} Cantidad en Inventario: {self._cantidad_en_inventario}"

    def str_para_administrador(self):
        return f"{self.__str__()} Numero de Serie: {self._numero_de_serie} Fecha de fabricacion: {self._fecha_de_fabricacion} Fecha de Compra: {self._fecha_de_compra} Proveedor: {self._proveedor}"

    def eliminar_producto(self):
        # Método para eliminar un producto del inventario
        Producto._productos_registrados.remove(self._codigo_producto)

class ProductoIndividual(Producto):
    def __init__(self, codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor):
        super().__init__(codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)

class ProductoCombo(Producto):
    def __init__(self, codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor, productos_incluidos: List[Producto]):
        super().__init__(codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)
        self._productos_incluidos = productos_incluidos

    #Obtiene la lista de productos incluidos en el combo.
    @property
    def obtener_productos_incluidos(self):
        return self._productos_incluidos
    
    #Calcula el precio total del combo.
    def precio_producto(self):
        return sum(producto.precio for producto in self._productos_incluidos)
    
def agregar_producto():
    try:        
        print("Ingresar datos del producto")
        codigo_producto = input("Codigo del producto: ")
        modelo = input("Modelo del producto: ")
        marca = input("Marca del producto: ")
        fabricante = input("Fabricante del producto: ")
        numero_de_serie = input("Numero de serie del producto: ")
        precio = input("Precio del producto: ")
        cantidad_en_inventario = input("Cantidad en inventario: ")
        fecha_de_compra = input("Fecha de compra: ")
        fecha_de_fabricacion = input("Fecha de fabricion: ")
        proveedor = input("Proveedor: ")
        producto = Producto(codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)
        productos.append(producto)
    except:
        print("Error al agregar producto")

def eliminar_producto():
    codigo_a_eliminar = input("Ingrese código de producto que desea eliminar: ")
    for producto in productos:
        if producto._codigo_producto == codigo_a_eliminar:
            productos.remove(producto)
            producto.eliminar_producto()  # Llamada al método de instancia
            break
    else:
        print(f"No se encontró ningún producto con este código.")

productos = []

while True:
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        eliminar_producto()
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
