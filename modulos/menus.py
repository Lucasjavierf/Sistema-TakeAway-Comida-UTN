"""
Solo muestra y controla menús.
Funciones relacionadas a los menús del sistema
Y desde aca llamás funciones de otros módulos.
"""
from roles.cliente import (
    realizar_pedido,
    ver_datos_cliente
)

from roles.restuarante import (
    preparar_pedido,
    entregar_pedido
)

from roles.administrador import (
    crear_usuario,
    borrar_usuario
)

def menu_cliente():
    """Muestra el menú del cliente."""

    pass


def menu_restaurante():
    """Muestra el menú del restaurante."""

    pass


def menu_admin():
    """Muestra el menú del administrador."""

    pass