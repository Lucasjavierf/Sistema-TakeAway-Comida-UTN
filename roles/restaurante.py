"""
Funciones correspondientes al rol restaurante.
"""
import random
from modulos.utilidades import *
from modulos.datos import *
from modulos.validaciones import *
from modulos.funciones import *


def ver_datos_restaurante(usuario: dict):
    """Muestra los datos del restaurante logueado (sin la contraseña)."""
    print("\n  DATOS DEL RESTAURANTE")
    print(f"  Usuario         : {usuario['usuario']}")
    print(f"  Nombre del local: {usuario['nombre_local']}")
    print(f"  Tipo de cocina  : {usuario['tipo_cocina']}")
    print(f"  Domicilio       : {usuario['domicilio']}")
    print(f"  Teléfono        : {usuario['telefono']}")
    print(f"  Pedidos hoy     : {usuario['pedidos_hoy']}")
    print(f"  Empleados       : {usuario['empleados']}")
    print(f"  Facturación     : ${usuario['facturacion']}")

    pausar()



def preparar_pedido(usuario: dict, pedidos: list):
    """Permite al restaurante tomar un pedido pendiente y pasarlo a preparación."""

    pendientes = buscar_pedidos(pedidos, usuario["usuario"], "pendiente")

    if len(pendientes) == 0:
        print("\n  No hay pedidos pendientes en este momento.")
        pausar()
        return

    print("\n  PEDIDOS PENDIENTES")
    for pedido in pendientes:
        print(f"  N° {pedido['numero']} | Cliente: {pedido['cliente']} | "
              f"Comida: {pedido['comida']} | Total: ${pedido['total']}")

    numero_ingresado = input("\n  Ingresá el número de pedido a preparar: ")

    if not verificar_numero_entero(numero_ingresado):
        print("\n  Número inválido.")
        pausar()
        return

    numero_ingresado = int(numero_ingresado)

    pedido_elegido = None
    for pedido in pendientes:
        if pedido["numero"] == numero_ingresado:
            pedido_elegido = pedido
            break

    if pedido_elegido is None:
        print("\n  Error: ese número no corresponde a ninguno de tus pedidos pendientes.")
        pausar()
        return

    print("\n  DETALLE DEL PEDIDO")
    print(f"  Cliente : {pedido_elegido['cliente']}")
    print(f"  Comida  : {pedido_elegido['comida']} x{pedido_elegido['cantidad_comida']}")
    print(f"  Bebida  : {pedido_elegido['bebida']} x{pedido_elegido['cantidad_bebida']}")
    print(f"  Total   : ${pedido_elegido['total']}")

    confirmacion = ""
    while confirmacion != "s" and confirmacion != "S" and confirmacion != "n" and confirmacion != "N":
        confirmacion = input("\n  ¿Confirmás la preparación de este pedido? (s/n): ")
        if confirmacion != "s" and confirmacion != "S" and confirmacion != "n" and confirmacion != "N":
            print("  Respuesta inválida. Ingresá 's' o 'n'.")

    if confirmacion == "s" or confirmacion == "S":
        actualizar_estado(pedidos, numero_ingresado, "en_preparacion")

        codigo_entrega = random.randint(1000, 9999)
        pedido_elegido["codigo_entrega"] = codigo_entrega

        guardar_json(RUTA_PEDIDOS, pedidos)

        print(f"\n  Pedido N° {numero_ingresado} pasó a estado EN PREPARACIÓN.")
        pausar()
    else:
        print("\n  Operación cancelada.")
        pausar()



def entregar_pedido(usuario: dict, pedidos: list):
    """Permite al restaurante entregar un pedido que está en preparación."""

    en_preparacion = buscar_pedidos(pedidos, usuario["usuario"], "en_preparacion")

    if len(en_preparacion) == 0:
        print("\n  No hay pedidos en preparación en este momento.")
        pausar()
        return

    print("\n  PEDIDOS EN PREPARACIÓN")
    for pedido in en_preparacion:
        print(f"  N° {pedido['numero']} | Cliente: {pedido['cliente']} | "
              f"Comida: {pedido['comida']} | Total: ${pedido['total']}")

    numero_ingresado = input("\n  Ingresá el número de pedido a entregar: ")

    if not verificar_numero_entero(numero_ingresado):
        print("\n  Número inválido.")
        pausar()
        return

    numero_ingresado = int(numero_ingresado)

    pedido_elegido = None
    for pedido in en_preparacion:
        if pedido["numero"] == numero_ingresado:
            pedido_elegido = pedido
            break

    if pedido_elegido is None:
        print("\n  Error: ese número no corresponde a ninguno de tus pedidos en preparación.")
        pausar()
        return

    intentos = 0
    entregado = False

    while intentos < 3 and entregado == False:
        codigo_ingresado = input("\n  Ingresá el código de entrega: ")

        if verificar_numero_entero(codigo_ingresado):
            codigo_ingresado = int(codigo_ingresado)

            if codigo_ingresado == pedido_elegido["codigo_entrega"]:
                entregado = True
            else:
                intentos = intentos + 1
                intentos_restantes = 3 - intentos
                if intentos_restantes > 0:
                    print(f"\n  Código incorrecto. Te quedan {intentos_restantes} intento(s).")
        else:
            intentos = intentos + 1
            intentos_restantes = 3 - intentos
            if intentos_restantes > 0:
                print(f"\n  Código inválido. Te quedan {intentos_restantes} intento(s).")

    if entregado == True:
        actualizar_estado(pedidos, numero_ingresado, "entregado")
        guardar_json(RUTA_PEDIDOS, pedidos)

        print("\n  Pedido entregado con éxito.")
        pausar()
    else:
        print("\n  Superaste el máximo de intentos. Operación cancelada.")
        pausar()

def ver_facturacion(usuario: dict, pedidos: list):
    """Muestra la facturación de todos los pedidos del restaurante en formato tabular."""

    matriz = obtener_pedidos_a_matriz(pedidos, usuario["usuario"])

    if len(matriz) == 0:
        print("\n  Este restaurante todavía no tiene pedidos registrados.")
        pausar()
        return

    estados_texto = {
        1: "pendiente",
        2: "en_preparacion",
        3: "entregado"
    }

    print("\n  FACTURACIÓN")
    print("  +---------------+------------+-----------------+")
    print("  | Número        | Total      | Estado          |")
    print("  +---------------+------------+-----------------+")

    total_general = 0
    for fila in matriz:
        numero = str(fila[0])
        total_fila = fila[1]
        total_texto = "$" + str(total_fila)
        estado_texto = estados_texto[fila[2]]

        espacios_numero = " " * (13 - len(numero))
        espacios_total = " " * (10 - len(total_texto))
        espacios_estado = " " * (15 - len(estado_texto))

        print("  | " + numero + espacios_numero + " | " + total_texto + espacios_total + " | " + estado_texto + espacios_estado + " |")

        total_general = total_general + total_fila

    print("  +---------------+------------+-----------------+")

    total_general_texto = "$" + str(total_general)
    espacios_total_general = " " * (29 - len(total_general_texto))
    print("  | TOTAL" + espacios_total_general + total_general_texto + " |")
    print("  +---------------+------------+-----------------+")

    pausar()