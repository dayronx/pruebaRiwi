# 1. Validación de datos con condicionales:

#     Crea un menú que pregunte al usuario qué acción desea realizar:-----
#         Agregar producto
#         Mostrar inventario
#         Calcular estadísticas
#         Salir
#     Usa condicionales if, elif y else para procesar la opción elegida.
#     Si el usuario ingresa una opción inválida, muestra un mensaje de error y pide nuevamente la entrada.







print("1::Agregar producto")
print("2::Mostrar inventario")
print("3::Calcular estadísticas")
print("4::Salir")
opcion=int(input("Dijiste una opcion "))

if opcion ==1:
    print("1::Agregar producto")
elif opcion==2:
    print("2::Mostrar inventario")
elif opcion==3:
    print("3::Calcular estadísticas")
elif opcion==4:
        print("4::Salir")
else:
    print("El numero no esta en la lista")        



