from Persona import Persona
from Personal import Personal
from Cliente import Cliente
from Empleados.Administrador import Administrador
from Empleados.Comprador import Comprador
from Empleados.Consultor import Consultor
from Empleados.Vendedor import Vendedor
from Producto import Producto, ProductoIndividual, ProductoCombo
from Productos.Gabinete import Gabinete
from Productos.Monitor import Monitor
from Productos.Procesador import Procesador
from Productos.TarjetasGraficas import TarjetaGrafica
from Factura import Factura
from datetime import datetime

import random

#Genera los codigos de los productos
def GenerarCodigo():
    codigo = random.randrange(1000, 9999)
    return codigo

#MEMO: Esta funcion se encarga de agregar clientes o de localizar clientes ya existentes en caso de tener la misma identidad
def agregar_cliente():
    
    identidad = input("Ingrese su numero de identidad: ")
    # si el cliente ya existe no va a crear uno nuevo
    for cliente_existente in clientes:
        if cliente_existente.identidad == identidad:
            print(f"El cliente con la identidad {identidad} ya existe: ")
            print("¡Bienvenido de nuevo! " + cliente_existente.nombre+" "+cliente_existente.apellido) #NOTA: agregar funcionalidad para utilizar este cliente en vez de imprimirlo
            # Salir  si el cliente ya existe 
            
        else:
            nombre = input("Ingrese su primer nombre: ")
            apellido = input("Ingrese su apellido: ")
            telefono = input("Ingrese su numero de telefonoe: ")
            rtn = input("Ingrese su numero de rtn: ")

            cliente = Cliente(nombre, apellido, identidad, telefono, rtn)
            clientes.append(cliente)

#MEMO: Esta funcion se encarga de agregar empleados o de localizar empleados ya existentes en caso de tener lel mismo numero de empleado
def ContratarPersonal():
   
        try:
            no_empleado = input("Ingrese el numero de empleado: ")
            # si el empleado ya existe no va a crear uno nuevo
            for empleado_existente in empleados:
                if empleado_existente.no_empleado == no_empleado:
                    print(f"El empleado con el numero de empleado {no_empleado} ya existe: ")
                    print(empleado_existente) #NOTA: agregar funcionalidad para utilizar este cliente en vez de imprimirlo
                    # Salir  si el empleado ya existe
                    break
                    
            nombre = input("Ingrese el nombre del empleado: ")
            apellido = input("Ingrese el apellido del empleado: ")
            identidad = input("Ingrese la identidad del empleado: ")
            telefono = input("Ingrese el telefono del empleado: ")
            salario = float(input("Ingrese el salario del empleadp: "))
            print("¿Cual sera el cargo de este empleado?")
            print("1. Comprador")
            print("2. Consultor")
            print("3. Vendedor")
            seguir = True
            opcion = int(input("Seleccione una opcion: "))
            while(seguir):
                match(opcion):
                    case 1:
                        
                        empleado = Comprador(nombre, apellido, identidad, telefono, no_empleado, salario)
                        empleados.append(empleado)
                        break
                    case 2:
                        empleado = Consultor(nombre, apellido, identidad, telefono, no_empleado, salario, None)
                        empleados.append(empleado)
                        break
                    case 3:
                        empleado = Vendedor(nombre, apellido, identidad, telefono, no_empleado, salario, None)
                        vendedores.append(empleado)
                        break
                    
                    case default:
                        print("Opcion invalida")
                        break  
        except:
            print("Datos Invalidos")  
      
