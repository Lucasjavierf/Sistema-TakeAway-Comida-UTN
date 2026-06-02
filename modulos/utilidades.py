'''
Funciones auxiliares reutilizables.
Ejemplos:
'''
import os
import random

def limpiar_pantalla():
    """Limpia la consola."""
    os.system("cls" if os.name == "nt" else "clear")

    pass


def pausar(mensaje = "Presiona enter para continuar..."):
    """Pausa la ejecución."""

    input(f"\n{mensaje}")

    pass


def generar_numero_pedido():
    """Genera un número de pedido aleatorio."""
    inicio = 1000000000000
    fin = 9999999999999

    return random.randint(inicio, fin)

    pass