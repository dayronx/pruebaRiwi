
    # Crea un archivo inventario.py.
    # Declara variables para nombre (string), precio (float) y cantidad (int).
    # Solicita al usuario estos datos con la función input().
    # Asegúrate de que el precio y la cantidad se conviertan correctamente a sus tipos numéricos usando float() e int().
    # Si el usuario ingresa un valor inválido, muestra un mensaje y vuelve a pedirlo.






name=input("enter a name  ")


# Solo permite 3 intentos (i=0, 1, 2)
for i in range(3): 

    price_text = input(f"Enter the product price (Attempt {i + 1}/3): ")
    
    try:
        price = float(price_text)
        # Si tiene éxito, usamos break para salir del ciclo for

        break 
    except ValueError:
        if i < 2:
            print("Error: Must be a valid decimal number. Try again.")
        else:
            # i es 2 (el tercer intento). 
            print(" Max attempts reached for price. Setting price to 0.0.")
            price = 0.0
            # No necesitamos break porque el ciclo termina aquí de todos modos,
            # pero lo pondríamos si el range fuera mayor.


# Solicitar y validar la Cantidad (Int) - 3 Intentos
quantity = 0
for i in range(3):
    quantity_text = input(f"Enter the quantity (Attempt {i+1}/3): ")
    try:
        quantity = int(quantity_text)
        # Si tiene éxito, usamos break para salir del ciclo for
        break
    except ValueError:
        if i < 1:
            print(" Error: Must be a WHOLE number. Try again.")
        else:
            print("Max attempts reached for quantity. Setting quantity to 0.")
            quantity = 0



print("...................")
print("\nData entered successfully:")
print("...................")
print(f"Product: {name}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print("...................")