#Crea instancias de los productos ya definidos, crea productos nuevos y crea combos
def agregarProducto():
    try:
        print("================================================================")
        print("Que producto desea agregar?")
        print("1. Gabinete")
        print("2. Monitor")
        print("3. Tarjeta Grafica")
        print("4. Procesador")
        print("5. Producto Nuevo")
        print("6. Agregar Combo")
        opcion = int(input("Ingrese una opcion: "))
        print("================================================================")
        print("")
        
    except:
        print("Opcion Invalida")
    else:
        
        match(opcion):
            case 1:
                print("================================================================")
                nombreProducto = input("ingrese el nombre del producto: ")
                codigoProducto = GenerarCodigo()
                modelo = input("Ingrese modelo del Gabinete: ")
                marca = input("Ingrese el marca del Gabinete: ")
                fabricante = input("Ingrese fabricante del Gabinete: ")
                numeroSerie = input("Ingrese numero de serie del Gabinete: ")
                precio = input("Ingrese precio del Gabinete: ")
                cantidadInventario = input("Ingrese cantidad que comprara de Gabinete: ")
                fechaCompra = input("Ingrese fecha de compra: ")
                fechaFabricacion = input("Ingrese fecha de fabricacion del Gabinete: ")
                proveedor = input("Ingrese proveedor del Gabinete: ")
                material = input("Ingrese material del Gabinete: ")
                color = input("Ingrese color del Gabinete: ")
                tamanioGabinete = input("Ingrese tamaño del Gabinete: ")
                peso = input("Ingrese peso del Gabinete: ")
                dimensiones = input("Ingrese dimensiones del Gabinete: ")
                capacidadVentiladores = input("tiene capacidad para ventiladores? ")
                
                gabinete = Gabinete(nombreProducto, codigoProducto, modelo, marca, fabricante, numeroSerie, precio, cantidadInventario, fechaCompra, 
                                    fechaFabricacion, proveedor, material,color, tamanioGabinete, peso, dimensiones, capacidadVentiladores)
                gabinetes.append(gabinete)
                print("Producto Agregado con exito")
                print("================================================================")
                print("")
                
                
            case 2:
                print("================================================================")
                
                nombreProducto = input("ingrese el nombre del producto: ")
                codigoProducto = GenerarCodigo()
                modelo = input("Ingrese modelo del monitor: ")
                marca = input("Ingrese el marca del monitor: ")
                fabricante = input("Ingrese fabricante del monitor: ")
                numeroSerie = input("Ingrese numero de serie del monitor: ")
                precio = input("Ingrese precio del monitor: ")
                cantidadInventario = input("Ingrese cantidad que comprara de monitor: ")
                fechaCompra = input("Ingrese fecha de compra: ")
                fechaFabricacion = input("Ingrese fecha de fabricacion del monitor: ")
                proveedor = input("Ingrese proveedor del monitor: ")
                resolucion = input("Ingrese la resolucion del monitor: ")
                tamanioMonitor = input("Ingrese el tamaño del monitor: ")
                conectividad = input("Ingrese la conectividad del Monitor: ")
                frecuencia = input("Ingrese la frecuencia del monitor: ")
                
                monitor = Monitor(nombreProducto, codigoProducto, modelo, marca, fabricante, numeroSerie, precio, cantidadInventario, fechaCompra, 
                                    fechaFabricacion, proveedor, resolucion, tamanioMonitor, conectividad, frecuencia)
                monitores.append(monitor)
                print("Producto Agregado con exito")
                print("================================================================")
                
                print("")
                
                
            case 3:
                print("================================================================")
                
                print("Ingresar datos del producto")
                codigo_producto = GenerarCodigo()
                nombre_producto = input("Nombre del producto: ")
                modelo = input("Modelo del producto: ")
                marca = input("Marca del producto: ")
                fabricante = input("Fabricante del producto: ")
                numero_de_serie = input("Numero de serie del producto: ")
                precio = input("Precio del producto: ")
                cantidad_en_inventario = input("Cantidad en inventario: ")
                fecha_de_compra = input("Fecha de compra: ")
                fecha_de_fabricacion = input("Fecha de fabricion: ")
                proveedor = input("Proveedor: ")
                vram= input("VRAM: ")
                salida = input("Salida: ")
                frecuencia_gpu= input("Frecuencia gpu: ")
                print("Producto Agregado con exito")
                print("================================================================")
                
                print("")
                producto = TarjetaGrafica(nombre_producto, codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor, vram, salida, frecuencia_gpu)
                tarjetasGraficas.append(producto)
                
            case 4:
                print("================================================================")
                
                print("Ingresar datos del producto")
                codigo_producto = GenerarCodigo()
                nombre_producto = input("Nombre del producto: ")
                modelo = input("Modelo del producto: ")
                marca = input("Marca del producto: ")
                fabricante = input("Fabricante del producto: ")
                numero_de_serie = input("Numero de serie del producto: ")
                precio = input("Precio del producto: ")
                cantidad_en_inventario = input("Cantidad en inventario: ")
                fecha_de_compra = input("Fecha de compra: ")
                fecha_de_fabricacion = input("Fecha de fabricion: ")
                proveedor = input("Proveedor: ")
                generacion= input("Generacion: ")
                nucleos = input("Nucleos: ")
                cache= input("Cache: ")
                zocalo_cpu=input("Zocalo CPU")
                frecuencia_cpu= input("Frecuencia cpu: ")
                producto = Procesador(nombre_producto, codigo_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor, generacion, nucleos, cache, zocalo_cpu, frecuencia_cpu)
                procesadores.append(producto)
                print("Producto Agregado con exito")
                print("================================================================")
                
                print("")
                
            case 5:
                print("================================================================")
                
                print("Ingresar datos de nuevo producto")
                codigoProducto = GenerarCodigo()
                nombre_producto = input("Nombre del producto: ")
                modelo = input("Modelo del producto: ")
                marca = input("Marca del producto: ")
                fabricante = input("Fabricante del producto: ")
                numero_de_serie = input("Numero de serie del producto: ")
                precio = input("Precio del producto: ")
                cantidad_en_inventario = input("Cantidad en inventario: ")
                fecha_de_compra = input("Fecha de compra: ")
                fecha_de_fabricacion = input("Fecha de fabricion: ")
                proveedor = input("Proveedor: ")
                nuevo_producto = ProductoIndividual(nombre_producto, codigoProducto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)
                productosNuevos.append(nuevo_producto)
                print("Producto Agregado con exito")
                print("================================================================")
                
                print("")
            case 6:
                print("================================================================")
                
                print("\nIngresar datos de Producto Combo")
                codigoCombo = GenerarCodigo()
                nombreCombo = input("Nombre del Combo: ")
                cantidad_en_inventario = input("Cantidad en inventario: ")
                fecha_de_compra = input("Fecha de compra: ")
                productos_incluidos = []
                print("================================================================")
                
                
                # Agregar productos al combo
                while True:
                    print("================================================================")
                    
                    print("\n¿Que desea hacer?")
                    agregar_producto_al_combo = input('"1". agregar un producto existente al combo \n"2".  Agregar Producto nuevo al combo \nEscribir "salir" para regresar \n')
                    print("================================================================")
                    
                    if agregar_producto_al_combo.lower() == '1':
                        try:
                            print("================================================================")
                            
                            print("Que producto desea agregar?")
                            print("1. Gabinete")
                            print("2. Monitor")
                            print("3. Tarjeta Grafica")
                            print("4. Procesador")
                            print("5. Producto Nuevo")
                            print("              ")
                            opcion = int(input("Ingrese una opcion: "))
                            print("================================================================")   
                            
                            print("")
                        except:
                            print("Opcion no válida")
                        else:
                            match(opcion):
                                case 1:
                                    i = int(1)
                                    for gabinete in gabinetes:
                                        print(f'{i}. {gabinete}')
                                        print("")
                                        i += int(1)
                                
                                    opcionIndice = int(input("Ingrese el indice del articulo que desea agregar: "))
                                    opcionIndice -= int(1)
                                    productos_incluidos.append(gabinetes[opcionIndice])
                                    
                                    print("\nProductos Incluidos")
                                    for producto in productos_incluidos:
                                        print(producto)
                                    
                                case 2:
                                    i = int(1)
                                    for monitor in monitores:
                                        print(f'{i}. {monitor}')
                                        print("")
                                        i += int(1)
                                
                                    opcionIndice = int(input("Ingrese el indice del articulo que desea agregar: "))
                                    opcionIndice -= int(1)
                                    productos_incluidos.append(monitores[opcionIndice])
                                    
                                    print("\nProductos Incluidos")
                                    for producto in productos_incluidos:
                                        print(producto)
                                    
                                case 3:
                                    i = int(1)
                                    for tarjetaGrafica in tarjetasGraficas:
                                        print(f'{i}. {tarjetaGrafica}')
                                        print("")
                                        i += int(1)
                                
                                    opcionIndice = int(input("Ingrese el indice del articulo que desea agregar: "))
                                    opcionIndice -= int(1)
                                    productos_incluidos.append(tarjetasGraficas[opcionIndice])

                                    print("\nProductos Incluidos")
                                    for producto in productos_incluidos:
                                        print(producto)
                                    
                                case 4:
                                    i = int(1)
                                    for procesador in procesadores:
                                        print(f'{i}. {procesador}')
                                        print("")
                                        i += int(1)
                                
                                    opcionIndice = int(input("Ingrese el indice del articulo que desea agregar: "))
                                    opcionIndice -= int(1)
                                    productos_incluidos.append(procesadores[opcionIndice])

                                    print("\nProductos Incluidos")
                                    for producto in productos_incluidos:
                                        print(producto)

                                case default:
                                    print("Opcion Invalida")
                                        
                    elif agregar_producto_al_combo.lower() == '2':
                        # Llamas a la función para agregar un producto individual
                        producto_incluido = agregarProducto()
                        # Agregas el producto individual a la lista de productos incluidos en el combo
                        productos_incluidos.append(producto_incluido)
                        
                    else:
                        print("\nSaliendo..")
                        break
                    

                
                    
                producto_combo = ProductoCombo(nombreCombo, codigoCombo, cantidad_en_inventario, fecha_de_compra, productos_incluidos)
                combos.append(producto_combo)

                # Imprime la información del combo utilizando el método __str__
                print("\nInformación del combo agregado:")
                print(producto_combo)
                print(producto_combo.precio_combo_descuento())
                print("")
                
                    
                    
                """except:
                    print("Por favor, ingrese un valor numérico válido para el precio del combo.")"""
            case 7:
                print("Salir...") 
            case default:
                print("Opcion Invalida")

