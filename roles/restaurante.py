"""
Funciones correspondientes al rol restaurante.
"""
from modulos.utilidades import *
from modulos.datos import *
from modulos.validaciones import *


def ver_datos_restaurante():
    """Muestra los datos del restaurante."""

    print(f"  Nombre          : {datos_restaurante[0]}")
    print(f"  Dirección       : {datos_restaurante[1]}")
    print(f"  Tipo de cocina  : {datos_restaurante[2]}")
    print(f"  Teléfono        : {datos_restaurante[3]}")
    print(f"  Pedidos hoy     : {datos_restaurante[4]}")
    print(f"  Empleados       : {datos_restaurante[5]}")
    print(f"  Facturación mes : ${datos_restaurante[6]}")

    pausar()



def preparar_pedido():
    """Simula la preparación de un pedido."""
    numero_pedido = generar_numero_pedido()
    codigo_entrega = 1234
    print("Pedido confirmado y en preparación.")
    print(f"Número de pedido : {numero_pedido}")
    print(f'Codigo de entrega : {codigo_entrega}')
    print("  Estado           : EN PREPARACIÓN ")
    pausar()




def entregar_pedido():
    """Simula la entrega del pedido."""
    print("  Entregar pedido")
    codigo_entrega = int(input("  Ingresar codigo de entrega "))
    if codigo_entrega == 1234:
        print("  Pedido entregado con éxito")
    else:
        print("  No se puede entregar el pedido " \
        "debido a que el código que le dió el cliente es incorrecto")
    
    pausar()




