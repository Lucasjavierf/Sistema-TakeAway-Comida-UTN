"""
Funciones reutilizables de validación.
Acá centralizamos TODAS las validaciones.

Este archivo va a ahorrar muchísimo código repetido.
"""

def validar_usuario(usuario):
    """Valida un nombre de usuario."""
    if len(usuario) < 3 or len(usuario) > 15:
        print("Error: El nombre de usuario debe tener entre 3 y 15 caracteres.")
        return False

    return True


def validar_password(password):
    """Valida una contraseña."""
    if len(password) < 6 or len(password) > 15:
        print("Error: La contraseña debe tener entre 6 y 15 caracteres.")
        return False

    return True


def validar_domicilio(domicilio):
    """Valida un domicilio."""
    if len(domicilio) < 7   or len(domicilio) > 30:
        print("Error: El domicilio debe tener entre 7 y 30 caracteres.")
        return False

    return True


def validar_numero_rango(numero, minimo, maximo):
    """Valida un rango numérico."""
    if numero < minimo or numero > maximo:
        print(f"Error: El número debe estar entre {minimo} y {maximo}.")
        return False
    return True


def validar_codigo_entrega(codigo):
    """Valida un código de entrega."""
    if len(codigo) == 4 and codigo == "1234":
        return True

    return False