#Consulta productos mediante codigo
def ConsultarProducto():
    pass

def generarFactura(cliente, productosPorComprar ):
    
    controlEnvios = ["Enviado", "Recibido", "Transito"]
    i = int(1)
    for vendedor in vendedores:
        print(f'{i}. {vendedor}')
        print("")
        i += int(1)
    
    
    opcionIndice = int(input("¿Quien realizo la venta? "))
    opcionIndice -= int(1)
    vendedorActual = vendedores[opcionIndice]
    controlEnvio = random.choice(controlEnvios)
    fechaVenta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subtotal =  sum(producto._precio for producto in productosPorComprar)
    total = subtotal * 1.12
    codigoFactura = GenerarCodigo()
  
    
    factura = Factura(cliente, productosPorComprar, vendedorActual, controlEnvio, fechaVenta, subtotal, total, codigoFactura )
    
    factura.imprimirFactura()
        

clientes = []
empleados = []
vendedores = []
gabinetes = []
monitores = []
procesadores = []
tarjetasGraficas = []
productosNuevos = []
combos = []
inventario = [gabinetes, monitores, procesadores, tarjetasGraficas, combos, productosNuevos]
productosPorComprar = []

#GENTE QUE YA EXISTE DENTRO DEL PROGRAMA

#Cliente(nombre, apellido, identidad, telefono, rtn)
cliente1 = Cliente("Pamela", "Gomez", "123456789", "27831234", "1234567890")
clientes.append(cliente1)
#Administrador (nombre, apellido, identidad, telefono, no_empleado,salario)
admin1 = Administrador("Michael", "Scott", "101112131415", "27835678", "001", 50000)
empleados.append(admin1)
#Comprador(nombre, apellido, identidad, telefono, no_empleado,salario)
comprador1 = Comprador("Carlos", "Costly", "1617181920", "27831011", "002", 35000)
empleados.append(comprador1)
#Consultor(nombre, apellido, identidad, telefono, no_empleado,salario, consultas hechas)
consultor1 = Consultor("Maki", "Zenin", "2122232425", "27831213", "003", 20000, 20)
empleados.append(consultor1)
#Vendedor(nombre, apellido, identidad, telefono, no_empleado, salario, ventas realizadas)
vendedor1 = Vendedor("Terre", "Neitor", "2627282930", "27831415", "004", 17000, 50)
vendedores.append(vendedor1)

