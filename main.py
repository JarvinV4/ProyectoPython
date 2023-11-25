from Persona import Persona
from Personal import Personal
from Cliente import Cliente
from Empleados.Administrador import Administrador
from Empleados.Comprador import Comprador
from Empleados.Consultor import Consultor
from Empleados.Vendedor import Vendedor



print("Dios mio ")


def agregar_cliente():
    try:
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        identidad = input("Ingrese la identidad del cliente: ")
        telefono = input("Ingrese el telefono del cliente: ")
        rtn = input("Ingrese el rtn del cliente: ")

        cliente = Cliente(nombre, apellido, identidad, telefono, rtn)
        clientes.append(cliente)
    except:
        print("Ingrese un valor correcto")


def ContratarPersonal():
    try:
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
    except:
        print("Ingrese un valor numerico para el salario")

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
        
    elif opcion == "2":
        empleado_nuevo = ContratarPersonal()
        

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
