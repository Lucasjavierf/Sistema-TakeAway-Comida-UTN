"""
Funciones relacionadas al inicio de sesión.
"""
from modulos.validaciones import validar_usuario, validar_password
from modulos.funciones import buscar_usuario
import modulos.datos as datos


def iniciar_sesion() -> dict:
    """Solicita credenciales y devuelve el diccionario completo del usuario logueado.

    Returns:
        dict: Diccionario del usuario autenticado.
    """
    while True:
        nombre = input("Ingrese usuario: ")

        if validar_usuario(nombre):
            password = input("Ingrese contraseña: ")

            if validar_password(password):
                usuario = buscar_usuario(datos.usuarios, nombre)

                if usuario is not None and usuario["password"] == password:
                    print(f"\nBienvenido, {nombre}!")
                    return usuario

                print("Error: usuario o contraseña incorrectos.")