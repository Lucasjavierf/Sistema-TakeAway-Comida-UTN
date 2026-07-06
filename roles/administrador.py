"""
Funciones correspondientes al rol Administrador.
"""
import modulos.datos as datos
from modulos.datos import guardar_json, RUTA_USUARIOS, RUTA_ELIMINADOS
from modulos.funciones import filtrar_por_rol, buscar_usuario
from modulos.utilidades import pausar, limpiar_pantalla
from modulos.validaciones import esperar_menu, validar_domicilio, verificar_numero_entero


integrantes = [
    "Fernandez Lucas Javier — Coordinación e integración",
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
    • Cliente       → realiza pedidos y consulta sus datos.
    • Restaurante   → prepara y entrega pedidos.
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


# ---------- Helpers internos (no forman parte de las firmas pedidas) ----------

def _pedir_nombre_usuario_nuevo() -> str:
    """Pide un nombre de usuario nuevo, validando longitud y que no exista."""
    while True:
        nombre = input("\n  Nombre de usuario (mín. 3 caracteres): ")
        if len(nombre) < 3:
            print("  Error: el nombre debe tener al menos 3 caracteres.")
            continue
        if buscar_usuario(datos.usuarios, nombre) is not None:
            print(f"  Error: el usuario '{nombre}' ya existe.")
            continue
        return nombre


def _pedir_contrasena() -> str:
    """Pide una contraseña válida (mínimo 6 caracteres)."""
    while True:
        contrasena = input("  Contraseña (mín. 6 caracteres): ")
        if len(contrasena) >= 6:
            return contrasena
        print("  Error: la contraseña debe tener al menos 6 caracteres.")


def _normalizar_texto(texto: str) -> str:
    """Convierte manualmente la primera letra a mayúscula y el resto a minúscula.

    No usa .capitalize() ni .title(): recorre carácter por carácter
    usando ord()/chr(), igual que verificar_numero_entero en validaciones.py.
    """
    resultado = ""
    for i in range(len(texto)):
        codigo = ord(texto[i])
        if i == 0:
            if codigo >= 97 and codigo <= 122:      # es minúscula (a-z)
                codigo = codigo - 32                # pasar a mayúscula
        else:
            if codigo >= 65 and codigo <= 90:       # es mayúscula (A-Z)
                codigo = codigo + 32                # pasar a minúscula
        resultado = resultado + chr(codigo)
    return resultado


def _pedir_texto_no_vacio(mensaje: str) -> str:
    """Pide un texto por input y valida que no esté vacío."""
    while True:
        texto = input(mensaje)
        if len(texto) == 0:
            print("  Error: este campo no puede quedar vacío.")
        else:
            return texto


def _pedir_rol_nuevo() -> str:
    """Pide el rol del nuevo usuario: Cliente o Restaurante."""
    while True:
        rol = _pedir_texto_no_vacio("  Rol (Cliente / Restaurante): ")
        rol = _normalizar_texto(rol)
        if rol in ("Cliente", "Restaurante"):
            return rol
        print("  Error: rol inválido. Escribí 'Cliente' o 'Restaurante'.")


def _pedir_domicilio() -> str:
    """Pide un domicilio válido (mínimo 7 caracteres), usando validaciones.py."""
    while True:
        domicilio = input("  Domicilio (mín. 7 caracteres): ")
        if validar_domicilio(domicilio):
            return domicilio


def _pedir_entero(mensaje: str) -> int:
    """Pide un número entero validando con verificar_numero_entero de validaciones.py."""
    while True:
        valor = input(mensaje)
        if verificar_numero_entero(valor):
            return int(valor)
        print("  Error: debe ingresar un número entero válido.")


def _confirmar(mensaje: str = "\n  ¿Confirmar? (s/n): ") -> bool:
    """Pide confirmación s/n (acepta mayúscula o minúscula, sin usar .lower())."""
    while True:
        respuesta = input(mensaje)
        if respuesta in ("s", "S"):
            return True
        if respuesta in ("n", "N"):
            return False
        print("  Respuesta inválida. Escribí 's' o 'n'.")


def _pedir_datos_cliente() -> dict:
    """Pide los datos específicos de un cliente nuevo."""
    print("\n  Completá los datos del cliente:")
    nombre = _pedir_texto_no_vacio("    Nombre    : ")
    apellido = _pedir_texto_no_vacio("    Apellido  : ")
    email = _pedir_texto_no_vacio("    Email     : ")
    telefono = _pedir_texto_no_vacio("    Teléfono  : ")
    domicilio = _pedir_domicilio()
    dni = _pedir_entero("    DNI       : ")
    edad = _pedir_entero("    Edad      : ")

    return {
        "domicilio": domicilio,
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "telefono": telefono,
        "dni": dni,
        "edad": edad,
        "cantidad_pedidos": 0,
    }


def _pedir_datos_restaurante() -> dict:
    """Pide los datos específicos de un restaurante nuevo."""
    print("\n  Completá los datos del restaurante:")
    nombre_local = _pedir_texto_no_vacio("    Nombre del local  : ")
    tipo_cocina = _pedir_texto_no_vacio("    Tipo de cocina    : ")
    telefono = _pedir_texto_no_vacio("    Teléfono          : ")
    domicilio = _pedir_domicilio()

    return {
        "domicilio": domicilio,
        "nombre_local": nombre_local,
        "tipo_cocina": tipo_cocina,
        "telefono": telefono,
        "pedidos_hoy": 0,
        "empleados": 0,
        "facturacion": 0.0,
    }


def _mostrar_usuario_sin_password(usuario: dict):
    """Muestra todos los campos de un usuario, salvo el password."""
    for clave, valor in usuario.items():
        if clave == "password":
            continue
        print(f"    {clave}: {valor}")


# ---------------------------- Funciones principales ----------------------------

def crear_usuario():
    """Crea un nuevo usuario (Cliente o Restaurante) y lo agrega al sistema."""
    limpiar_pantalla()
    print("Crear usuario")

    nombre = _pedir_nombre_usuario_nuevo()
    password = _pedir_contrasena()
    rol = _pedir_rol_nuevo()

    if rol == "Cliente":
        datos_extra = _pedir_datos_cliente()
    else:
        datos_extra = _pedir_datos_restaurante()

    nuevo_usuario = {
        "usuario": nombre,
        "password": password,
        "rol": rol,
    }
    nuevo_usuario.update(datos_extra)

    print("\n  Revisá los datos ingresados:")
    _mostrar_usuario_sin_password(nuevo_usuario)

    if _confirmar():
        datos.usuarios.append(nuevo_usuario)
        guardar_json(RUTA_USUARIOS, datos.usuarios)
        print(f"\n  Usuario '{nombre}' creado exitosamente.")
    else:
        print("\n  Operación cancelada")

    pausar()


def borrar_usuario():
    """Borra un usuario existente del sistema (excepto administradores)."""
    limpiar_pantalla()
    print("Borrar usuario\n")

    if len(datos.usuarios) == 0:
        print("  No hay usuarios registrados.")
        pausar()
        return

    print("  Usuarios registrados:")
    for u in datos.usuarios:
        nombre_mostrar = u.get("nombre", u.get("nombre_local", ""))
        print(f"    • {u['usuario']} — {nombre_mostrar} — {u['rol']}")

    nombre = input("\n  Nombre de usuario a eliminar (mín. 3 caracteres): ")
    if len(nombre) < 3:
        print("  Error: el nombre debe tener al menos 3 caracteres.")
        pausar()
        return

    usuario = buscar_usuario(datos.usuarios, nombre)
    if usuario is None:
        print(f"\n  Error: no existe ningún usuario con el nombre '{nombre}'.")
        pausar()
        return

    print("\n  Datos del usuario a eliminar:")
    _mostrar_usuario_sin_password(usuario)

    if not _confirmar():
        print("\n  Operación cancelada")
        pausar()
        return

    if usuario["rol"] == "Administrador":
        print("\n  Error: no se puede eliminar una cuenta de Administrador.")
        pausar()
        return

    for i in range(len(datos.usuarios)):
        if datos.usuarios[i]["usuario"] == nombre:
            datos.eliminados.append(usuario)
            datos.usuarios.pop(i)
            break

    guardar_json(RUTA_USUARIOS, datos.usuarios)
    guardar_json(RUTA_ELIMINADOS, datos.eliminados)
    print(f"\n  Usuario '{nombre}' eliminado exitosamente.")
    pausar()


def ver_info_sistema():
    """Muestra el submenú de información del sistema."""
    while True:
        limpiar_pantalla()
        print("Información del sistema\n")
        print("  1. Ver integrantes y descripción del sistema")
        print("  2. Ver usuarios por rol")
        print("  0. Volver")

        opcion = input("\n  Elegí una opción: ")

        if opcion == "1":
            print("\n  Integrantes del grupo:")
            for integrante in integrantes:
                print(f"     • {integrante}")
            print(descripcion_sistema)
            print(funcionalidades_extras)
            pausar()

        elif opcion == "2":
            rol = _pedir_texto_no_vacio("\n  Rol a consultar (Cliente / Restaurante / Administrador): ")
            rol = _normalizar_texto(rol)
            if rol not in ("Cliente", "Restaurante", "Administrador"):
                print("  Error: rol inválido.")
                pausar()
                continue

            usuarios_filtrados = filtrar_por_rol(datos.usuarios, rol)
            if len(usuarios_filtrados) == 0:
                print(f"\n  No hay usuarios con el rol '{rol}'.")
            else:
                print(f"\n  Usuarios con rol '{rol}':")
                for u in usuarios_filtrados:
                    print()
                    _mostrar_usuario_sin_password(u)
            pausar()

        elif opcion == "0":
            break

        else:
            print("\n  Opción inválida. Intentá de nuevo.")
            pausar()
