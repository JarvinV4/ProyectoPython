from Producto import Producto

class Gabinete(Producto):
    def __init__(self,
                 nombre_producto,
                 codigo_producto,
                 modelo,
                 marca,
                 fabricante,
                 numero_de_serie,
                 precio,
                 cantidad_en_inventario,
                 fecha_de_compra,
                 fecha_de_fabricacion,
                 proveedor,
                 material,
                 color,
                 tamano_gabinete,
                 peso,
                 dimensiones,
                 capacidad_de_ventiladores):
        
        super().__init__(nombre_producto, codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)
        self._material = material
        self._color = color
        self._tamano_gabinete = tamano_gabinete
        self._peso = float(peso)
        self._dimensiones = dimensiones
        self._capacidad_de_ventiladores = capacidad_de_ventiladores
        self._tipoProducto = "Gabinete"
        
        
    def __str__(self):
        return f"[Nombre Producto: {self.nombre_producto} Codigo Producto: {self._codigo_producto} Modelo: {self._modelo} Marca: {self._marca} Precio: {self._precio}]"
        #return f'Nombre Producto: {self.nombre_producto} Codigo Producto: {self._codigo_producto} Modelo: {self._modelo} Marca: {self._marca} Fabricante: {self._fabricante} Numero Serie: {self._numero_de_serie} Precio: {self._precio} Cantidad Inventario: {self._cantidad_en_inventario} Fecha Compra: {self._fecha_de_compra} Fecha Fabricador: {self._fecha_de_fabricacion} Proveedor: {self._proveedor} Material: {self._material} Color: {self._color} Tamaño Gabinete: {self._tamano_gabinete} Peso: {self._peso} Dimensiones: {self._dimensiones} Capacidad Ventiladores: {self._capacidad_de_ventiladores}'   
        
        