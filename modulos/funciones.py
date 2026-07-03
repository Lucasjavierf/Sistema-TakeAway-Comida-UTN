"""
Funciones puras del sistema.

Todas las funciones de este módulo son puras:
reciben datos como parámetros, devuelven un resultado
y no modifican ninguna variable fuera de su scope.
"""


def filtrar_catalogo(catalogo: list, restaurante: str, categoria: str) -> list:
    """Devuelve los ítems del catálogo de un restaurante filtrados por categoría.

    Args:
        catalogo (list): Lista completa del catálogo.
        restaurante (str): Nombre de usuario del restaurante.
        categoria (str): "comida" o "bebida".

    Returns:
        list: Lista de ítems que coinciden con el restaurante y la categoría.
    """
    resultado = []
    for item in catalogo:
        if item["restaurante"] == restaurante and item["categoria"] == categoria:
            resultado.append(item)
    return resultado


def calcular_total_pedido(comida: dict, cant_c: int, bebida: dict, cant_b: int) -> float:
    """Calcula el precio total de un pedido.

    Args:
        comida (dict): Ítem de comida del catálogo.
        cant_c (int): Cantidad de comida.
        bebida (dict): Ítem de bebida del catálogo, o None si no hay bebida.
        cant_b (int): Cantidad de bebida.

    Returns:
        float: Precio total del pedido.
    """
    total = comida["precio"] * cant_c
    if bebida is not None and cant_b > 0:
        total = total + (bebida["precio"] * cant_b)
    return total


def buscar_pedidos(pedidos: list, restaurante: str, estado: str) -> list:
    """Devuelve los pedidos de un restaurante filtrados por estado.

    Args:
        pedidos (list): Lista completa de pedidos.
        restaurante (str): Nombre de usuario del restaurante.
        estado (str): "pendiente", "en_preparacion" o "entregado".

    Returns:
        list: Lista de pedidos que coinciden con el restaurante y el estado.
    """
    resultado = []
    for pedido in pedidos:
        if pedido["restaurante"] == restaurante and pedido["estado"] == estado:
            resultado.append(pedido)
    return resultado


def actualizar_estado(pedidos: list, numero: int, nuevo_estado: str):
    """Modifica el estado de un pedido en la lista.

    Args:
        pedidos (list): Lista completa de pedidos.
        numero (int): Número del pedido a actualizar.
        nuevo_estado (str): Nuevo estado a asignar.

    Returns:
        dict | None: El pedido modificado, o None si no se encontró.
    """
    for pedido in pedidos:
        if pedido["numero"] == numero:
            pedido["estado"] = nuevo_estado
            return pedido
    return None


def obtener_pedidos_a_matriz(pedidos: list, restaurante: str) -> list:
    """Construye una matriz con los pedidos de un restaurante.

    Cada fila contiene: [numero, total, estado_como_int]
    donde estado: 1=pendiente, 2=en_preparacion, 3=entregado.

    Args:
        pedidos (list): Lista completa de pedidos.
        restaurante (str): Nombre de usuario del restaurante.

    Returns:
        list: Matriz (lista de listas) con los datos de facturación.
    """
    estados = {
        "pendiente":      1,
        "en_preparacion": 2,
        "entregado":      3
    }
    matriz = []
    for pedido in pedidos:
        if pedido["restaurante"] == restaurante:
            fila = [pedido["numero"], pedido["total"], estados[pedido["estado"]]]
            matriz.append(fila)
    return matriz


def filtrar_por_rol(usuarios: list, rol: str) -> list:
    """Devuelve la lista de usuarios que tienen el rol indicado.

    Args:
        usuarios (list): Lista completa de usuarios.
        rol (str): "Cliente", "Restaurante" o "Administrador".

    Returns:
        list: Lista de usuarios con ese rol.
    """
    resultado = []
    for usuario in usuarios:
        if usuario["rol"] == rol:
            resultado.append(usuario)
    return resultado


def buscar_usuario(usuarios: list, nombre: str):
    """Busca un usuario por nombre de usuario.

    Args:
        usuarios (list): Lista completa de usuarios.
        nombre (str): Nombre de usuario a buscar.

    Returns:
        dict | None: El diccionario del usuario encontrado, o None si no existe.
    """
    for usuario in usuarios:
        if usuario["usuario"] == nombre:
            return usuario
    return None
