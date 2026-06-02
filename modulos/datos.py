"""
Datos hardcodeados del sistema.

También:
menú de comidas, bebidas, datos del cliente, datos del restaurante, etc...
"""


usuarios = [
    {
        "usuario": "clienteA",
        "password": "tengohambre123",
        "rol": "cliente"
    },

    {
        "usuario": "mcdonald",
        "password": "cajitafeliz7",
        "rol": "restaurante"
    },

    {
        "usuario": "adminrappi",
        "password": "admin1234",
        "rol": "admin"
    }
]

Menu_comidas = ["pizza", "hamburguesa", "milanesa"]
precio_comidas = [5000, 3000, 4000]
Menu_bebidas = ["coca-cola", "sprite", "agua"]
precio_bebidas = [1500, 1500, 1000]

datos_restaurante = ["Resto UTN", "Medrano 951", "comida rápida", "11-4444-9876", 15, 8, 250000.0]



#Datos de cliente
Domicilio_cliente = "Av. Siempre Viva 742"

Datos_string_cliente = [
    "Nombre: clienteA",
    "Apellido: Krauz",
    "Email: cleinteA@gmail.com",
    "Telefono: 11-1234-5678"
]

Datos_int_cliente = [
    5,      # cantidad pedidos
    25000,  # gasto total
    3000    # ultimo pedido
]

pedido_actual = None