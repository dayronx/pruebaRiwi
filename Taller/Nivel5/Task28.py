

# 1. El diccionario 'estudiantes' debe estar FUERA del bucle
# para que los cambios se mantengan.
estudiantes  = {
    "Juan": {
        "Email": "juan@example.com",
        "Edad": 20,
        "Direccion": "Calle 123",
        "Team": "A",
    },
    "Pedro": {
        "Email": "pedro@example.com",
        "Edad": 22,
        "Direccion": "Avenida 456",
        "Team": "B",
    },
    "Emma": {
        "Email": "emma@example.com",
        "Edad": 21,
        "Direccion": "Carrera 789",
        "Team": "A",
    }
}

print("# Gestión de estudiantes (mini base de datos) 👨‍🎓")
print("")
option = ""


while option != '4':
    
    print("--- MENÚ ---")
    print("1:: MOSTRAR todos los estudiantes")
    print("2:: INGRESAR nuevo estudiante")
    print("3:: ELIMINAR estudiante")
    print("4:: SALIR")
    print("------------")
    option = input("Elige una opción (1-4): ")
    print("")

    if option == '1':
            #MOSTRAR
            if estudiantes:
                print("---------------LISTA DE ESTUDIANTES -----------------------")
                for nombre, datos in estudiantes.items():
                    print(f"nombre: --{nombre}--")
                    for clave, valor in datos.items():
                        print(f"-- {clave}: {valor}")
                print("----------------------------------------------")         
            else:
                print("la base datos esta vacia  ")

    elif option =='2':
        #ingresar
        print("--- INGRESAR NUEVO ESTUDIANTE ---")
        nuevo_nombre = input("introduce el nombre del estudiante").strip().capitalize()

        if nuevo_nombre in estudiantes:
            print("Error el estudiante {nuevo_nombre} ya existe")
        elif not nuevo_nombre:
            print(f"error el nombre no puede estar vacio")
        else:
            #tomar los datos
            email=input("ingresa el corre: ").strip
            edad=input("ingresa la edad:  ").strip
            direccion=input("ingresa la direccion").strip
            team=input("introduce el equipo de trabajo:  ").strip

            #guardar datos en el diccionario
            estudiantes[nuevo_nombre] = {

                "Email" : email,
                "Edad"  : edad,
                "Direccion" : direccion,
                "Team" : team,
            }
            print(f"el estudiante, {nuevo_nombre} fue añadido correctamente")            

    elif option =='3':
        #Eliminar
        print("------Eliminar Estudiante-----")
        if not estudiantes:
            print("No hayu estudiantes para eliminar ")
        else:
            nombre_eliminar = input("introduce el nombre del estudiante a eliminar: ").strip().capitalize()
            if nombre_eliminar in estudiantes:
                del estudiantes[nombre_eliminar]
                print(f"Estudiante {nombre_eliminar} -- eliminado correctamnete")
            else:
                print(f"error el estudiante --{nombre_eliminar},--no se encontro en la base de datos")
        print("----------------------------------------------------")               

    elif option =='4':
        # 4:: SALIR
        print("Saliendo... ¡Adiós!")       
        break    

    else:
        # Opción inválida
        print(" Opción no válida. Por favor, elige un número entre 1 y 4.")
    
    print("") # Salto de línea para mejor separación entre iteraciones

