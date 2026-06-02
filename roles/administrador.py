"""
Funciones correspondientes al rol administrador.
"""
from modulos.utilidades import *
import modulos.datos as datos

integrantes = [
    "Fernandez Lucas Javier— Coordinación e integración",
    "Ferrari Renzo Damián — Login, validaciones y datos",
    "Kraus Matias — Cliente y menús",
    "Araujo Juan Ignacio — Restaurante, administrador y utilidades",
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
    return len(texto) >= minimo
 
 
def pedir_nombre_usuario():
    """Solicita un nombre de usuario válido (mínimo 3 caracteres)."""
    while True:
        nombre = input("\n  Nombre de usuario (mín. 3 caracteres): ")
        if validar_longitud(nombre, 3):
            return nombre
        print("  El nombre debe tener al menos 3 caracteres.")
 
 
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
        print("  Rol inválido. Escribí 'cliente' o 'restaurante'.")
 
 
def pedir_domicilio():
    """Solicita un domicilio válido (mínimo 7 caracteres)."""
    while True:
        domicilio = input("    Domicilio (mín. 7 caracteres): ")
        if validar_longitud(domicilio, 7):
            return domicilio
        print("  El domicilio debe tener al menos 7 caracteres.")
 
 
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
    nombre   = input("    Nombre completo    : ")
    apellido = input("    Apellido           : ")
    email    = input("    Email              : ")
    telefono = input("    Teléfono           : ")
    domicilio = pedir_domicilio()
    print(f"\n  Datos registrados para el cliente '{nombre} {apellido}'.")
 
 
def usuario_existe(nombre):
    """Devuelve True si ya existe un usuario con ese nombre."""
    for user in datos.usuarios:
        if user["usuario"] == nombre:
            return True
    return False
 
 
def crear_usuario():
    """Crea un nuevo usuario y lo agrega a la lista de usuarios."""
    print("\nCrear usuario")
 
    while True:
        nombre = pedir_nombre_usuario()
        if usuario_existe(nombre):
            print(f"  Error: el usuario '{nombre}' ya existe. Elegí otro nombre.")
        else:
            break
 
    contrasena = pedir_contrasena()
    rol = pedir_rol()
 
    nuevo_usuario = {
        "usuario": nombre,
        "password": contrasena,
        "rol": rol
    }
    datos.usuarios.append(nuevo_usuario)
 
    print(f"\n  Datos del nuevo usuario:")
    print(f"    Nombre : {nombre}")
    print(f"    Rol    : {rol}")
 
    if rol == "cliente":
        pedir_datos_cliente()
    else:
        pedir_datos_restaurante()
 
    print(f"\n  Usuario '{nombre}' creado exitosamente.")
    pausar()
 
 
def borrar_usuario():
    """Borra un usuario existente de la lista."""
    print("\nBorrar usuario")
 
    nombre = pedir_nombre_usuario()
 
    for i in range(len(datos.usuarios)):
        if datos.usuarios[i]["usuario"] == nombre:
            if datos.usuarios[i]["rol"] == "admin":
                print("  Error: no se puede eliminar una cuenta de administrador.")
                pausar()
                return
            datos.usuarios.pop(i)
            print(f"\n  Usuario '{nombre}' eliminado exitosamente.")
            pausar()
            return
 
    print(f"\n  Error: no existe ningún usuario con el nombre '{nombre}'.")
    pausar()
 
 
def ver_info_sistema():
    """Muestra información general del sistema."""
    print("\nInformación del sistema")
 
    print("\n  Integrantes del grupo:")
    for integrante in integrantes:
        print(f"     • {integrante}")
 
    print(descripcion_sistema)
    print(funcionalidades_extras)
    pausar()