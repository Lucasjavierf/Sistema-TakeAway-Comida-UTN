# Instrucciones para la Entrega 2 — UTN Eats

> Leer esto antes de tocar cualquier archivo.

---

## Distribución de trabajo

| Integrante | Archivo |
|---|---|
| Lucas (ya hecho) | `modulos/datos.py`, `modulos/funciones.py`, `modulos/login.py`, `modulos/app.py`, `modulos/menus.py`, `datos/*.json` |
| Renzo | `roles/administrador.py` |
| Matias | `roles/cliente.py` |
| Juan | `roles/restaurante.py` |

**Cada uno trabaja solo en su archivo.** No tocar lo que hizo otro.

---

## Contexto general

Lucas dejó lista la base de la entrega 2:
- `datos/usuarios.json`, `catalogo.json`, `pedidos.json`, `eliminados.json` — los 4 archivos de datos
- `modulos/datos.py` — carga y guarda JSON
- `modulos/funciones.py` — funciones puras que todos deben usar
- `modulos/login.py` — devuelve el diccionario completo del usuario
- `modulos/app.py` — flujo principal
- `modulos/menus.py` — menús actualizados con parámetros correctos

---

## Funciones disponibles en `modulos/funciones.py`

Importarlas así:
```python
from modulos.funciones import nombre_de_la_funcion
```

| Función | Qué hace |
|---|---|
| `filtrar_catalogo(catalogo, restaurante, categoria)` | Devuelve lista de items del catálogo de ese restaurante y categoría ("comida" o "bebida") |
| `calcular_total_pedido(comida, cant_c, bebida, cant_b)` | Calcula el total. Si no hay bebida, pasar `None` y `0` |
| `buscar_pedidos(pedidos, restaurante, estado)` | Devuelve pedidos filtrados por restaurante y estado |
| `actualizar_estado(pedidos, numero, nuevo_estado)` | Cambia el estado de un pedido en la lista. Devuelve el pedido o None |
| `obtener_pedidos_a_matriz(pedidos, restaurante)` | Devuelve matriz [[numero, total, estado_int], ...] |
| `filtrar_por_rol(usuarios, rol)` | Devuelve usuarios con ese rol ("Cliente", "Restaurante", "Administrador") |
| `buscar_usuario(usuarios, nombre)` | Devuelve el dict del usuario o None |

## Cómo guardar en JSON

```python
from modulos.datos import guardar_json, RUTA_PEDIDOS, RUTA_USUARIOS, RUTA_ELIMINADOS
import modulos.datos as datos

guardar_json(RUTA_PEDIDOS, datos.pedidos)     # después de modificar pedidos
guardar_json(RUTA_USUARIOS, datos.usuarios)   # después de crear/borrar usuario
guardar_json(RUTA_ELIMINADOS, datos.eliminados) # después de borrar usuario
```

> **Regla de oro:** si una función ya existe en `funciones.py`, usarla, no reimplementarla. Si modificás datos, siempre llamar a `guardar_json()` antes de volver al menú.

---

## Estructura de los diccionarios (para no inventar campos)

### Cliente
```python
{
    "usuario": "clienteA",
    "password": "tengohambre123",
    "rol": "Cliente",
    "domicilio": "Av. Siempre Viva 742",
    "nombre": "Lucas",
    "apellido": "Krauz",
    "email": "clienteA@gmail.com",
    "telefono": "11-1234-5678",
    "dni": 38012345,
    "edad": 22,
    "cantidad_pedidos": 5
}
```

### Restaurante
```python
{
    "usuario": "mcdonald",
    "password": "cajitafeliz7",
    "rol": "Restaurante",
    "domicilio": "Medrano 951",
    "nombre_local": "McDonald's UTN",
    "tipo_cocina": "comida rapida",
    "telefono": "11-4444-9876",
    "pedidos_hoy": 15,
    "empleados": 8,
    "facturacion": 250000.0
}
```

### Pedido
```python
{
    "numero": 1234567890123,
    "codigo_entrega": None,
    "cliente": "clienteA",
    "restaurante": "mcdonald",
    "comida": "Hamburguesa clasica",
    "cantidad_comida": 2,
    "bebida": "Coca-Cola",
    "cantidad_bebida": 2,
    "total": 9400.0,
    "estado": "pendiente",
    "fecha": "2025-06-01"
}
```

---






## 👤 Renzo — `roles/administrador.py`

**Firmas que DEBE tener tu archivo** (menus.py las llama así):

```python
def crear_usuario():
def borrar_usuario():
def ver_info_sistema():
```

### `crear_usuario()`

