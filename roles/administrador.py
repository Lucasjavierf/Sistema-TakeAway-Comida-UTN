"""
Funciones correspondientes al rol administrador.
"""
from modulos.utilidades import *

integrantes = [
    "Persona 1 — Coordinación e integración",
    "Persona 2 — Login, validaciones y datos",
    "Persona 3 — Cliente y menús",
    "Persona 4 — Restaurante, administrador y utilidades",
]


descripcion_sistema = """
  ¿Para qué sirve?
    UTN Eats es un sistema de pedidos de comida por consola que permite
    a clientes hacer pedidos, a restaurantes gestionarlos y a administradores
    mantener los usuarios del sistema.
 
  ¿Qué problema resuelve?
    Centraliza la gestión de pedidos take away sin necesidad de delivery,
    simplificando la comunicación entre cliente y restaurante.
 
  ¿Qué tipos de usuario tenemos?
    • Cliente      → realiza pedidos y consulta sus datos.
    • Restaurante  → prepara y entrega pedidos.
    • Administrador → gestiona usuarios del sistema.
"""
 
funcionalidades_extras = """
  Funcionalidades extras:
    Cliente:
      • Consultar historial de pedidos
      • Ver promociones del día
      • Cancelar un pedido pendiente
 
    Administrador:
      • Ver listado completo de usuarios
      • Generar reporte de actividad del sistema
 
    Restaurante:
      • Ver pedidos pendientes del día
      • Actualizar el menú disponible
"""


def validar_longitud(texto, minimo):
    """Devuelve True si el texto tiene al menos 'minimo' caracteres."""
    if len(texto) >= minimo:
        return True
    return False

def pedir_nombre_usuario():
    """Solicita un nombre de usuario válido (mínimo 3 caracteres)."""
    while True:
        nombre = input("\n  Nombre de usuario (mín. 3 caracteres): ")
        if validar_longitud(nombre, 3):
            return nombre
        print(" El nombre debe tener al menos 3 caracteres.")

def pedir_contrasena():
    """Solicita una contraseña válida (mínimo 6 caracteres)."""
    while True:
        contrasena = input("  Contraseña (mín. 6 caracteres): ")
        if validar_longitud(contrasena, 6):
            return contrasena
        print("  La contraseña debe tener al menos 6 caracteres.")

def pedir_rol():
    """Solicita que se elija un rol: cliente o restaurante."""
    while True:
        rol = input("  Rol (cliente / restaurante): ")
        if rol in ("cliente", "restaurante"):
            return rol
        print(" Rol inválido. Escribí 'cliente' o 'restaurante'.")

def pedir_datos_restaurante():
    """Solicita los datos básicos de un nuevo restaurante."""
    print("\n  Completá los datos del restaurante:")
    nombre      = input("    Nombre del local   : ")
    tipo_cocina = input("    Tipo de cocina     : ")
    telefono    = input("    Teléfono           : ")
    domicilio   = pedir_domicilio()
    print(f"\n  Datos registrados para el restaurante '{nombre}'.")

def pedir_datos_cliente():
    """Solicita los datos básicos de un nuevo cliente."""
    print("\n  Completá los datos del cliente:")
    nombre      = input("    Nombre completo    : ")
    apellido    = input("    Apellido           : ")
    email       = input("    Email              : ")
    telefono    = input("    Teléfono           : ")
    domicilio   = pedir_domicilio()
    print(f"\n  Datos registrados para el cliente '{nombre} {apellido}'.")

def pedir_domicilio():
    """Solicita un domicilio válido (mínimo 7 caracteres)."""
    while True:
        domicilio = input("    Domicilio (mín. 7 caracteres): ")
        if validar_longitud(domicilio, 7):
            return domicilio
        print(" El domicilio debe tener al menos 7 caracteres.")

def crear_usuario():
    """Simula la creación de un usuario."""
    print("Crear usuario")
    nombre = pedir_nombre_usuario()
    contraseña = pedir_contrasena()
    rol = pedir_rol()

    print(f"\n Datos del nuevo usuario")
    print(f"   Nombre  : {nombre}")
    print(f"   Rol  :  {rol}")

    if rol == "cliente":
        pedir_datos_cliente()
    else:
        pedir_datos_restaurante()
    
    print("\n Usuario creado exitosamente.")
    pausar()
 


    pass


def borrar_usuario():
    """Simula el borrado de un usuario."""
    print("borrar usuario")
 
    nombre = pedir_nombre_usuario()
    print(f"\n Usuario '{nombre}' eliminado del sistema exitosamente.")
    pausar()
    pass


def modificar_usuario():
    """Simula la modificación de un usuario."""


    pass


def ver_usuarios():
    """Muestra los usuarios registrados."""

    pass


def ver_info_sistema():
    """Muestra información general del sistema."""
    print("Información del sistema")
 
    print("\n  Integrantes del grupo:")
    print(f"     • {integrantes[0]}")
    print(f"     • {integrantes[1]}")
    print(f"     • {integrantes[2]}")
    print(f"     • {integrantes[3]}")

    print(descripcion_sistema)
    print(funcionalidades_extras)
    pausar()

def menu_administrador():
    """Muestra y gestiona el menú del rol Administrador."""
    while True:
        limpiar_pantalla()
        print("menú administrador")
        print("  1. Crear usuario")
        print("  2. Borrar usuario")
        print("  3. Ver información del sistema")
        print("  0. Cerrar sesión")
 
        opcion = input("\n  Elegí una opción: ")
 
        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            borrar_usuario()
        elif opcion == "3":
            ver_info_sistema()
        elif opcion == "0":
            print("\n Sesión cerrada. ¡Hasta luego!")
            break
        else:
            print("\n Opción inválida. Intentá de nuevo.")
            pausar()
    pass