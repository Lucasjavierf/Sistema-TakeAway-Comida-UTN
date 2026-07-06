import modulos.datos as datos
from modulos.datos import guardar_json, RUTA_PEDIDOS
from modulos.funciones import filtrar_catalogo, calcular_total_pedido, buscar_usuario, filtrar_por_rol
from modulos.validaciones import verificar_numero_entero, esperar_menu
from modulos.utilidades import generar_numero_pedido, generar_codigo_entrega, pausar

"""
Funciones correspondientes al rol cliente.
"""


def ver_datos_cliente(usuario):
    """Muestra los datos del cliente."""
    print("Datos del Cliente:")
    print(f"Usuario: {usuario['usuario']}")
    print(f"Nombre: {usuario['nombre']} {usuario['apellido']} ")
    print(f"Email: {usuario['email']}")
    print(f"Teléfono: {usuario['telefono']}")
    print(f"Domicilio: {usuario['domicilio']}")
    print(f"DNI: {usuario['dni']}")
    print(f"Edad: {usuario['edad']}")
    print(f"Cantidad pedidos: {usuario['cantidad_pedidos']}")
    pausar() 


def ver_menu_comidas(comidas): #Puede ir en prints
    """Muestra el menú de comidas disponibles."""
    print("Menú de Comidas:")
    for i in range(len(comidas)):
        print(f"{i+1}. {comidas[i]['nombre']}: ${comidas[i]['precio']}")



def ver_menu_bebidas(bebidas): #Esto tambien puede ir en prints
    """Muestra el menú de bebidas disponibles."""
    print("Menú de Bebidas:")
    print("0. Sin bebida")
    for i in range(len(bebidas)):
        print(f"{i+1}. {bebidas[i]['nombre']}: ${bebidas[i]['precio']}")


def seleccionar_comida(comidas):
    """Permite seleccionar una comida."""
    ver_menu_comidas(comidas)
    comida_elegida = None
    while comida_elegida is None:
        opcion = input("Elija el número de la comida que desea: ")
        if verificar_numero_entero(opcion) and int(opcion) > 0 and int(opcion) <= len(comidas):
            comida_elegida = comidas[int(opcion) - 1]
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
    return comida_elegida

def seleccionar_bebida(bebidas):
    """Permite seleccionar una bebida."""
    ver_menu_bebidas(bebidas)
    bebida_elegida = "sin_elegir"
    while bebida_elegida == "sin_elegir":
        opcion = input("Elija el número de la bebida que desea (0 para ninguna): ")
        if verificar_numero_entero(opcion):
            opcion = int(opcion)
            if opcion == 0:
                bebida_elegida = None
            elif opcion > 0 and opcion <= len(bebidas):
                bebida_elegida = bebidas[opcion - 1]
            else:
                print("Opción no válida. Por favor, intente nuevamente.")
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
    return bebida_elegida

def pedir_cantidad_unidades(mensaje:str, minimo:int, maximo:int) -> int:
    cantidad = None
    while cantidad is None:
        opcion = input(mensaje)
        if verificar_numero_entero(opcion) and int(opcion) >= minimo and int(opcion) <= maximo:
            cantidad = int(opcion)
        else:
            print(f"Cantidad no válida. Debe ser un número entre {minimo} y {maximo}. Por favor, intente nuevamente.")
    return cantidad

def generar_numero_unico(pedidos:list, tipo_de_numero:str) -> int:
    if tipo_de_numero == "pedido":
        numero = generar_numero_pedido()
    elif tipo_de_numero == "entrega":
        numero = generar_codigo_entrega()
    numeros_existentes = [pedido["numero"] for pedido in pedidos]
    while numero in numeros_existentes:
        if tipo_de_numero == "pedido":
            numero = generar_numero_pedido()
        elif tipo_de_numero == "entrega":
            numero = generar_codigo_entrega()
    return numero

