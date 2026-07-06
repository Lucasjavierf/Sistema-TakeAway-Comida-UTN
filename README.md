# Sistema Take Away de Comida - UTN

## Descripción

Sistema desarrollado en Python que simula una plataforma de pedidos Take Away con tres tipos de usuarios: **Cliente**, **Restaurante** y **Administrador**.

El proyecto fue desarrollado como trabajo práctico para la materia de Programación de la Universidad Tecnológica Nacional (UTN), aplicando programación estructurada, modularización, persistencia mediante archivos JSON y reutilización de funciones.

---

# Objetivos

* Implementar un sistema modular utilizando funciones.
* Administrar distintos tipos de usuarios según su rol.
* Persistir la información del sistema mediante archivos JSON.
* Aplicar validaciones de datos y separación de responsabilidades.
* Simular el flujo completo de un pedido de comida.

---


# Estructura del proyecto

```
Sistema-TakeAway-Comida-UTN/

│
├── datos/
│   ├── catalogo.json
│   ├── usuarios.json
│   ├── pedidos.json
│   └── eliminados.json
│
├── modulos/
│   ├── app.py
│   ├── datos.py
│   ├── funciones.py
│   ├── login.py
│   ├── menus.py
│   ├── prints.py
│   ├── utilidades.py
│   └── validaciones.py
│
├── roles/
│   ├── administrador.py
│   ├── cliente.py
│   └── restaurante.py
│
├── main.py
└── README.md
```

---

# Funcionalidades

## Cliente

* Inicio de sesión.
* Visualización de datos personales.
* Realización de pedidos.
* Consulta de pedidos en preparación.
* Confirmación del pedido antes de registrarlo.

## Restaurante

* Visualización de datos.
* Consulta de pedidos pendientes.
* Cambio de estado a "En preparación".
* Entrega de pedidos mediante código de entrega.
* Consulta de facturación utilizando una matriz.

## Administrador

* Alta de usuarios.
* Baja de usuarios.
* Consulta de usuarios por rol.
* Visualización de información general del sistema.

---

# Persistencia de datos

Toda la información del sistema se almacena mediante archivos JSON.

* **usuarios.json** → Usuarios registrados.
* **catalogo.json** → Productos disponibles.
* **pedidos.json** → Pedidos realizados.
* **eliminados.json** → Historial de usuarios eliminados.

Cada modificación realizada desde el sistema se guarda automáticamente antes de regresar al menú principal.

---

# Funciones principales

El proyecto implementa las funciones solicitadas por la consigna:

* filtrar_catalogo()
* calcular_total_pedido()
* buscar_pedidos()
* actualizar_estado()
* obtener_pedidos_a_matriz()
* filtrar_por_rol()
* buscar_usuario()

Estas funciones fueron diseñadas para reutilizar lógica y mantener un código organizado.

---

# Organización del proyecto

El sistema fue dividido en módulos para separar responsabilidades.

* **roles/** contiene la lógica específica de Cliente, Restaurante y Administrador.
* **modulos/** contiene la lógica general compartida por todo el sistema.
* **datos/** almacena la persistencia de la información.

Esta organización facilita el mantenimiento del código y el trabajo colaborativo.
