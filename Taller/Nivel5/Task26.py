# Simplified Product and Price Menu (Discount Store / D1-type Warehouse)

print("--- Product and Price Catalog ---")

# Row 1
print("Milk: 44   |  Bread: 555      |   Eggs: 120      | Detergent: 65      |  Sugar: 300")

# Row 2
print("Rice: 80   |  Toothpaste: 15  |   Oil: 75        | Tuna: 20           |  Coffee: 100")

# Row 3
print("Soap: 45   |  Shampoo: 18     |   Lentils: 90    | Toilet_Paper: 35   |  Beans: 145")

# Row 4
print("Salt: 60   |  Soda: 25        |   Flour: 115     | Butter: 50         |  Cheese: 160")

# Row 5
print("Oats: 70   |  Cookies: 10     |   Fish: 85       | Gelatin: 40        |  Chicken: 190")

# Row 6
print("Carrot: 55 |  Apple: 30       |   Tomato: 130    | Lemon: 95          |  Potato: 210")

# Row 7
print("Onion: 48  |  Banana: 22      |   Avocado: 105   | Lettuce: 68        |  Orange: 175")




carrito_de_compras = []

new_compra= input("Which fruit do you want to add?:  | cuando desees dejar de agregar escribe FIN  ").lower()
carrito_de_compras.append(new_compra)
print("*********************************************************************")
print(f"✅ '{new_compra.capitalize()}' added!")
print("*********************************************************************")
print("|En tu carrito de compra tienes los siguientes productos|")
print(carrito_de_compras)
print("*********************************************************************")
quantity = int(input("Enter quantity of prodcut"))




# # --- 1. SISTEMA DE PRECIOS (INVENTARIO) ---
# # Este diccionario contiene los precios fijos de tu sistema.
# INVENTORY_PRICES = {
#     "Leche": 44, 
#     "Pan": 555, 
#     "Huevos": 120, 
#     "Detergente": 65, 
#     "Arroz": 80,
#     "Aceite": 75,
#     "Cafe": 100
# }

# # --- 2. CARRITO DE COMPRAS (VACÍO INICIALMENTE) ---
# # Aquí se guardarán las compras del usuario como {Producto: Cantidad}.
# shopping_cart = {}

# # --- 3. FUNCIÓN DE AGREGAR PRODUCTOS ---
# def add_product_to_cart():
#     """Permite al usuario ingresar un producto y cantidad, y lo agrega al carrito."""
    
#     print("\n--- Agregar Producto al Carrito ---")
    
#     # 1. Solicitar el nombre del producto
#     product_name = input("Ingrese el nombre del producto (ej. Leche, Pan, Huevos): ").strip().title()
    
#     # 2. Verificar si el producto existe en el sistema de precios
#     if product_name not in INVENTORY_PRICES:
#         print(f"ERROR: '{product_name}' no existe en nuestro inventario.")
#         return # Sale de la función si el producto no existe
        
#     # 3. Solicitar la cantidad
#     try:
#         quantity = int(input(f"Ingrese la cantidad de '{product_name}' que desea: "))
#         if quantity <= 0:
#             print("ERROR: La cantidad debe ser un número positivo.")
#             return
#     except ValueError:
#         print("ERROR: La cantidad ingresada no es un número válido.")
#         return

#     # 4. Agregar o actualizar el producto en el carrito
#     # Usamos .get() para manejar la situación si el producto ya estaba antes
#     current_quantity = shopping_cart.get(product_name, 0)
#     shopping_cart[product_name] = current_quantity + quantity
    
#     print(f"\n-> Se han agregado {quantity} unidades de '{product_name}'.")

# # --- 4. FUNCIÓN DE CALCULAR TOTAL ---
# def calculate_total(cart):
#     """Calcula el costo total del carrito."""
#     total_price = 0
#     print("\n--- DESGLOSE DE COMPRA ---")
    
#     if not cart:
#         print("El carrito está vacío.")
#         return 0

#     for item, quantity in cart.items():
#         # Obtener el precio unitario del sistema de precios
#         unit_price = INVENTORY_PRICES.get(item, 0) 
        
#         # Multiplicar la cantidad por el precio unitario
#         subtotal = unit_price * quantity
        
#         # Sumar al total
#         total_price += subtotal
        
#         # Imprimir detalle
#         print(f"{quantity}x {item.ljust(15)} @ {unit_price} = {subtotal}")

#     print("-" * 35)
#     print(f"TOTAL A PAGAR: {total_price}")
#     return total_price

# # --- 5. BUCLE PRINCIPAL (INTERACCIÓN CON EL USUARIO) ---
# while True:
#     print("\n==============================")
#     print("Seleccione una opción:")
#     print("1. Agregar producto")
#     print("2. Finalizar compra y calcular total")
#     print("3. Salir")
    
#     choice = input("Opción: ")
    
#     if choice == '1':
#         add_product_to_cart()
    
#     elif choice == '2':
#         calculate_total(shopping_cart)
#         # Después de calcular, podrías romper el bucle si la compra termina:
#         # break 
    
#     elif choice == '3':
#         print("Saliendo del programa. ¡Hasta luego!")
#         break
        
#     else:
#         print("Opción no válida. Intente de nuevo.")









# total_cost = (product*quantity)