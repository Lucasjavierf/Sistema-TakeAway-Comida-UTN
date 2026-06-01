"""
Solo muestra y controla menús.
Funciones relacionadas a los menús del sistema
Y desde aca llamás funciones de otros módulos.
"""
from roles.cliente import (
    realizar_pedido, ver_datos_cliente
)

from roles.restuarante import (
    preparar_pedido, entregar_pedido
)

from roles.administrador import (
    crear_usuario, borrar_usuario
)
from prints import (
    print_menu_admin, print_menu_cliente, print_menu_restaurante
)

def menu_cliente():
    """Muestra el menú del cliente."""
    seguir = True
    while seguir == True:
        print("Menú del Cliente:")
        print("1. Realizar Pedido")
        print("2. Ver Datos del Cliente")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            realizar_pedido()
        elif opcion == "2":
            ver_datos_cliente()
        elif opcion == "3":
            seguir = False
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
    pass


def menu_restaurante():
    """Muestra el menú del restaurante."""

    print_menu_restaurante()
    pass


def menu_admin():
    """Muestra el menú del administrador."""
    print_menu_admin()
    pass