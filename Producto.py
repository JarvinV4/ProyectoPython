class Producto:
    def __init__(self, codigo, nombre, marca, modelo, precio, cantidad_Inventario):
        self.codigo = codigo
        self.nombre = nombre 
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.cantidad_Inventario = cantidad_Inventario

class Producto_Individual(Producto):
    def __init__(self, codigo, nombre, marca, modelo, precio, cantidad_Inventario, fecha_fabricacion, proveedor ):
        super().__init__(codigo, nombre, marca, modelo, precio, cantidad_Inventario)
        self.fecha_fabricacion = fecha_fabricacion
        self.proveedor = proveedor

class Producto_Combo(Producto):
    def __init__(self, codigo, nombre, marca, modelo, precio, cantidad_Inventario, productos_incluidos):
        super().__init__(codigo, nombre, marca, modelo, precio, cantidad_Inventario)
        self.productos_incluidos = productos_incluidos

class TarjetadeVideo(Producto):
    def __init__(self, codigo, nombre, marca, modelo, precio, cantidad_Inventario, capacidad, serie, conectividad):
        super().__init__(codigo, nombre, marca, modelo, precio, cantidad_Inventario)
        self.capacidad = capacidad
        self.serie = serie
        self.conectividad = conectividad

class Procesador(Producto):
    def __init__(self, codigo, nombre, marca, modelo, precio, cantidad_Inventario, generacion, nucleos, cache):
        super().__init__(codigo, nombre, marca, modelo, precio, cantidad_Inventario)
        self.generacion = generacion
        self.nucleos = nucleos
        self.cache = cache

class Monitor(Producto):
    def __init__(self, codigo, nombre, marca, modelo, precio, cantidad_Inventario, cantidad_Hercios, resolucion, tamano, tipo_Pantalla):
        super().__init__(codigo, nombre, marca, modelo, precio, cantidad_Inventario)
        self.cantidad_Hercios = cantidad_Hercios
        self.resolucion = resolucion
        self.tamano = tamano
        self.tipo_Pantalla = tipo_Pantalla

class Gabinete(Producto):
    def __init__(self, codigo, nombre, marca, modelo, precio, cantidad_Inventario, alto, ancho, color):
        super().__init__(codigo, nombre, marca, modelo, precio, cantidad_Inventario)
        self.alto = alto
        self.ancho = ancho
        self.color = color