1. Pedir y validar nombre de usuario (mínimo 3 caracteres), verificar que no exista ya con `buscar_usuario(datos.usuarios, nombre)`
2. Pedir contraseña (mínimo 6 caracteres)
3. Pedir rol: solo `"Cliente"` o `"Restaurante"` (con mayúscula, así está en el JSON)
4. Pedir los datos correspondientes según el rol:
   - **Cliente:** nombre, apellido, email, teléfono, domicilio (mín. 7 chars), dni (int), edad (int) → `cantidad_pedidos: 0`
   - **Restaurante:** nombre_local, tipo_cocina, teléfono, domicilio (mín. 7 chars) → `pedidos_hoy: 0`, `empleados: 0`, `facturacion: 0.0`
5. Mostrar todos los datos ingresados y pedir confirmación (s/n)
6. Si confirma:
   - Armar el diccionario con todos los campos y agregarlo a `datos.usuarios`
   - `guardar_json(RUTA_USUARIOS, datos.usuarios)`
   - Mostrar mensaje de éxito
7. Si rechaza, mostrar "Operación cancelada" y volver

### `borrar_usuario()`

1. Mostrar lista de todos los usuarios con `datos.usuarios`, mostrando: usuario, nombre/nombre_local y rol
2. Pedir el nombre de usuario a eliminar (mínimo 3 caracteres)
3. Buscar con `buscar_usuario(datos.usuarios, nombre)`
4. Si no existe, mostrar error y volver
5. Si existe, mostrar todos sus datos y pedir confirmación (s/n)
6. Si confirma:
   - Protección: si el rol es `"Administrador"` no permitir el borrado
   - Guardar el usuario en `datos.eliminados` con `.append()`
   - Borrarlo de `datos.usuarios` con `.pop(i)`
   - `guardar_json(RUTA_USUARIOS, datos.usuarios)`
   - `guardar_json(RUTA_ELIMINADOS, datos.eliminados)`
   - Mostrar mensaje de éxito
7. Si rechaza, mostrar "Operación cancelada"

### `ver_info_sistema()`

Mostrar un submenú:
```
1. Ver integrantes y descripción del sistema
2. Ver usuarios por rol
0. Volver
```

- Opción 1: igual que la entrega 1 (integrantes, descripción, funcionalidades extras)
- Opción 2: pedir el rol (`"Cliente"`, `"Restaurante"` o `"Administrador"`), usar `filtrar_por_rol(datos.usuarios, rol)` y mostrar los datos de cada usuario sin mostrar la contraseña

### Imports que necesitás
```python
import modulos.datos as datos
from modulos.datos import guardar_json, RUTA_USUARIOS, RUTA_ELIMINADOS
from modulos.funciones import filtrar_por_rol, buscar_usuario
from modulos.utilidades import pausar, limpiar_pantalla
from modulos.validaciones import esperar_menu
```







---

## 👤 Matias — `roles/cliente.py`

**Firmas que DEBE tener tu archivo** (menus.py las llama así):

```python
def ver_datos_cliente(usuario: dict):
def realizar_pedido(usuario: dict, catalogo: list, pedidos: list):
def ver_pedidos_en_preparacion(usuario: dict, pedidos: list):
```

### `ver_datos_cliente(usuario)`
Mostrar los campos del diccionario `usuario`. No mostrar `password`.
Campos disponibles: `usuario`, `rol`, `domicilio`, `nombre`, `apellido`, `email`, `telefono`, `dni`, `edad`, `cantidad_pedidos`

### `realizar_pedido(usuario, catalogo, pedidos)`
1. Pedir nombre del restaurante (mínimo 3 caracteres)
2. Verificar que existe con `buscar_usuario(datos.usuarios, nombre_restaurante)` y que su rol sea `"Restaurante"`. Si no existe, informar error y volver.
3. Mostrar comidas con `filtrar_catalogo(catalogo, nombre_restaurante, "comida")`
4. El usuario elige una comida (por número) y la cantidad (1-10)
5. Mostrar bebidas con `filtrar_catalogo(catalogo, nombre_restaurante, "bebida")` + opción 0 para ninguna
6. Si elige bebida, pedir cantidad (1-10)
7. Calcular total con `calcular_total_pedido(comida_dict, cant_c, bebida_dict, cant_b)`. Si no hay bebida pasar `None` y `0`
8. Mostrar ticket con todos los datos y preguntar si confirma (s/n)
9. Si confirma:
   - Generar número único de 13 cifras verificando que no esté ya en `pedidos`
   - Armar el diccionario del pedido con EXACTAMENTE esta estructura:
   ```python
   nuevo_pedido = {
       "numero": numero_generado,
       "codigo_entrega": None,
       "cliente": usuario["usuario"],
       "restaurante": nombre_restaurante,
       "comida": comida_dict["nombre"],
       "cantidad_comida": cant_c,
       "bebida": bebida_dict["nombre"] if bebida_dict else "ninguna",
       "cantidad_bebida": cant_b,
       "total": total,
       "estado": "pendiente",
       "fecha": "2025-06-01"
   }
   ```
   - `pedidos.append(nuevo_pedido)`
   - `guardar_json(RUTA_PEDIDOS, pedidos)`
   - Mostrar confirmación con el número de pedido