#Gabinetes existentes en el programa
gabinete1 = Gabinete("Gabinete", 4251,  "4000D Airflow", "Corsair", "Corsair", "B08C7BGV3D", 79.98, 60, "18/05/2021", "15/09/2020", "Corsair Gaming, Inc.", "Acero, vidrio templado, plástico", "Negro", "Mid Tower", 17.31, "17,83 x 9,06 x 18,35", "120 Milímetros")
gabinete2 = Gabinete("Gabinete", 1825,  "Y60", "HYTE", "HYTE", "B0BVJ4ZFPZ", 169.99, 50, "25/06/2023", "15/03/2022", "HYTE, Inc.", "Vidrio templado", "Blanco Nieve", "Mid Tower", 22, "17,95 x 11,22 x 18,19 ", "120 Milímetros")
gabinetes.append(gabinete1)
gabinetes.append(gabinete2)

#Monitores existentes en el programa
monitor1 = Monitor("Monitor", 1414,  "Pro MP251", "MSI", "MSI", "A4AGF5XFDV", 79.99, 240, "20/11/2023", "11/10/2023", "MSI, Inc.", "1920 x 1080", "25 Pulgadas", "HDMI", "100 Hz")
monitor2 = Monitor("Monitor", 1423,  "Odyssey G30A", "SAMSUNG", "SAMSUNG", "LS27AG302NNXZA", 169.99, 210, "19/07/2022", "21/06/2021", "Samsung Electronics Co., Ltd.", "1920 x 1080", "27 Pulgadas", "	Bluetooth, wifi, HDMI", "144 Hz")
monitores.append(monitor1)
monitores.append(monitor2)

