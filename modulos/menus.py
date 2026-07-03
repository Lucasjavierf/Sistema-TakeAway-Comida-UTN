"""
Solo muestra y controla menús.
Recibe el usuario logueado y lo pasa a las funciones de cada rol.
"""
from roles.cliente import (
    realizar_pedido, ver_datos_cliente, ver_pedidos_en_preparacion
)
from roles.restaurante import (
    ver_datos_restaurante, preparar_pedido, entregar_pedido, ver_facturacion
)
from roles.administrador import (
    crear_usuario, borrar_usuario, ver_info_sistema
)
from modulos.utilidades import limpiar_pantalla, pausar
from modulos.validaciones import esperar_menu
import modulos.datos as datos


def menu_cliente(usuario: dict):
    """Muestra el menú del cliente."""
    while True:
        limpiar_pantalla()
        print(f"  USUARIO  : {usuario['usuario']}")
        print(f"  TIPO     : {usuario['rol']}")
        print()
        print("  1. Ver mis datos")
        print("  2. Realizar pedido")
        print("  3. Ver mis pedidos en preparación")
        print("  0. Cerrar sesión")

        opcion = input("\n  Elegí una opción: ")

        if opcion == "1":
            ver_datos_cliente(usuario)
        elif opcion == "2":
            realizar_pedido(usuario, datos.catalogo, datos.pedidos)
        elif opcion == "3":
            ver_pedidos_en_preparacion(usuario, datos.pedidos)
        elif opcion == "0":
            print("\n  Sesión cerrada. ¡Hasta luego!")
            break
        else:
            print("\n  Opción inválida. Intentá de nuevo.")
            pausar()


def menu_restaurante(usuario: dict):
    """Muestra el menú del restaurante."""
    while True:
        limpiar_pantalla()
        print(f"  USUARIO  : {usuario['usuario']}")
        print(f"  TIPO     : {usuario['rol']}")
        print()
        print("  1. Ver mis datos")
        print("  2. Preparar pedido")
        print("  3. Entregar pedido")
        print("  4. Ver facturación")
        print("  0. Cerrar sesión")

        opcion = input("\n  Elegí una opción: ")

        if opcion == "1":
            ver_datos_restaurante(usuario)
        elif opcion == "2":
            preparar_pedido(usuario, datos.pedidos)
        elif opcion == "3":
            entregar_pedido(usuario, datos.pedidos)
        elif opcion == "4":
            ver_facturacion(usuario, datos.pedidos)
        elif opcion == "0":
            print("\n  Sesión cerrada. ¡Hasta luego!")
            break
        else:
            print("\n  Opción inválida. Intentá de nuevo.")
            pausar()


def menu_administrador():
    """Muestra el menú del administrador."""
    while True:
        limpiar_pantalla()
        print("  TIPO: Administrador")
        print()
        print("  1. Crear usuario")
        print("  2. Borrar usuario")
        print("  3. Ver información del sistema")
        print("  0. Cerrar sesión")

        opcion = input("\n  Elegí una opción: ")

        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            borrar_usuario()
        elif opcion == "3":
            ver_info_sistema()
        elif opcion == "0":
            print("\n  Sesión cerrada. ¡Hasta luego!")
            break
        else:
            print("\n  Opción inválida. Intentá de nuevo.")
            pausar()
