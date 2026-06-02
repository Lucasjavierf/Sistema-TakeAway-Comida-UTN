"""
Todo lo visual:
mensaje inicial, títulos, separadores, mensajes decorativos, menús impresos etc... 
"""



def mensaje_inicial():
    """Imprime el texto de presentacion solicitado en la consigna"""

    print('================= Bienvenido al sistema de delivery UTN Eats =================')
    print('Pide desde la comodidad de tu casa!')        
    print('Este sistema permite realizar pedidos de comida entre clientes y restaurantes.')    


#Menus Roles 

def print_menu_cliente():
    print("1. Ver datos")
    print("2. Realizar pedido")
    print("3. Salir")
    
def print_menu_restaurante():
    print("1. Ver datos")
    print("2. Preparar pedido")
    print("3. Entregar pedido")
    print("4. Salir")

def print_menu_admin():
    print("1. Crear usuario")
    print("2. Borrar usuario")
    print("3. Ver información")
    print("4. Salir")

def lista_restaurantes():
    print("RestoUTN")
    print("MinutasAV")