10. Si rechaza, mostrar "Pedido cancelado"

### `ver_pedidos_en_preparacion(usuario, pedidos)`
1. Filtrar los pedidos donde `pedido["cliente"] == usuario["usuario"]` y `pedido["estado"] == "en_preparacion"`
2. Si no hay ninguno, mostrar mensaje de error
3. Por cada pedido mostrar claramente: **código de entrega**, número de pedido, restaurante, comida, bebida y total

### Imports que necesitás
```python
import modulos.datos as datos
from modulos.datos import guardar_json, RUTA_PEDIDOS
from modulos.funciones import filtrar_catalogo, calcular_total_pedido, buscar_usuario
from modulos.validaciones import verificar_numero_entero, esperar_menu
from modulos.utilidades import generar_numero_pedido, pausar
```





---

## 👤 Juan — `roles/restaurante.py`

**Firmas que DEBE tener tu archivo** (menus.py las llama así):

```python
def ver_datos_restaurante(usuario: dict):
def preparar_pedido(usuario: dict, pedidos: list):
def entregar_pedido(usuario: dict, pedidos: list):
def ver_facturacion(usuario: dict, pedidos: list):
```

### `ver_datos_restaurante(usuario)`
Mostrar los campos del diccionario `usuario`. No mostrar `password`.
Campos disponibles: `usuario`, `rol`, `domicilio`, `nombre_local`, `tipo_cocina`, `telefono`, `pedidos_hoy`, `empleados`, `facturacion`

### `preparar_pedido(usuario, pedidos)`
1. Usar `buscar_pedidos(pedidos, usuario["usuario"], "pendiente")` para obtener pendientes
2. Si no hay ninguno, mostrar error y volver
3. Mostrar la lista: número, cliente, comida y total
4. Pedir el número de pedido a preparar. Si no está en la lista, mostrar error
5. Mostrar detalle del pedido y pedir confirmación (s/n)
6. Si confirma:
   - `actualizar_estado(pedidos, numero, "en_preparacion")`
   - Generar código de entrega: `random.randint(1000, 9999)` y guardarlo en `pedido["codigo_entrega"]`
   - `guardar_json(RUTA_PEDIDOS, pedidos)`
   - Mostrar confirmación (**NO mostrar el código de entrega** al restaurante)
7. Si rechaza, mostrar "Operación cancelada"

### `entregar_pedido(usuario, pedidos)`
1. Usar `buscar_pedidos(pedidos, usuario["usuario"], "en_preparacion")`
2. Si no hay ninguno, mostrar error y volver
3. Mostrar lista (**sin mostrar el código de entrega**)
4. Pedir número de pedido. Si no está, mostrar error
5. Pedir código de entrega por input
6. Si el código coincide con `pedido["codigo_entrega"]`:
   - `actualizar_estado(pedidos, numero, "entregado")`
   - `guardar_json(RUTA_PEDIDOS, pedidos)`
   - Mostrar "Pedido entregado con éxito"
7. Si no coincide, mostrar error

### `ver_facturacion(usuario, pedidos)`
1. Llamar `obtener_pedidos_a_matriz(pedidos, usuario["usuario"])`
2. Si la matriz está vacía, mostrar mensaje
3. Imprimir tabla con encabezado y filas. Convertir el estado de int a texto: 1=pendiente, 2=en_preparacion, 3=entregado
4. Al final mostrar el total sumando la columna `total` de cada fila

Ejemplo de formato:
```
+---------------+----------+-----------------+
| Número        | Total    | Estado          |
+---------------+----------+-----------------+
| 1234567890123 | $9400.0  | pendiente       |
| 9876543210987 | $2500.0  | en_preparacion  |
+---------------+----------+-----------------+
| TOTAL                    | $11900.0        |
+---------------+----------+-----------------+
```

### Imports que necesitás
```python
import random
import modulos.datos as datos
from modulos.datos import guardar_json, RUTA_PEDIDOS
from modulos.funciones import buscar_pedidos, actualizar_estado, obtener_pedidos_a_matriz
from modulos.validaciones import verificar_numero_entero, esperar_menu
from modulos.utilidades import pausar
```