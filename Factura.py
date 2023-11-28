from Persona import Persona
from Cliente import Cliente
from Empleados.Vendedor import Vendedor
from Producto import Producto, ProductoIndividual, ProductoCombo
from Productos.Gabinete import Gabinete
from Productos.Monitor import Monitor
from Productos.Procesador import Procesador
from Productos.TarjetasGraficas import TarjetaGrafica
from datetime import datetime

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
        self.fecha_emision = datetime.now()
        self.subtotal = subtotal
        self.ISV = float(0.12)
        self.total = total
        self.codigoFactura = codigoFactura
        
    def imprimirFactura(self):
        print("=" * 105)
        print("{:^85}".format("Factura"))
        print("=" * 105)
        print("\nNúmero de Factura: {:>81}".format(self.codigoFactura))
        print("Fecha de Emisión: {:>82}".format(self.fecha_emision.strftime("%Y-%m-%d %H:%M:%S")))
        print("")
        print("{:>35}".format(str(self.cliente)))
        print("Vendedor: {:>3}".format(str(self.vendedor.nombre)),(str(self.vendedor.apellido)))
        print("\nProductos:")
        for producto in self.productosPorComprar:
            if isinstance(producto, Producto):
                print("{:<30} {:>20}".format(f"- {str(producto.nombre_producto)}:", f"{str(producto._precio)}"))
            else:
                print("Error: El objeto producto no es una instancia de la clase Producto.")
        print("\nEstado de envio: {:>84}".format(self.control_envio))       
        print("\nSubtotal: {:>91}".format(f"{self.subtotal}%"))
        print("\nISV: {:>96}".format(f"{self.ISV}%"))
        print("Total a Pagar: {:>86}".format(self.total))
        print("=" * 105)

    
    