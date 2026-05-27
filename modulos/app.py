from modulos.prints import mensaje_inicial
from modulos.login import iniciar_sesion
from modulos.menus import (
    menu_cliente,
    menu_restaurante,
    menu_admin
)

""" Módulo principal de ejecución de la aplicación.

Se encarga de controlar el flujo general del sistema:
- mostrar la presentación
- iniciar sesión
- identificar el rol del usuario
- dirigir al menú correspondiente
"""

def iniciar_app():

    mensaje_inicial()

    rol = iniciar_sesion()

    match rol:

        case "cliente":
            menu_cliente()

        case "restaurante":
            menu_restaurante()

        case "admin":
            menu_admin()

        case _:
            print("Error: rol no reconocido")