from modulos.datos import *


"""
Funciones correspondientes al rol cliente.
"""


def ver_datos_cliente():
    """Muestra los datos del cliente."""
    print("Datos del Cliente:")
    print(f"Domicilio: {Domicilio_cliente}")
    print(Datos_string_cliente[0])
    print(Datos_string_cliente[1])
    print(Datos_string_cliente[2])
    print(Datos_string_cliente[3])
    print(f"Cantidad de pedidos hechos: {Datos_int_cliente[0]}")
    print(f"Gasto total: ${Datos_int_cliente[1]}")
    print(f"Descuento total obtenido: ${Datos_int_cliente[2]}")

def ver_menu_comidas():
    """Muestra el menú de comidas disponibles."""
    print("Menú de Comidas:")
    for i in range(len(Menu_comidas)):
        print(f"{i+1}. {Menu_comidas[i]}: ${precio_comidas[i]}")



def ver_menu_bebidas():
    """Muestra el menú de bebidas disponibles."""
    print("Menú de Bebidas:")
    print("0. Sin bebida")
    for i in range(len(Menu_bebidas)):
        print(f"{i+1}. {Menu_bebidas[i]}: ${precio_bebidas[i]}")



def seleccionar_comida():
    """Permite seleccionar una comida."""
    ver_menu_comidas()
    comida_seleccionada = None
    while comida_seleccionada == None:
        opcion = int(input("Elija el número de la comida que desea: "))    
        if opcion > 0 and opcion <= len(Menu_comidas):
            comida_seleccionada = Menu_comidas[opcion - 1]
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
    return comida_seleccionada


def seleccionar_bebida():
    """Permite seleccionar una bebida."""
    ver_menu_bebidas()
    bebida_seleccionada = None
    while bebida_seleccionada == None:
        opcion = int(input("Elija el número de la bebida que desea: ")) 
        if opcion == 0:
            bebida_seleccionada = "Sin bebida"
        elif opcion > 0 and opcion <= len(Menu_bebidas):
                bebida_seleccionada = Menu_bebidas[opcion - 1]
        else:
                print("Opción no válida. Por favor, intente nuevamente.")
    return bebida_seleccionada



def realizar_pedido():
    
    """Gestiona el flujo principal de un pedido."""
    print("Realizar Pedido:")
    while True:
        restaurante = input("Ingrese el nombre del restaurante al que desea pedir: ")
        if len(restaurante) >= 3:
            break
        else:
            print("El nombre del restaurante debe tener al menos 3 caracteres. Por favor, intente nuevamente.")
        
    datos_comida = seleccionar_comida()
    while True:
        unidades_comida_pedidas = int(input("Ingrese la cantidad de unidades que desea pedir: "))
        if unidades_comida_pedidas > 0 and unidades_comida_pedidas <= 10:
            break
        else:
            print("La cantidad de unidades debe ser un número entre 1 y 10. Por favor, intente nuevamente.")
    datos_bebida = seleccionar_bebida()
    if datos_bebida != "Sin bebida":
        while True:
            unidades_bebida_pedidas = int(input("Ingrese la cantidad de unidades que desea pedir: "))   
            if unidades_bebida_pedidas >= 0 and unidades_bebida_pedidas <= 10:
                break
            else:
                print("La cantidad de unidades debe ser un número entre 0 y 10. Por favor, intente nuevamente.")
    else:
        unidades_bebida_pedidas = 0
    total_pedido = calcular_total(datos_comida, unidades_comida_pedidas, datos_bebida, unidades_bebida_pedidas)
    datos_finales_pedido = [restaurante, datos_comida, unidades_comida_pedidas, datos_bebida, unidades_bebida_pedidas, total_pedido]
    confirmar_pedido(datos_finales_pedido)
    return datos_finales_pedido

    



def calcular_total(datos_comida, unidades_comida_pedidas, datos_bebida, unidades_bebida_pedidas):
    """Calcula el total del pedido."""
    precio_comida = 0
    for i in range(len(Menu_comidas)):
        if datos_comida == Menu_comidas[i]:
            precio_comida = precio_comidas[i]
            break
    precio_bebida = 0
    for i in range(len(Menu_bebidas)):
        if datos_bebida == Menu_bebidas[i]:
            precio_bebida = precio_bebidas[i]
            break
    total = (precio_comida * unidades_comida_pedidas) + (precio_bebida * unidades_bebida_pedidas)
    return total


def confirmar_pedido(datos_finales_pedido):
    """Confirma el pedido realizado."""
    print("Pedido realizado con éxito.")
    print("RESUMEN DEL PEDIDO:")
    print(f"Restaurante: {datos_finales_pedido[0]}")
    print(f"Comida: {datos_finales_pedido[1]}")
    print(f"Cantidad: {datos_finales_pedido[2]}")
    print(f"Bebida: {datos_finales_pedido[3]}")
    print(f"Cantidad: {datos_finales_pedido[4]}")
    print(f"Total: ${datos_finales_pedido[5]}")