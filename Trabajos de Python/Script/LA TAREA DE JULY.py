
# Descripcion: proyecto final
# Programadora: Juliana Buitrago
# Fecha: 20/03/2023
# Version: 3.0

# Menu de opciones
# Menu de Clientes
def opcion_Menu_de_clientes():
    print("Ha seleccionado Menu de Clientes")

clientes = {}

def agregar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    clientes[nombre] = {"telefono": telefono}
    print("Cliente agregado con éxito.")

def modificar_cliente():
    nombre = input("Ingrese el nombre del cliente a modificar: ")
    if nombre in clientes:
        telefono = input("Ingrese el nuevo teléfono del cliente: ")
        clientes[nombre]["telefono"] = telefono
        print("Cliente modificado con éxito.")
    else:
        print("El cliente no existe.")

def borrar_cliente():
    nombre = input("Ingrese el nombre del cliente a borrar: ")
    if nombre in clientes:
        del clientes[nombre]
        print("Cliente borrado con éxito.")
    else:
        print("El cliente no existe.")
    
def borrar_todos_los_clientes():
    clientes.clear()
    print("Todos los clientes han sido borrados con éxito.")
# Menu de Productos
def opcion_Menu_de_Productos():
    print("Ha seleccionado Menu de Productos")
productos = {}

# Función para agregar un producto
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    productos[nombre] = {"descripcion": descripcion, "precio": precio}
    print("Producto agregado con éxito")

# Función para modificar un producto
def modificar_producto():
    nombre = input("Ingrese el nombre del producto a modificar: ")
    if nombre in productos:
        descripcion = input("Ingrese la nueva descripción del producto: ")
        precio = float(input("Ingrese el nuevo precio del producto: "))
        productos[nombre] = {"descripcion": descripcion, "precio": precio}
        print("Producto modificado con éxito")
    else:
        print("Producto no encontrado")

# Función para borrar un producto
def borrar_producto():
    nombre = input("Ingrese el nombre del producto a borrar: ")
    if nombre in productos:
        del productos[nombre]
        print("Producto eliminado con éxito")
    else:
        print("Producto no encontrado")

# Función para borrar todos los productos
def borrar_todos_los_productos():
    productos.clear()
    print("Todos los productos han sido eliminados")

while True:
        print("Menu Principal:")
        print("1. Opcion Menu de Clientes")
        print("2. Opcion Menu de Productos")
        print("3. Acerca de")
        print("4. Cerrar Programa")
        opciones = input ("Seleccione una opcion: ")
        if opciones == "1":
             while True:
                print("Menu de Clientes")
                print("1. Agregar Cliente")
                print("2. Modificar Cliente")
                print("3. Borrar Cliente")
                print("4. Borrar todos los Clientes")
                print("5. Volver al Menu Principal")
                Menudeclientes = input ("Seleccione una opcion: ")

                if Menudeclientes =="1":
                    agregar_cliente()
                elif Menudeclientes =="2":
                    modificar_cliente()
                elif Menudeclientes =="3":
                    borrar_cliente()
                elif Menudeclientes =="4":
                    borrar_todos_los_clientes()
                elif Menudeclientes =="5":
                    break
                else:
                    print("Opcion invalida, Seleccione una opcion valida.")
        if opciones == "2":
            while True:
                print("Menu de Productos")
                print("1. Agregar Productos")
                print("2. Modificar Porductos")
                print("3. Borrar Producto")
                print("4. Borrar todos los productos")
                print("5. Volver al menu principal")
                Menudeproductos= input ("Seleccione una opcion: ")

                if Menudeproductos =="1":
                    agregar_producto()
                elif Menudeproductos =="2":
                    modificar_producto()
                elif Menudeproductos =="3":
                    borrar_producto()
                elif Menudeproductos =="4":
                    borrar_todos_los_productos()
                elif Menudeproductos =="5":
                    break
                else:
                    print("Seleccione una opcion valida.")
        if opciones == "3":
            print("Eato es un programa para administrar el registro de los clientes del restaurante y la la toma de pedidos de este, registrando sus productos como orden. Hecho Juliana Buitrago")
        if opciones == "4": 
            break
        else:
           print("Opcion Invalida, seleccione una opcion valida.")
