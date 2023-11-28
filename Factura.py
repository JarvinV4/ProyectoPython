from Persona import Persona
from Cliente import Cliente
from Empleados.Vendedor import Vendedor
from Producto import Producto, ProductoIndividual, ProductoCombo
from Productos.Gabinete import Gabinete
from Productos.Monitor import Monitor
from Productos.Procesador import Procesador
from Productos.TarjetasGraficas import TarjetaGrafica

class Factura():
    
    cliente = None
    productosPorComprar = [] 
    vendedor = None
    #Tipo de envio
    control_envio = None 
    fecha_venta = None
    subtotal = float
    ISV = float(0.12)
    total = float
    codigoFactura = int

    def __init__(self, cliente, productosPorComprar, vendedor, control_envio, fecha_venta, subtotal, total, codigoFactura):
        self.cliente = cliente
        self.productosPorComprar = productosPorComprar
        self.vendedor = vendedor
        self.control_envio = control_envio
        self.fecha_venta = fecha_venta
        self.subtotal = subtotal
        self.ISV = float(0.12)
        self.total = total
        self.codigoFactura = codigoFactura
        
    def imprimirFactura(self):
        print("=" * 50)
        print("{:^30}".format("Factura"))
        print("=" * 50)
        print("\nNúmero de Factura: {:>30}".format(self.codigoFactura))
        print("Fecha de Emisión: {:>28}".format(self.fecha_venta))
        print("Cliente: {:>35}".format(str(self.cliente)))
        print("Vendedor: {:>35}".format(str(self.vendedor.nombre + " " + self.vendedor.apellido)))
        print("\nProductos:")
        for producto in self.productosPorComprar:
            if isinstance(producto, Producto):
                print("{:<30} {:>20}".format(f"- {str(producto.nombre)}:", f"{str(producto.precio)}"))
            else:
                print("Error: El objeto producto no es una instancia de la clase Producto.")
        print("\nSubtotal: {:>29}".format(f"{self.subtotal}%"))
        print("Total a Pagar: {:>29}".format(self.total))
        print("=" * 50)
    
    
cliente1 = Cliente("Pamela", "Gomez", "123456789", "27831234", "1234567890")
vendedor1 = Vendedor("Terre", "Neitor", "2627282930", "27831415", "004", 17000, 50)        

factura = Factura(cliente1, [1,2,3,4,5] , vendedor1, "Adomicilio", "17/12/23", 100, float(100*1.12), "001200" )

factura.imprimirFactura()