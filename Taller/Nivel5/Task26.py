# Simplified Product and Price Menu (Discount Store / D1-type Warehouse)

# 1. Catálogo de productos para referencia visual
print("--------------------------------------------------------------------------------------------------------------")
print("----------------------------- Product and Price Catalog ------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")

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

# 2. Diccionario de precios (Se mantiene intacto)
products_and_prices = {
    "Milk"   : 44, "Bread"      : 555, "Eggs"     : 120, "Detergent"   : 65, "Sugar"  : 300,
    "Rice"   : 80, "Toothpaste" : 15 , "Oil"      : 75 , "Tuna"        : 20, "Coffee" : 100,
    "Soap"   : 45, "Shampoo"    : 18 , "Lentils"  : 90 , "Toilet_Paper": 35, "Beans"  : 145,
    "Salt"   : 60, "Soda"       : 25 , "Flour"    : 115, "Butter"      : 50, "Cheese" : 160,
    "Oats"   : 70, "Cookies"    : 10 , "Fish"     : 85 , "Gelatin"     : 40, "Chicken": 190,
    "Carrot" : 55, "Apple"      : 30 , "Tomato"   : 130, "Lemon"       : 95, "Potato" : 210,
    "Onion"  : 48, "Banana"     : 22 , "Avocado"  : 105, "Lettuce"     : 68, "Orange" : 175
}

# 3. Inicializamos del carrito
shopping_car = [] 

print("--------------------------------------------------------------------------------------------------------------")
print("Escribe el nombre del producto (ej: Milk) o 'pay' para finalizar.")
print("--------------------------------------------------------------------------------------------------------------")







# 4. Bucle para añadir productos 
while True:
    # Se pide el producto y se usa .title() para que coincida con las claves del diccionario (ej: milk -> Milk)
    new_product = input("¿Qué producto quieres añadir?: ").strip().title() 
    
    if new_product.lower() == 'pay':
        break 
    
    # Intenta añadir el producto
    # Se añade la verificación para que solo se agreguen productos válidos
    if new_product in products_and_prices:
        shopping_car.append(new_product)
        print(f" '{new_product}' añadido al carrito!")
    else:
        # Mensaje de error más específico para productos no encontrados
        print(f" Producto '{new_product}' no encontrado. Por favor, revisa el catálogo y la ortografía.")


print("**********************************************")
print(" RESUMEN DE LA COMPRA ")
print("**********************************************")

total_a_pagar = 0

if not shopping_car:
    print("El carrito está vacío. ¡No hay nada que pagar!")
else:
    # 5. Calcular el total y listar productos
    print("\n--- PRODUCTOS AGREGADOS ---")
    
    # Se usa un diccionario temporal para contar las cantidades y listarlas mejor
    conteo_productos = {}
    
    for producto in shopping_car:
        # Contar cuántas veces aparece cada producto
        conteo_productos[producto] = conteo_productos.get(producto, 0) + 1
        
        # Sumar el precio al total
        precio = products_and_prices.get(producto, 0) # Obtener el precio, 0 si no existe (aunque ya validamos)
        total_a_pagar += precio

    # Mostrar la lista detallada y el total
    for producto, cantidad in conteo_productos.items():
        precio_unitario = products_and_prices[producto]
        subtotal = cantidad * precio_unitario
        print(f"  * {cantidad} x {producto} (Precio Unitario: {precio_unitario}) - Subtotal: {subtotal}")

    print("\n----------------------------------------------")
    print(f"🛒 Lista de todos los productos (orden de ingreso): {shopping_car}")
    print("----------------------------------------------")
    print(f" VALOR TOTAL A PAGAR: {total_a_pagar}")
    print("**********************************************")

# Nota: Se eliminó el bloque 'try-except' porque no se estaban manejando números enteros,
# sino validando contra el diccionario de productos.