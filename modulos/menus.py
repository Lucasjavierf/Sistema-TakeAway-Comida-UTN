"""
Solo muestra y controla menús.
Funciones relacionadas a los menús del sistema
Y desde aca llamás funciones de otros módulos.
"""
from roles.cliente import (
    realizar_pedido, ver_datos_cliente
)
from roles.restaurante import *
from roles.administrador import *
from modulos.validaciones import *

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



            
def menu_restaurante():
    """Muestra y gestiona el menú del rol Restaurante."""
    while True:
        limpiar_pantalla()
        print("Menú restaurante")
        print("  1. Ver datos del restaurante")
        print("  2. Preparar pedido")
        print("  3. Entregar pedido")
        print("  0. Cerrar sesión")
 
        opcion = input("\n  Elegí una opción: ")
 
        if opcion == "1":
            ver_datos_restaurante()
        elif opcion == "2":
            preparar_pedido()
        elif opcion == "3":
            entregar_pedido()
        elif opcion == "0":
            print("\n Sesión cerrada. ¡Hasta luego!")
            break
        else:
            print("\n Opción inválida. Intentá de nuevo.")
            pausar()



def menu_administrador():
    """Muestra y gestiona el menú del rol Administrador."""
    while True:
        limpiar_pantalla()
        print("menú administrador")
        print("  1. Crear usuario")
        print("  2. Borrar usuario")
        print("  3. Ver información del sistema")
        print("  4. Salir")
 
        opcion = input("\n  Elegí una opción: ")
 
        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            borrar_usuario()
        elif opcion == "3":
            ver_info_sistema()
        elif opcion == "4":
            print("\n Sesión cerrada. ¡Hasta luego!")
            break
        else:
            print("\n Opción inválida. Intentá de nuevo.")
            pausar()

   