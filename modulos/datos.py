"""
Módulo de carga y persistencia de datos.

Maneja la lectura y escritura de los archivos JSON del sistema.
Al importar este módulo, todas las listas quedan cargadas en memoria
y disponibles para el resto de los módulos.
"""

import json
import os

# Rutas de los archivos JSON
RUTA_USUARIOS   = os.path.join("datos", "usuarios.json")
RUTA_CATALOGO   = os.path.join("datos", "catalogo.json")
RUTA_PEDIDOS    = os.path.join("datos", "pedidos.json")
RUTA_ELIMINADOS = os.path.join("datos", "eliminados.json")


def cargar_json(ruta: str) -> list:
    """Carga un archivo JSON y devuelve su contenido como lista de diccionarios.

    Args:
        ruta (str): Ruta al archivo JSON.

    Returns:
        list: Lista de diccionarios con los datos del archivo.
    """
    archivo = open(ruta, "r", encoding="utf-8")
    contenido = archivo.read()
    archivo.close()
    return json.loads(contenido)


def guardar_json(ruta: str, datos: list) -> None:
    """Guarda una lista de diccionarios en un archivo JSON.

    Args:
        ruta (str): Ruta al archivo JSON.
        datos (list): Lista de diccionarios a guardar.
    """
    archivo = open(ruta, "w", encoding="utf-8")
    archivo.write(json.dumps(datos, indent=4, ensure_ascii=False))
    archivo.close()


# Listas cargadas en memoria al iniciar el programa
usuarios   = cargar_json(RUTA_USUARIOS)
catalogo   = cargar_json(RUTA_CATALOGO)
pedidos    = cargar_json(RUTA_PEDIDOS)
eliminados = cargar_json(RUTA_ELIMINADOS)
