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
        identidad = input("Ingrese su numero de identidad: ")
        # si el cliente ya existe no va a crear uno nuevo
        for cliente_existente in clientes:
            if cliente_existente.identidad == identidad:
                print(f"El cliente con la identidad {identidad} ya existe: ")
                print(cliente_existente) #agregar funcionalidad para utilizar este cliente en vez de imprimirlo
                # Salir  si el cliente ya existe
                return 
        nombre = input("Ingrese su primer nombre: ")
        apellido = input("Ingrese su apellido: ")
        telefono = input("Ingrese su numero de telefonoe: ")
        rtn = input("Ingrese su numero de rtn: ")


        cliente = Cliente(nombre, apellido, identidad, telefono, rtn)
        clientes.append(cliente)
    except:
        print("Ingrese un valor correcto")


def ContratarPersonal():
    try:
        no_empleado = input("Ingrese el numero de empleado: ")
        # si el empleado ya existe no va a crear uno nuevo
        for empleado_existente in empleados:
            if empleado_existente.no_empleado == no_empleado:
                print(f"El empleado con el numero de empleado {no_empleado} ya existe: ")
                print(empleado_existente) #agregar funcionalidad para utilizar este cliente en vez de imprimirlo
                # Salir  si el empleado ya existe
                return 
        nombre = input("Ingrese el nombre del empleado: ")
        apellido = input("Ingrese el apellido del empleado: ")
        identidad = input("Ingrese la identidad del empleado: ")
        telefono = input("Ingrese el telefono del empleado: ")
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
    print("Pagina de LOGIN:")
    print("Elija la opcion adecuada a sus necesidades:")
    print("1. Si usted es cliente ")
    print("2. Si usted es un empleado ")
    print("21. Para imprimir todos los clientes y empleados ** Nota: Solo para testing**")
    print("3. Salir")
    opcion=input()
    if opcion =="1":
        print("Cliente")
        cliente_nuevo = agregar_cliente()

    elif opcion =="2":
        print("Empleado")
        empleado_nuevo = ContratarPersonal()

    #Imprimir todo NOTA: solo para testing eliminar despues
    elif opcion =="21":
        print("Listade empleados:")
        for empleado in empleados:
            print (empleado)
        print("Listade clientes:")
        for cliente in clientes:
            print (cliente)
    
    elif opcion =="3":
        break





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
