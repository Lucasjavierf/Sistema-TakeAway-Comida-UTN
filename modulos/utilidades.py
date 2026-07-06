'''
Funciones auxiliares reutilizables.
Ejemplos:
'''
import os
import random

def limpiar_pantalla():
    """Limpia la consola."""
    os.system("cls" if os.name == "nt" else "clear")



def pausar(mensaje = "Presiona enter para continuar..."):
    """Pausa la ejecución."""

    input(f"\n{mensaje}")


def generar_numero_pedido():
    """Genera un número de pedido aleatorio de 13 cifras."""
    inicio = 1000000000000
    fin = 9999999999999

    return random.randint(inicio, fin)


def generar_codigo_entrega():
    """Genera un código de entrega aleatorio de 4 dígitos."""
    return random.randint(1000, 9999)
