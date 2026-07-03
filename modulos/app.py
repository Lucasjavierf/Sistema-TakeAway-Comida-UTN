"""Módulo principal de ejecución de la aplicación.

Se encarga de controlar el flujo general del sistema:
- mostrar la presentación
- iniciar sesión
- identificar el rol del usuario
- dirigir al menú correspondiente
"""

from modulos.prints import mensaje_inicial
from modulos.login import iniciar_sesion
from modulos.menus import (
    menu_cliente,
    menu_restaurante,
    menu_administrador
)


def iniciar_app():
    """Inicia el flujo principal del sistema."""

    mensaje_inicial()

    while True:
        usuario = iniciar_sesion()

        match usuario["rol"]:

            case "Cliente":
                menu_cliente(usuario)

            case "Restaurante":
                menu_restaurante(usuario)

            case "Administrador":
                menu_administrador()

            case _:
                print("Error: rol no reconocido.")

        print("\n¿Qué querés hacer?")
        print("  1. Iniciar sesión con otra cuenta")
        print("  2. Salir del sistema")
        opcion = input("\n  Elegí una opción: ")

        if opcion == "2":
            print("\n¡Hasta luego! Gracias por usar UTN Eats.")
            break