#Procesadores existentes en el programa
procesador1 = Procesador("Procesador", 2524,  "Core i7-12700KF", "Intel", "Intel Corporation", "B09FXKHN7M", 199.00, 130, "16/05/2022", "04/11/2021", "Intel Corporation", "Doceava Generación", "12 Nucleos", "25MB", "LGA 1700", "3.00 Hz")
procesador2 = Procesador("Procesador", 2726, "Ryzen 9-5900X", "AMD", "AMD", "B08164VTWH", 288.99, 180, "16/05/2022", "08/10/2020", "Advanced Micro Devices, Inc.", "Quinta generacion", "12 Nucleos", "64MB", "Socket AM4", "4,8 GHz")
procesadores.append(procesador1)
procesadores.append(procesador2)

#Tarjetas Graficas en el programa
tarjeta_grafica1 = TarjetaGrafica("Tarjetas Graficas", 2429,  "ROG Strix NVIDIA GeForce RTX 4070 Ti OC Edition", "ASUS", "ASUS", "B0BQTVQQP4", 899.99, 140, "01/03/2023", "05/01/2023", "Nvidia Corporation", "12GB", "HDMI", "2790 MHz")
tarjeta_grafica2 = TarjetaGrafica("Tarjetas Graficas", 2437,  "Radeon RX 7700 XT", "AMD", "Power Color", "B0CFP6F859", 429.99, 90, "01/11/2023", "06/09/2023", "Advanced Micro Devices, Inc.", "12GB", "HDMI, Mini DisplayPort", "2226 MHz")
tarjetasGraficas.append(tarjeta_grafica1)
tarjetasGraficas.append(tarjeta_grafica2)

