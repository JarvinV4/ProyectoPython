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

"""from Productos.Producto import Producto
from Productos.ProductoCombo import Producto_combo
from Productos.Gabinete import Gabinete
from Productos.Monitor import Monitor
from Productos.Procesador import Procesador
from Productos.TarjetaVideo import TarjetaVideo"""

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
                        empleados.append(empleado)
                        break
                    
                    case default:
                        print("Opcion invalida")
                        break  
        except:
            print("Datos Invalidos")  
      
def agregarProducto():
    try:
        print("Que producto desea agregar?")
        print("1. Monitor")
        print("2. Gabinete")
        print("3. Tarjeta Grafica")
        print("4. Procesador")
        print("5. Producto Nuevo")
        print("6. Agregar Combo")
        opcion = int(input("Ingrese una opcion: "))
    except:
        print("Opcion Invalida")
        
        match(opcion):
            case 1:
                pass
            case 2:
                pass
            case 3:
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
                producto = TarjetaGrafica(codigo_producto, nombre_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor, vram, salida, frecuencia_gpu)
                productos.append(producto)
                for producto in productos:
                    print(producto)
            case 4:
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
                producto = Procesador(codigo_producto, nombre_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor, generacion, nucleos, cache, zocalo_cpu, frecuencia_cpu)
                productos.append(producto)
                for producto in productos:
                    print(producto)
            case 5:
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
                nuevo_producto = ProductoIndividual(nombre_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)
                productoIndividual.append(nuevo_producto)
            case 6:
                print("Ingresar datos de Producto Combo")
                codigoProducto = GenerarCodigo()
                nombre_producto = input("Nombre del Combo: ")
                modelo = input("Modelo del combo: ")
                marca = input("Marca del combo: ")
                fabricante = input("Fabricante del combo: ")
                numero_de_serie = input("Numero de serie del combo: ")
                precio = input("Precio del combo: ")
                cantidad_en_inventario = input("Cantidad en inventario: ")
                fecha_de_compra = input("Fecha de compra: ")
                fecha_de_fabricacion = input("Fecha de fabricion: ")
                proveedor = input("Proveedor: ")                
                productos_incluidos = []
                producto_combo = ProductoCombo(modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor, productos_incluidos)
                # Agregar productos al combo
                while True:
                    agregar_producto_al_combo = input("¿Desea agregar un producto al combo? (si/no): ")
                    if agregar_producto_al_combo.lower() == 'si':
                        # Llamas a la función para agregar un producto individual
                        producto_incluido = agregarProducto()
                        # Agregas el producto individual a la lista de productos incluidos en el combo
                        productos_incluidos.append(producto_incluido)
                    else:
                        break

                combos.append(producto_combo)
            case default:
                print("Opcion Invalida")




def ConsultarProducto():
    pass

    



clientes = []
empleados = []
combos = []
productoIndividual = []
inventario = []

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
empleados.append(vendedor1)





while True:
    try:
        print("Pagina de LOGIN:")
        print("Elija la opcion adecuada a sus necesidades:")
        print("1. Si usted es cliente ")
        print("2. Si usted es un empleado ")
        print("3. Para imprimir todos los clientes y empleados ** Nota: Solo para testing**")
        print("4. Salir")
        
        opcion=int(input("Eliga una opcion: "))
        
        match(opcion):
            case 1:
                print("Cliente")
                agregar_cliente()
                for cliente in clientes:
                    print (cliente)
            
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
                                        print("administrador")
                                        print("Funcionalidades de administrador: ")
                                        print("1. *** Contratar nuevo empleado ***")
                                        print("2. *** Ver todos los empleados ***")
                                        print("3. *** Cerrar sesion ***")
                                        seleccion = int(input("***Ingrese que desea hacer***: "))
                                        
                                        match(seleccion):
                                            case 1:
                                                ContratarPersonal()
                                            case 2:
                                                for empleado in empleados:
                                                    print(empleado)
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
                for producto in productos:
                    print(producto)
            
            case default:
                print("Opcion invalida1")
    except:
            print("Opcion Invalida")    
