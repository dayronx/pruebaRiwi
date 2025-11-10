#     Lista de números y promedio.
#     Números pares: guardar solo los pares.
#     Eliminar duplicados.

#             IMPORTANTE !!!!!!

# Símbolo,Significado,Función
# :,Indica que se va a aplicar un formato.,Separa la variable de la instrucción de formato.
# .2,Indica la precisión.,Le dice a Python cuántos dígitos debe mostrar después del punto decimal.
# f,Indica el tipo.,Le dice a Python que trate el valor como un número de punto flotante (float).




# 3. LISTA DE NÚMEROS Y PROMEDIO
numbers = [15, 20, 35, 40, 10]
add = sum(numbers)
count = len(numbers)
average = add / count

print("---  NUMBER AVERAGE ---")
print(f"List of numbers: {numbers}")
print(f"Total sum: {add}")
print(f"The average is: {average:.2f}")
print("-" * 35)