#Productos-Individuales que ya existen en el inventario
producto_individual1 = ProductoIndividual("Mouse inalámbrico", 1234,  "G305", "Logitech LIGHSTPEED", "Logitech", "910-005273", 43.75, 250, "23/09/2023", "06/2016", "Logitech, Inc.")
producto_individual2 = ProductoIndividual("Teclado mecánico", 5678,  "G715", "Logitech LIGTHSYNC TKL", "Logitech", "920-010684", 212, 140, "15/08/2023", "28/08/2022", "Logitech, Inc")
producto_individual3 = ProductoIndividual("Memoria RAM", 2345,  "Corsair", "VENGEANCE LPX DDR4", "Corsair", "B0143UM4TC", 67.99, 140, "01/04/2019", "15/06/2021", "Corsair Gaming, Inc.")
productosNuevos.append(producto_individual1)
productosNuevos.append(producto_individual2)
productosNuevos.append(producto_individual3)

#Productos -Combo que ya existen en el programa
producto_combo1 = ProductoCombo("ComboNavideño", 2323, 15, "13/04/2022",  [producto_individual1])
producto_combo2 = ProductoCombo("ComboBlackFriday", 2327, 20, "24/12/2023",  [monitor1, producto_individual1, producto_individual2])
combos.append(producto_combo1)
combos.append(producto_combo2)

