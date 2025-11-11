
numeros_usuario = [] 

print("---  INGRESO DE NÚMEROS ---")


print("Escribe 'FIN' cuando hayas terminado de ingresar números.")

while True:
    entrada = input("Ingresa un número o 'FIN': ").lower()

    if entrada == 'fin':
        break 
    
    try:

        nuevo_numero = int(entrada)
        numeros_usuario.append(nuevo_numero)
        print(f" Número {nuevo_numero} agregado.")
    except ValueError:

        print(" Entrada no válida. Por favor, ingresa un número entero o 'FIN'.")

numeros_pares = [num for num in numeros_usuario if num % 2 == 0]

print("\n--- RESULTADOS ---")
print(f"Lista de todos los números: {numeros_usuario}")
print(f"Lista de solo números pares: {numeros_pares}")