# # Objetivo: Crear, recorrer, modificar y eliminar elementos en listas.

# #     Lista de frutas.
# #     Agregar y eliminar frutas.
# #     Buscar un elemento en la lista.




# Initial List
fruits = ["apple", "banana", "cherry", "grape"]
option = ""

print("--- 🍇 INTERACTIVE FRUIT MANAGEMENT ---")
print(f"Current list: {fruits}")

# The loop repeats until the user chooses to exit (option 4)
while option != "4":
    print("\n--- MENU ---")
    print("1. Add fruit")
    print("2. Remove fruit")
    print("3. Show current list")
    print("4. Exit")
    
    option = input("Choose an option (1-4): ")

    if option == "1":
        # Option 1: ADD FRUIT
        new_fruit = input("Which fruit do you want to add?: ").lower()
        fruits.append(new_fruit)
        print(f"'{new_fruit.capitalize()}' added!")
        
    elif option == "2":
        # Option 2: REMOVE FRUIT
        fruit_to_remove = input("Which fruit do you want to remove?: ").lower()
        
        if fruit_to_remove in fruits:
            fruits.remove(fruit_to_remove)
            print(f"'{fruit_to_remove.capitalize()}' removed!")
        else:
            print(f"Error: '{fruit_to_remove.capitalize()}' is not in the list.")
            
    elif option == "3":
        # Option 3: SHOW LIST
        print(f"\nCurrent list: {fruits}")

    elif option == "4":
        # Option 4: EXIT
        print(" Exiting the fruit manager. Goodbye!")
        
    else:
        # Invalid option
        print(" Invalid option. Please choose 1, 2, 3, or 4.")

print(f"Final list saved: {fruits}")