while True:
   
    try:
        print("================================================================")
        
        print("Pagina de LOGIN:")
        print("Elija la opcion adecuada a sus necesidades:")
        print("1. Si usted es cliente ")
        print("2. Si usted es un empleado ")
        print("3. Salir")
        opcion=int(input("Elija una opcion: "))
        print("================================================================")
        
        print("")
    except:
        print("Opcion Invalida")    
    else:
        match(opcion):
            case 1:
                print("Cliente")
                agregar_cliente()
                for cliente in clientes:
                    print (cliente)
                    
                clienteActual = cliente
                
                try:    
                    print("================================================================")
                    
                    print("¿Que desea hacer?")
                    print("1. seleccionar productos a comprar")
                    print("2. Consultar por algun producto mediante codigo de producto")
                    print("3. Ver inventario")
                    opcion = int(input("Ingrese una opcion: "))
                    print("================================================================\n")
                    
                except:
                    pass
                else:
                    match(opcion):
                        case 1:
                            seguir = True
                    while(seguir):
                        try:
                            print("================================================================")
                            
                            print("Qué desea comprar")
                            print("1. Gabinete")
                            print("2. Monitor")
                            print("3. Tarjetas Graficas")
                            print("4. Procesadores")
                            print("5. Otros Productos")
                            print("6. Combos")
                            print("7. Terminar Compra")
                            opcion = int(input("Qué desea realizar? "))
                            print("================================================================")
                            
                        except:
                            print("Ingrese Una Opcion")
                        else:
                            match(opcion):
                                case 1:
                                    print("================================================================")
                                    
                                    i = int(1)
                                    for gabinete in gabinetes:
                                        print(f'{i}. {gabinete}')
                                        print("")
                                        i += int(1)
                                
                                    opcionIndice = int(input("Ingrese el indice del articulo que desea agregar: "))
                                    opcionIndice -= int(1)
                                    productosPorComprar.append(gabinetes[opcionIndice])
                                    
                                    print("\nProductos Incluidos")
                                    for producto in productosPorComprar:
                                        print(producto)
                                    print("================================================================")
                                    
                                case 2:
                                    print("================================================================")
                                    i = int(1)
                                    for monitor in monitores:
                                        print(f'{i}. {monitor}')
                                        print("")
                                        i += int(1)
                                        
                                    opcionIndice = int(input("Ingrese el indice del articulo que desea agregar: "))
                                    opcionIndice -= int(1)
                                    productosPorComprar.append(monitores[opcionIndice])
                                    
                                    print("\nProductos Incluidos")
                                    for producto in productosPorComprar:
                                        print(producto)
                                    print("================================================================")
                                    
                                case 3:
                                    print("================================================================")
                                    
                                    i = int(1)
                                    for tarjetaGrafica in tarjetasGraficas:
                                        print(f'{i}. {tarjetaGrafica}')
                                        print("")
                                        i += int(1)
                                
                                    opcionIndice = int(input("Ingrese el indice del articulo que desea agregar: "))
                                    opcionIndice -= int(1)
                                    productosPorComprar.append(tarjetasGraficas[opcionIndice])

                                    print("\nProductos Incluidos")
                                    for producto in productosPorComprar:
                                        print(producto)
                                    
                                    print("================================================================")
                                    
                                case 4:
                                    print("================================================================")
                                    
                                    i = int(1)
                                    for procesador in procesadores:
                                        print(f'{i}. {procesador}')
                                        print("")
                                        i += int(1)
                                
                                    opcionIndice = int(input("Ingrese el indice del articulo que desea agregar: "))
                                    opcionIndice -= int(1)
                                    productosPorComprar.append(procesadores[opcionIndice])

                                    print("\nProductos Incluidos")
                                    for producto in productosPorComprar:
                                        print(producto)
                                        
                                    print("================================================================")
                                        
                                case 5:
                                    print("================================================================")
                                    
                                    i = int(1)
                                    for producto in productosNuevos:
                                        print(f'{i}. {producto}')
                                        print("")
                                        i += int(1)
                                
                                    opcionIndice = int(input("Ingrese el indice del articulo que desea agregar: "))
                                    opcionIndice -= int(1)
                                    productosPorComprar.append(productosNuevos[opcionIndice])

                                    print("\nProductos Incluidos")
                                    for producto in productosPorComprar:
                                        print(producto)
                                        
                                    print("================================================================")
                                        
                                case 6:
                                    print("================================================================")
                                    
                                    i = int(1)
                                    for combo in combos:
                                        print(f'{i}. {combo}')
                                        print("")
                                        i += int(1)
                                
                                    opcionIndice = int(input("Ingrese el indice del articulo que desea agregar: "))
                                    opcionIndice -= int(1)
                                    productosPorComprar.append(combos[opcionIndice])

                                    print("\nProductos Incluidos")
                                    for producto in productosPorComprar:
                                        print(producto)
                                        
                                    print("================================================================")
                                        
                                case 7:
                                    generarFactura(clienteActual, productosPorComprar)
                                    
                                
                                case default:
                                    print("Opcion Invalida")
                    
            
            case 2:
                print("Empleado")
                seguir = True
                while(seguir):
                    noEmpleado = input("Ingrese su numero de empleado para iniciar sesion: ")
                    for empleado in empleados:
                        if noEmpleado == empleado.no_empleado:
                            print(empleado)
                            acceso = empleado.nivelAcceso
                            while(seguir):
                                match(acceso):
                                    case 1:
                                        print("================================================================")
                                        print("administrador")
                                        print("Funcionalidades de administrador: ")
                                        print("1. *** Contratar nuevo empleado ***")
                                        print("2. *** Ver todos los empleados ***")
                                        print("3. *** Cerrar sesion ***")
                                        seleccion = int(input("***Ingrese que desea hacer***: "))
                                        print("================================================================")   
                                        print("")
                                        
                                        match(seleccion):
                                            case 1:
                                                
                                                print("================================================================")
                                                ContratarPersonal()
                                                print("================================================================")
                                            case 2:
                                                print("================================================================")
                                                
                                                for empleado in empleados:
                                                    print(empleado)
                                                print("================================================================")
                                                    
                                            case 3:
                                                seguir = False
                                                break
                                            
                                    case 2:
                                        print("Comprador")
                                        agregarProducto()
                                        
                                    case 3:
                                        print("Consultor")
                                        "consultar existencia"
                                        "consultar por codigo de producto"
                                        pass
                                    case 4:
                                        print("Vendedor")
                                        pass

            case 3:
                print("Gracias por su visita ☻")
                break
            
            case default:
                print("Opcion invalida1")