# 1. Lista original VACIA
numeros_usuario = [] # Usamos un nombre claro para la lista

print("--- 🔢 INGRESO DE NÚMEROS ---")

# 1.1 Solicitamos los números de la lista usando un bucle 'while' interactivo
print("Escribe 'FIN' cuando hayas terminado de ingresar números.")

while True:
    entrada = input("Ingresa un número o 'FIN': ").lower()

    if entrada == 'fin':
        break # Sale del bucle si el usuario escribe 'fin'
    
    try:
        # Intentamos convertir la entrada a un número entero (int)
        nuevo_numero = int(entrada)
        numeros_usuario.append(nuevo_numero)
        print(f" Número {nuevo_numero} agregado.")
    except ValueError:
        # Captura el error si el usuario no escribe un número o 'fin'
        print("⚠️ Entrada no válida. Por favor, ingresa un número entero o 'FIN'.")

# 2. Comprensión de listas para filtrar solo los pares
# La variable 'num' original tenía problemas de alcance; usamos 'numeros_usuario'.
# Condición: si el resto de la división por 2 es 0, es par.
numeros_pares = [num for num in numeros_usuario if num % 2 == 0]

print("\n--- ✅ RESULTADOS ---")
print(f"Lista de todos los números: {numeros_usuario}")
print(f"Lista de solo números pares: {numeros_pares}")