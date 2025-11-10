import random

# 1. Configuración del juego
# Generar un número aleatorio entre 1 y 100 (incluidos)
numero_secreto = random.randint(1, 20)
intentos = 0
adivinado = False

print("--- 🧠 ¡Adivina el Número Secreto! ---")
print("Estoy pensando en un número entre 1 y 20.")

# 2. Bucle principal del juego (se ejecuta mientras no se adivine)
while not adivinado:
    try:
        # Solicitar el intento al usuario//este es el error si escriben decimales
        intento_usuario = int(input("Introduce tu adivinanza: "))
        intentos += 1  # Incrementar el contador de intentos

        # 3. Comprobar la adivinanza
        if intento_usuario == numero_secreto:
            adivinado = True  # Cambia la bandera para salir del bucle
            
        elif intento_usuario < numero_secreto:
            print("❌ Demasiado bajo. ¡Intenta con un número mayor!")
            
        else:
            intento_usuario > numero_secreto
            print("❌ Demasiado alto. ¡Intenta con un número menor!")

    except ValueError:
        print("⚠️ Entrada no válida. Por favor, introduce un número entero.")

# 4. Mensaje de victoria (se ejecuta al salir del bucle)
print(f"\n🎉 ¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
