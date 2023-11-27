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

def ConsultarProducto():
    pass

def AgregarProducto():
    pass
    



clientes = []
empleados = []
Inventario = []

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

#PRODUCTOS QUE YA EXISTEN EN EL PROGRAMA

<<<<<<< Updated upstream
#Producto(codigo_producto, nombre_producto, modelo, marca, fabricante, numero_de_serie, precio, cantidad_en_inventario, fecha_de_compra, fecha_de_fabricacion, proveedor)
#Gabinetes existentes en el programa
gabinetes1 = Gabinete(4251, "Gabinete", "4000D Airflow", "Corsair", "Corsair", "B08C7BGV3D", 79.98, 60, "18/05/2021", "15/09/2020", "Corsair Gaming, Inc.", "Acero, vidrio templado, plástico", "Negro", "Mid Tower", 17.31, "17,83 x 9,06 x 18,35", "120 Milímetros")
gabinetes2 = Gabinete(1825, "Gabinete", "Y60", "HYTE", "HYTE", "B0BVJ4ZFPZ", 169.99, 50, "25/06/2023", "15/03/2022", "HYTE, Inc.", "Vidrio templado", "Blanco Nieve", "Mid Tower", 22, "17,95 x 11,22 x 18,19 ", "120 Milímetros")

#Monitores existentes en el programa
monitores1 = Monitor(1414, "Monitor", "Pro MP251", "MSI", "MSI", "A4AGF5XFDV", 79.99, 240, "20/11/2023", "11/10/2023", "MSI, Inc.", "1920 x 1080", "25 Pulgadas", "HDMI", "100 Hz")
monitores2 = Monitor(1423, "Monitor", "Odyssey G30A", "SAMSUNG", "SAMSUNG", "LS27AG302NNXZA", 169.99, 210, "19/07/2022", "21/06/2021", "Samsung Electronics Co., Ltd.", "1920 x 1080", "27 Pulgadas", "	Bluetooth, wifi, HDMI", "144 Hz")

#Procesadores existentes en el programa
procesador1 = Procesador(2524, "Procesador", "Core i7-12700KF", "Intel", "Intel Corporation", "B09FXKHN7M", 199.00, 130, "16/05/2022", "04/11/2021", "Intel Corporation", "Doceava Generación", "12 Nucleos", "25MB", "LGA 1700", "3.00 Hz")
procesador2 = Procesador(2726, "Procesador", "Ryzen 9-5900X", "AMD", "AMD", "B08164VTWH", 288.99, 180, "16/05/2022", "08/10/2020", "Advanced Micro Devices, Inc.", "Quinta generacion", "12 Nucleos", "64MB", "Socket AM4", "4,8 GHz")

#Tarjetas Graficas en el programa
tarjeta_grafica1 = TarjetaGrafica(2429, "Tarjetas Graficas", "ROG Strix NVIDIA GeForce RTX 4070 Ti OC Edition", "ASUS", "ASUS", "B0BQTVQQP4", 899.99, 140, "01/03/2023", "05/01/2023", "Nvidia Corporation", "12GB", "HDMI", "2790 MHz")
tarjeta_grafica2 = TarjetaGrafica(2437, "Tarjetas Graficas", "Radeon RX 7700 XT", "AMD", "Power Color", "B0CFP6F859", 429.99, 90, "01/11/2023", "06/09/2023", "Advanced Micro Devices, Inc.", "12GB", "HDMI, Mini DisplayPort", "2226 MHz")

#Productos-Individuales que ya existen en el inventario
producto_individual1 = ProductoIndividual(1234, "Mouse inalámbrico", "G305", "Logitech LIGHSTPEED", "Logitech", "910-005273", 43.75, 250, "23/09/2023", "06/2016", "Logitech, Inc.")
producto_individual2 = ProductoIndividual(5678, "Teclado mecánico", "G715", "Logitech LIGTHSYNC TKL", "Logitech", "920-010684", 212, 140, "15/08/2023", "28/08/2022", "Logitech, Inc")
producto_individual3 = ProductoIndividual(2345, "Memoria RAM", "Corsair", "VENGEANCE LPX DDR4", "Corsair", "B0143UM4TC", 67.99, 140, "01/04/2019", "15/06/2021", "Corsair Gaming, Inc.")

#Productos -Combo que ya existen en el programa
combos = [producto_individual1, producto_individual2]
producto_combo1 = ProductoCombo(2323, "ComboNavideño","ComboModelo", "ComboMarca", "ComboFabricante", "CMB0001", 579.99, 15, "13/04/2022", "15/12/2022", "ComboProveedor", [producto_individual1])
producto_combo2 = ProductoCombo(2327, "ComboBlackFriday", "ComboModelo","ComboMarca", "ComboFabricante", "CMB0002", 349.99, 20, "24/12/2023", "23/12/2023", "ComboProveedor", [monitores1, producto_individual1, producto_individual2])



=======
>>>>>>> Stashed changes
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
                                        
                                        pass
                                    case 3:
                                        print("Consultor")
                                        pass
                                    case 4:
                                        print("Vendedor")
                                        pass

            case 3:
                seguir = False
            
            case default:
                print("Opcion invalida")
    except:
            print("Opcion Invalida")    
