from abc import ABC,abstractmethod

class Persona():
    def __init__(self, nombre, apellido, identidad, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.identidad = identidad
        self.telefono = telefono
class Cliente(Persona):
    def __init__(self, nombre, apellido, identidad, telefono, rtn):
        super().__init__(nombre, apellido, identidad, telefono)

        self.rtn = rtn

    def __str__(self):
        return (f"Cliente: {self.nombre} {self.apellido}, ID: {self.identidad}, Teléfono: {self.telefono}, RTN: {self.rtn}")

    def SeleccionarProductos(self):
        print("A")
class Personal(Persona, ABC):
    def __init__(self, nombre, apellido, identidad, telefono, no_empleado, salario):
        super().__init__(nombre, apellido, identidad, telefono)
        self.no_empleado = no_empleado
        self.salario = salario
    
    @abstractmethod
    def CalculoSalario(self):
        pass
class Administrador(Personal):
    def __init__(self, nombre, apellido, identidad, telefono, no_empleado, salario):
        super().__init__(nombre, apellido, identidad, telefono, no_empleado, salario)


    def CalculoSalario(self):
        return super().CalculoSalario()
    
    def __str__(self):
        return (f"Administrador: {self.nombre} {self.apellido}, ID: {self.identidad}, Telefono: {self.telefono}, No. Empleado: {self.no_empleado}, Salario: {self.salario}")
    
class Comprador(Personal):
    def __init__(self, nombre, apellido, identidad, telefono, no_empleado, salario):
        super().__init__(nombre, apellido, identidad, telefono, no_empleado, salario)

    def ComprarInventario():
        print("Comprando producot")


    def AgregarNuevoProducto():
        print("Agregar nuevo producto")

    def CalculoSalario(self):
        return super().CalculoSalario()
    
    def __str__(self):
        return (f"Comprador: {self.nombre} {self.apellido}, ID: {self.identidad}, Telefono: {self.telefono}, No. Empleado: {self.no_empleado}, Salario: {self.salario}")


class Consultor(Personal):
    def __init__(self, nombre, apellido, identidad, telefono, no_empleado, salario, historial_consultas):
        super().__init__(nombre, apellido, identidad, telefono, no_empleado, salario)
        self.historial_consultas = historial_consultas


    def CalculoSalario(self):
        return super().CalculoSalario()
    
    def __str__(self):
        return (f"Consultor: {self.nombre} {self.apellido}, ID: {self.identidad}, Telefono: {self.telefono}, No. Empleado: {self.no_empleado}, Salario: {self.salario}")
    
class Vendedor(Personal):
    def __init__(self, nombre, apellido, identidad, telefono, no_empleado, salario, ventasRealizadas):
        super().__init__(nombre, apellido, identidad, telefono, no_empleado, salario)
        self.ventasRealizadas=ventasRealizadas

    def generarFactura(self):
        print("facrura")

    def VenderProducto(self):
        print("Vendr")

    def CalculoSalario(self):
        return super().CalculoSalario()
    
    def __str__(self):
        return (f"Vendedor: {self.nombre} {self.apellido}, ID: {self.identidad}, Telefono: {self.telefono}, No. Empleado: {self.no_empleado}, Salario: {self.salario}")




def agregar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    identidad = input("Ingrese la identidad del cliente: ")
    telefono = input("Ingrese el telefono del cliente: ")
    rtn = input("Ingrese el rtn del cliente: ")

    cliente = Cliente(nombre, apellido, identidad, telefono, rtn)
    clientes.append(cliente)



def ContratarPersonal():
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    identidad = input("Ingrese la identidad del empleado: ")
    telefono = input("Ingrese el telefono del empleado: ")
    no_empleado = input("Ingrese el numero de empleado: ")
    salario = float(input("Ingrese el salario del empleadp: "))
    print("¿Cual sera el cargo de este empleado?")
    print("1. Comprador")
    print("2. Consultor")
    print("3. Vendedor")
    opcion=input("Seleccione una opcion ")
    while True:

        if opcion =="1":
            empleado = Comprador(nombre, apellido, identidad, telefono, no_empleado, salario)
            empleados.append(empleado)
            break
        elif opcion =="2":
            empleado = Consultor(nombre, apellido, identidad, telefono, no_empleado,salario, None)
            empleados.append(empleado)
            break
        elif opcion =="3":
            empleado = Vendedor(nombre, apellido, identidad, telefono, no_empleado, salario, None)
            empleados.append(empleado)
            break
        else:
            print("Seleccione una de las opciones disponibles")

clientes =[]
empleados =[]



while True:
    print("1. Agregar cliente")
    print("2. Agregar empleado")
    print("3. Salir")
    #para ver si se almacenan correctamente
    print("4 Ver empleados")
    print("5 ver clientes")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        cliente_nuevo = agregar_cliente()
        print("Cliente agregado")
    elif opcion == "2":
        empleado_nuevo = ContratarPersonal()
        print("Empleado agregado:")

    elif opcion == "3":
        print("Adio")
        break

    elif opcion =="4":
        print("Listade empleados:")
        for empleado in empleados:
            print (empleado)

    elif opcion =="5":
        print("Listade clientes:")
        for cliente in clientes:
            print (cliente)

    else:
        print("Seleccione una de las opciones disponibles")