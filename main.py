from Persona import Persona
from Personal import Personal
from Cliente import Cliente
from Empleados.Administrador import Administrador
from Empleados.Comprador import Comprador
from Empleados.Consultor import Consultor
from Empleados.Vendedor import Vendedor



print("Dios mio ")

#MEMO: Esta funcion se encarga de agregar clientes o de localizar clientes ya existentes en caso de tener la misma identidad
def agregar_cliente():
    try:
        identidad = input("Ingrese su numero de identidad: ")
        # si el cliente ya existe no va a crear uno nuevo
        for cliente_existente in clientes:
            if cliente_existente.identidad == identidad:
                print(f"El cliente con la identidad {identidad} ya existe: ")
                print("¡Bienvenido de nuevo! " + cliente_existente.nombre+" "+cliente_existente.apellido) #NOTA: agregar funcionalidad para utilizar este cliente en vez de imprimirlo
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
#lista de cuentas para acceder a las funcionalidades especificas
cuentas_usuario = [
    {"usuario":"admin", "contrasena":"123"},
    {"usuario":"comprador", "contrasena":"123"},
    {"usuario":"consultor", "contrasena":"123"},
    {"usuario":"vendedor", "contrasena":"123"}

]
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
        #NOTA AGREGAR: Lista de productos o tal, lo primero que le va a salir al cliente al ingresar a la pagina

    elif opcion =="2":
        print("Empleado")
        usuario_ingresado = input("Ingrese su nombre de usuario: ") 
        contrasena_ingresado = input("Ingrese su contrasena: ") 
        iniciar_sesion=None
        for cuenta in cuentas_usuario:
            if cuenta["usuario"]== usuario_ingresado and cuenta["contrasena"]== contrasena_ingresado:
                iniciar_sesion=True
                break

        if iniciar_sesion:
            #NOTA: borrar el bobeito
            #NOTA: agregar funcionalidad de identificar tipo de empleado y actuar en consecuencia
            print("***************************")
            print("¡Hola de nuevo! Bienvenido mi rey")
            print("***************************")
            sesion_iniciada=True
            while sesion_iniciada==True:
                
                if usuario_ingresado== "admin":
                    print("Funcionalidades de administrador: ")
                    print("1. *** Contratar nuevo empleado ***")
                    print("2. *** Ver todos los empleados ***")
                    print("3. *** Cerrar sesion ***")
                    seleccion=input("***Ingrese que desea hacer***: ")
                    
                    usando_sistema=True
                    while usando_sistema== True:
                        if seleccion =="1":
                            empleado_nuevo = ContratarPersonal()
                            usando_sistema=False
                        elif seleccion =="2":
                            #NOTA: Hay un bug, que si la lista esta vacia hara un loop jaja
                            print("Lista de empleados:")
                            for empleado in empleados:
                                 print (empleado)
                                 usando_sistema=False




                        elif seleccion=="3":
                            print("¡Nos vemos!")
                            usando_sistema=False
                            iniciar_sesion=False
                            sesion_iniciada=False
                            break
                            
                    
                    #break
                elif usuario_ingresado == "comprador":
                    print("Funcionalidades del comprador")
                    #NOTA: agregar funcionalidad del comprador
                    break
                elif usuario_ingresado == "consultor":
                    print("Funcionalidades del consultor")
                    #NOTA: agregar funcionalidad del consultor
                    break
                elif usuario_ingresado == "vendedor":
                    print("Funcionalidades del vendedor")
                    #NOTA: agregar funcionalidad del vendedor
                    break

        else:
            #NOTA: borrar el bobeito
            print("***************************")
            print("QUIEN SOS IDENTIFICATE BIEN")
            print("***************************")
        
        #Solo puede contratar si es un admin
        #empleado_nuevo = ContratarPersonal()

    #Imprimir todo NOTA: solo para testing eliminar despues
    elif opcion =="21":
        
        print("Listade clientes:")
        for cliente in clientes:
            print (cliente)
    
    elif opcion =="3":
        break




""" NOTA: Esto no sirve ya, borrarlo despues
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
"""