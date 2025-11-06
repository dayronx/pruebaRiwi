
    # Crea un archivo inventario.py.
    # Declara variables para nombre (string), precio (float) y cantidad (int).
    # Solicita al usuario estos datos con la función input().
    # Asegúrate de que el precio y la cantidad se conviertan correctamente a sus tipos numéricos usando float() e int().
    # Si el usuario ingresa un valor inválido, muestra un mensaje y vuelve a pedirlo.



#     = str(input(""))
# price    = float(input(""))
# quantity = int(input(""))


# 📋 Código sencillo para principiantes

# 1. Solicitar Nombre (String)
# Un string siempre es fácil de capturar.
product_name = input("Enter the product name: ")

# 2. Solicitar y validar el Precio (Float)
# Usamos un ciclo para repetir si hay error.
while True:
    # Pedimos el dato
    price_text = input("Enter the product price (e.g., 15.99): ")
    
    # Intentamos convertir el texto a número (float)
    try:
        price = float(price_text)
        # Si la conversión funciona, salimos del ciclo.
        break  
    except ValueError:
        # Si la conversión falla (ej. el usuario escribió "Hola"), mostramos error y el ciclo se repite.
        print(" Error: You must enter a number for the price!")

# 3. Solicitar y validar la Cantidad (Int)
# Hacemos exactamente lo mismo, pero usando int().
while True:
    # Pedimos el dato
    quantity_text = input("Enter the quantity (whole number): ")
    
    # Intentamos convertir el texto a número (int)
    try:
        quantity = int(quantity_text)
        # Si la conversión funciona, salimos del ciclo.
        break  
    except ValueError:
        # Si la conversión falla, mostramos error y el ciclo se repite.
        print(" Error: You must enter a WHOLE number for the quantity!")


# 4. Mostrar el resultado (Confirmación)
print("\n Data entered successfully:")
print(f"Product: {product_name}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")