from abc import ABC, abstractmethod

class Producto(ABC):
    _productos_registrados = set()

    def __init__(self, nombre_producto, codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor):
       
        """#Verifica si el codigo del producto ya existe
        while codigo_producto in Producto._productos_registrados:
            print("Advertencia: El codigo ya esta en uso.")
            #Solicitar un nuevo codigo
            codigo_producto = input("Ingrese un nuevo codigo de producto: ")"""
        self.nombre_producto = nombre_producto
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
        self._tipoProducto = "Producto"

        # Registrar el nuevo código de producto
        Producto._productos_registrados.add(codigo_producto)
        
    @classmethod
    def eliminar_producto(cls, codigo_producto):
        # Método de clase para eliminar un producto del inventario
        if codigo_producto in cls._productos_registrados:
            cls._productos_registrados.remove(codigo_producto)
            print(f"Producto con código {codigo_producto} eliminado.")
        else:
            print(f"No se encontró ningún producto con código {codigo_producto}.")

    def __str__(self):
        return f'Codigo: {self._codigo_producto} Nombre del Producto: {self.nombre_producto} Modelo: {self._modelo} Marca: {self._marca} Fabricante: {self._fabricante} Precio: {self._precio} Cantidad en Inventario: {self._cantidad_en_inventario}'

    def str_para_administrador(self):
        return f'{self.__str__()} Numero de Serie: {self._numero_de_serie} Fecha de fabricacion: {self._fecha_de_fabricacion} Fecha de Compra: {self._fecha_de_compra} Proveedor: {self._proveedor}'

    def eliminar_producto(self):
        # Método para eliminar un producto del inventario
        Producto._productos_registrados.remove(self._codigo_producto) 
    

class ProductoIndividual(Producto):
    def __init__(self, nombre_producto, codigo_producto,  modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor):
        super().__init__(nombre_producto, codigo_producto,  modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)
        self._tipoProducto = "Producto Individual"
        

       
       
       
       
       
       
       
       

class ProductoCombo(Producto):        
    nombre_producto = None
    codigoCombo = None
    precio = None
    cantidadInventario = None
    fechaCompra = None
    productosIncluidos = []
    
    
    def __init__(self, nombreCombo, codigoCombo, cantidadInventario, fecha_de_compra, productosIncluidos):
        self._tipoProducto = "Combos"
        self.cantidadInventario = cantidadInventario
        self._fecha_de_compra = fecha_de_compra
        self.nombreCombo = nombreCombo
        self.codigoCombo = codigoCombo
        self.productosIncluidos = productosIncluidos

        
    def __str__(self):
        comboInfo= f'[Nombre Combo: {self.nombreCombo} Cantidad Inventario: {self.cantidadInventario} Codigo Combo: {self.codigoCombo} ]'
        comboInfo += '\nProductos Incluidos:\n'
        for i, producto in enumerate(self.productosIncluidos, start=1):
            comboInfo += f'{i}. {producto.__str__()} \n'
        return comboInfo
    
    #Calcula el precio total del combo.
    def precio_combo(self):
        #return sum(producto._precio for producto in self.productosIncludos)
        precio_total = sum(producto._precio for producto in self.productosIncluidos)
        return precio_total
        
        
    def precio_combo_descuento(self):  
        if len(self.productosIncluidos) > 2:  
            descuento = 0.15 * self.precio_combo()
            precio_con_descuento = self.precio_combo() - descuento
            return precio_con_descuento
        else:
            # Calcular el precio total sin descuento
            return sum(producto._precio for producto in self.productosIncluidos)
        
    def InfoCombo(self):
        # Formatea la información del combo
        combo_info = f'Nombre Combo: {self.nombreCombo}\nCódigo Combo: {self.codigoCombo}\nPrecio Total del Combo: {self.precio_combo()}\n, Precio del combo con descuento: {self.precio_combo_descuento()}'
        combo_info += f'Cantidad en Inventario: {self.cantidadInventario}\nFecha de Compra: {self._fecha_de_compra}\n'
        
        # Agrega información de los productos incluidos
        combo_info += 'Productos Incluidos:\n'
        for i, producto in enumerate(self.productosIncluidos, start=1):
            combo_info += f'{i}. {producto.InfoCombo()} \n'

        return combo_info
    
    #Obtiene la lista de productos incluidos en el combo.
    @property
    def obtener_productos_incluidos(self):
            return self.productosIncluidos
        
    
    
""" def __init__(self, nombre_combo, codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor, productos_incluidos: List[Producto]):
        super().__init__(nombre_producto, codigo_producto, nombre_combo, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)
        self._productos_incluidos = productos_incluidos"""