def realizar_pedido(usuario:dict, catalogo:list, pedidos:list) -> dict:
    
    """Gestiona el flujo principal de un pedido."""
    print("Realizar Pedido:")
    print("\n  Restaurantes disponibles:")
    restaurantes_disponibles = filtrar_por_rol(datos.usuarios, "Restaurante")
    for rest in restaurantes_disponibles:
        print(f"    \u2022 {rest['usuario']} \u2014 {rest['nombre_local']}")
    print()
    while True:
        nombre_restaurante = input("Ingrese el nombre de usuario del restaurante: ")
        if len(nombre_restaurante) >= 3:
            break
        else:
            print("El nombre del restaurante debe tener al menos 3 caracteres. Por favor, intente nuevamente.")
    restaurante = buscar_usuario(datos.usuarios, nombre_restaurante)
    if restaurante is None or restaurante["rol"] != "Restaurante":
        print("El restaurante ingresado no existe o no es un restaurante válido. Por favor, intente nuevamente.")
        pausar()
        return None
    comidas_disponibles = filtrar_catalogo(catalogo, restaurante["usuario"], "comida")
    if len(comidas_disponibles) == 0:
        print("El restaurante seleccionado no tiene comidas disponibles. Por favor, intente nuevamente.")
        pausar()
        return None
    comida_dict = seleccionar_comida(comidas_disponibles)
    cantidad_comida = pedir_cantidad_unidades("Ingrese la cantidad de unidades de comida (1-10): ", 1, 10)
    bebidas_disponibles = filtrar_catalogo(catalogo, restaurante["usuario"], "bebida")
    bebidas_dict = None
    cantidad_bebida = 0
    if len(bebidas_disponibles) > 0:
        bebidas_dict = seleccionar_bebida(bebidas_disponibles)
        if bebidas_dict is not None:
            cantidad_bebida = pedir_cantidad_unidades("Ingrese la cantidad de unidades de bebida (1-10): ", 1, 10)
    total = calcular_total_pedido(comida_dict, cantidad_comida, bebidas_dict, cantidad_bebida)
    print("Resumen del Pedido:")
    print(f"Restaurante: {restaurante['usuario']}")
    print(f"Comida: {comida_dict['nombre']}")
    print(f"Cantidad: {cantidad_comida}")
    if bebidas_dict is not None:
        print(f"Bebida: {bebidas_dict['nombre']}")
        print(f"Cantidad: {cantidad_bebida}")
    print(f"Total: ${total}")
    confirmacion = input("¿Desea confirmar el pedido? (s/n): ")
    if confirmacion == "S" or confirmacion == "s":
        numero_pedido = generar_numero_unico(pedidos, "pedido")
        numero_entrega = generar_numero_unico(pedidos, "entrega")
        pedido = {
            "numero": numero_pedido,
            "codigo_entrega": numero_entrega,
            "cliente": usuario["usuario"],
            "restaurante": nombre_restaurante,
            "comida": comida_dict["nombre"],
            "cantidad_comida": cantidad_comida,
            "bebida": bebidas_dict["nombre"] if bebidas_dict else "ninguna",
            "cantidad_bebida": cantidad_bebida,
            "total": total,
            "estado": "pendiente",
            "fecha": "2025-06-01",
        }
        pedidos.append(pedido)
        guardar_json(RUTA_PEDIDOS, pedidos)
        print("Pedido realizado con éxito.")
    else:
        print("Pedido cancelado.")
    pausar()

def ver_pedidos_en_preparacion(usuario:dict, pedidos:list):
    pedidos_filtrados = []
    for pedido in pedidos:
        if pedido["cliente"] == usuario["usuario"] and pedido["estado"] == "en_preparacion":
            pedidos_filtrados.append(pedido)
    if len(pedidos_filtrados) == 0:
        print("No hay pedidos en preparación.")
    else:
        print("Pedidos en preparación:")
        for pedido in pedidos_filtrados:
            print(f"Codigo de entrega: {pedido['codigo_entrega']}")
            print(f"Número de pedido: {pedido['numero']}")
            print(f"Restaurante: {pedido['restaurante']}")
            print(f"Comida: {pedido['comida']} (Cantidad: {pedido['cantidad_comida']})")
            if pedido["bebida"] != "ninguna":
                print(f"Bebida: {pedido['bebida']} (Cantidad: {pedido['cantidad_bebida']})")
            print(f"Total: ${pedido['total']}")
            print("\n")
    pausar()