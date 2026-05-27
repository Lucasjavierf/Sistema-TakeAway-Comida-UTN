# -Sistema-TakeAway-Comida-UTN
Sistema de Take Away de comida desarrollado en Python para la materia de Programación.

📌 Descripción:
UTN Eats es una aplicación por consola que simula el funcionamiento básico de un sistema de pedidos de comida take away.

El sistema permite la interacción entre distintos tipos de usuarios:

Cliente
Restaurante
Administrador

Cada rol posee funcionalidades y menús propios.

🎯 Objetivo del proyecto

El objetivo principal de esta entrega es:

Organizar correctamente un programa en Python
Utilizar funciones
Validar datos ingresados por el usuario
Modularizar el código
Diferenciar funcionalidades según el rol del usuario
Simular el flujo básico de un sistema de pedidos

👥 Integrantes :

Estructura del proyecto
Sistema-TakeAway-Comida-UTN/
│
├── main.py
│
├── modulos/
│   ├── administrador.py
│   ├── cliente.py
│   ├── restaurante.py
│   ├── login.py
│   ├── menus.py
│   ├── validaciones.py
│   ├── utilidades.py
│   ├── datos.py
│   └── prints.py
│
├── README.md
└── .gitignore



📁 Descripción de archivos
---------------main.py-----------------
Solo ejecuta el sistema con una llamada a iniciar.app() 


---------------App.py------------------
Archivo principal del sistema.
Se encarga de:

-iniciar el programa
-mostrar la presentación
-ejecutar el login
-redirigir según el rol del usuario


---------------prints.py------------
Contiene funciones relacionadas a:

-mensajes
-títulos
-menús
-presentación visual del sistema


--------------login.py--------------
Manejo del inicio de sesión:

-validación de usuario
-validación de contraseña
-identificación del rol


-------------menus.py---------------
Contiene los distintos menús del sistema:

-menú cliente
-menú restaurante
-menú administrador



---------------validaciones.py-------------
Funciones reutilizables para validar:

-nombres
-contraseñas
-rangos numéricos
-códigos
-domicilios
-entradas del usuario


---------------datos.py------------------
Almacena datos hardcodeados del sistema:

-usuarios
-comidas
-bebidas
-datos de clientes
-datos de restaurantes


-------------utilidades.py------------
Funciones auxiliares reutilizables.
Ejemplos:

-limpiar pantalla
-pausar ejecución
-generar números aleatorios


-------------cliente.py---------------
Funciones correspondientes al rol Cliente:

-ver datos
-realizar pedidos
-seleccionar comidas y bebidas
-calcular totales


------------------restaurante.py----------------------
Funciones correspondientes al rol Restaurante:

-ver datos
-preparar pedidos
-entregar pedidos


-----------------administrador.py-----------------------
Funciones correspondientes al rol Administrador:

-crear usuarios
-borrar usuarios
-visualizar información del sistema