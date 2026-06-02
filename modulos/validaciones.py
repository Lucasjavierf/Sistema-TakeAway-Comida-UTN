import os
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



def verificar_numero_entero(numero:str) -> bool:
    """Verifica si el numero ingresado es entero comparandolo con los valores ascii validos.

    Args:
        numero (str): Numero ingresado por el usuario

    Returns:
        bool: True si el numero es entero, False en caso contrario.
    """
    if len(numero) > 0:
        bandera_valido = True
        for i in range(len(numero)):
            caracter = numero[i]
            ascii_caracter = ord(caracter)
            if ascii_caracter < 48 or ascii_caracter > 57 and (i != 0 or caracter != '-'):
                bandera_valido = False
                break
    else:
        bandera_valido = False

    return bandera_valido


def esperar_menu() -> None:
    """Borra lo que hay en la terminal y pone un input como pausa.
    """
    input("Ingresa enter para continuar...")
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')