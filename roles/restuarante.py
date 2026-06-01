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
    pass


def ver_pedidos():
    """Muestra los pedidos recibidos."""
    

    pass


def preparar_pedido():
    """Simula la preparación de un pedido."""
    numero_pedido = generar_numero_pedido()
    print("  Pedido confirmado y en preparación.")
    print(f"  Número de pedido : {numero_pedido}")
    print("  Estado           : EN PREPARACIÓN ")
    pausar()

    pass


def generar_codigo_entrega():
    """Genera un código de entrega aleatorio."""
    inicio = 1000
   
    fin = 9999

    return random.randint(inicio, fin)
    pass


def entregar_pedido():
    """Simula la entrega del pedido."""
    print("  Entregar pedido")
    numero_pedido = input("Ingresar numero de pedido")
    min = 1000000000000000
    max =9999999999999
    numero_pedido = validar_numero_rango(numero_pedido,min,max)
    codigo_entrega = input("  Ingresar codigo de entrega ")
    codigo_entrega = validar_codigo_entrega(codigo_entrega)
    if codigo_entrega == 1234:
        print(f" Pedido numero: {numero_pedido}")
        print("  Pedido entregado con éxito")
    else
        print("  No se puede entregar el pedido " \
        "debido a que el código que le dió el cliente es incorrecto")
    
    pausar()


    pass

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