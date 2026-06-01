"""
Funciones relacionadas al inicio de sesión.

Ahí:
pedís usuario, pedís contraseña, validás longitud, verificás usuarios, devolvés el rol, etc...
"""
from modulos.validaciones import *
from modulos.datos import usuarios
def iniciar_sesion():
    while True:
        usuario = input("Ingrese usuario: ")
        
        if validar_usuario(usuario):
            password = input("Ingrese contraseña: ")
            if validar_password(password):
                for user in usuarios:
                    if user["usuario"] == usuario and user["password"] == password:
                        print(f"Bienvenido {usuario}!")
                        return user["rol"]
                
                print("Error: Usuario o contraseña incorrectos.")