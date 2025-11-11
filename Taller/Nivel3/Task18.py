# Sumar hasta que el usuario escriba 0.




# Inicializamos la variable que guardará la suma total
total_sum = 0

# Inicializamos la variable que guarda el número ingresado.
# La inicializamos con un valor distinto de 0 para que el bucle comience.
number = -1 

print("--- Number Adder ---")
print("Enter numbers to sum. The process will terminate when you enter 0.")


while number != 0 :
    try:
         
        number = int(input("Enter a number (0 to exit): "))
        
        # Sumamos el número ingresado a la suma total
        total_sum += number



    except ValueError:
         print("Please only enter integers.")



# Al salir del bucle, mostramos el resultado final.
print(f"\nProcess finished. The total sum of all numbers entered is: {total_sum}")
