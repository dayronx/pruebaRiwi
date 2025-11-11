# Gestión de estudiantes (mini base de datos).

# 1. Definición del diccionario fuera del bucle para que los cambios sean persistentes
estudiantes = {
    "Juan": {
        "Email": "juan@example.com",
        "Edad": 20,
        "Direccion": "Calle Falsa 123",
        "Team": "Red",
    },
    "Pedro": {
        "Email": "pedro@example.com",
        "Edad": 22,
        "Direccion": "Avenida Siempre Viva",
        "Team": "Blue",
    },
    "Emma": {
        "Email": "emma@example.com",
        "Edad": 19,
        "Direccion": "Elm Street 10",
        "Team": "Green",
    }
}

option = ""

while option != '4':
    
    print("\n--- GESTIÓN DE ESTUDIANTES ---")
    print("1:: MOSTRAR")
    print("2:: INGRESAR ")
    print("3:: ELIMINAR")
    print("4:: SALIR")
    print("------------------------------")
    
    option = input("Choose an option (1-4): ").strip()
    print("")

    # --- LÓGICA DE OPCIONES ---
    
    if option == '1':
        ## 1. MOSTRAR
        print("--- LISTA DE ESTUDIANTES ---")
        if not estudiantes:
            print("El diccionario de estudiantes está vacío.")
        else:
            for nombre, datos in estudiantes.items():
                print(f"** Nombre: {nombre} **")
                # Imprime los detalles del estudiante
                for clave, valor in datos.items():
    
                    print(f"  - {clave}: {valor}")
                    
            print("----------------------------")
            
    elif option == '2':  
        ## 2. INGRESAR
        print("--- INGRESAR NUEVO ESTUDIANTE ---")
        nombre_nuevo = input("Nombre del estudiante: ").strip().title()
        
        if nombre_nuevo in estudiantes:
            print(f"❌ Error: El estudiante '{nombre_nuevo}' ya existe.")
        else:
            # Pide los datos del nuevo estudiante
            email = input("Email: ")
            edad = input("Edad: ")
            direccion = input("Dirección: ")
            team = input("Team: ")

            # Crea el diccionario anidado y lo añade
            estudiantes[nombre_nuevo] = {
                "Email": email,
                "Edad": edad,
                "Direccion": direccion,
                "Team": team
            }
            print(f"✅ Estudiante '{nombre_nuevo}' ingresado correctamente.")

    elif option == '3':
        ## 3. ELIMINAR
        print("--- ELIMINAR ESTUDIANTE ---")
        nombre_eliminar = input("Nombre del estudiante a eliminar: ").strip().title()
        
        if nombre_eliminar in estudiantes:
            # Usa el método pop() para eliminar la clave y sus datos
            estudiantes.pop(nombre_eliminar)
            print(f"✅ Estudiante '{nombre_eliminar}' eliminado correctamente.")
        else:
            print(f"❌ Error: El estudiante '{nombre_eliminar}' no se encontró.")

    elif option == '4': 
        ## 4. SALIR
        print("Saliendo del programa. ¡Hasta pronto!")       
        break    
        
    else:
        # Manejo de entrada no válida
        print("⚠️ Opción no válida. Por favor, elige un número del 1 al 4.")