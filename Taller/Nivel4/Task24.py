numeros_usuario = []

print("ingreso de numeros")


while True:
        
    try:
        entrada = input("Ingresa un número o 'FIN': ")
        

        if entrada == 'fin':
                break
        else:
            numero_nuevo = int(entrada)
            numeros_usuario.append(numero_nuevo)
            print(f"{numero_nuevo}  agregado")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero o 'FIN'.")
        


print("\n--- RESULTADOS ---")
print(f"Lista de todos los números: {numeros_usuario}")
# print(f"Lista de solo números pares: {numeros_pares}")             