
# ---------------------------------------- #
#           EJERCICIOS DE SUMA             #
# ---------------------------------------- #                                                        


# .	Define tres variables: num1 = 25, num2 = 30, num3 = 45. Imprime la suma total de las tres.



# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a second number"))
# num3 = int(input("Enter a third number"))

# print("la suma de los numeros es:")
# print(num1+num2+num3)





# 2.	Pide al usuario que ingrese dos números enteros por separado y luego imprime la suma de estos dos números.



# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a second number"))

# print("la suma de los numeros es:")
# print(num1+num2)


# 3.	Un carrito de compras tiene tres artículos con precios de $15.99, $2.50 y $45.00. Calcula e imprime el monto total a pagar.



# num1 = 15.99
# num2 = 2.50
# num3 = 45.00

# print("El valor de la compra es:")
# print(num1+num2+num3)




# ---------------------------------------- #
#           EJERCICIOS DE RESTA            #
# ---------------------------------------- #

# 1.	Dada la variable saldo_inicial = 500 y un retiro. Calcula e imprime el saldo restante en la cuenta.



# initialBalance = 500
# withdrawal= int(input("Enter the amount to withdraw."))

# s=initialBalance-withdrawal

# print(f"Your available balance is::{s}")


# 2.	Pide al usuario el año actual y su año de nacimiento. Imprime su edad aproximada (la diferencia entre los años).


# age = int(input("Enter your date of birth:"))
# current_Year = 2025

# a=current_Year-age

# print(f"Your age is: {a}")



# -------------------------------------------------#
#           EJERCICIOS DE MULTIPLICACION           #
# -------------------------------------------------#


# 1.	Una receta requiere 3 huevos. Calcula e imprime la cantidad total de huevos necesarios para preparar 4 recetas completas.

# print("To determine the number of eggs necessary for this preparation.")
# number = int(input("Enter the number of recipes you are going to prepare:"))
# s=3
# a=(number*s)


# print(f"You need {a} eggs.")



# 2.	Pide al usuario la base y la altura de un rectángulo. Calcula e imprime el área (Área = base × altura).


# num1 = int(input(" Enter the base of the rectangle:   "))
# num2 = int(input("Enter the height of the rectangle:  "))
 
# a = num1*num2

# print(f" the area fo rectangle is: {a}")




# 3.	Una persona gana $15 por hora. Si trabaja 40 horas a la semana, calcula e imprime el salario bruto semanal total.{a}

# num1 = int(input(" Enter how many hours have you worked this week?:  "))

# hour_value = 15

# a = num1*hour_value

# print(f"The salary you earned this week is: {a}")




# -------------------------------------------------#
#           EJERCICIOS DE DIVISION                 #
# -------------------------------------------------#

# 1.	Calcula e imprime el resultado de la división flotante (con decimales) de 100 entre 12.

# print(100/12)

# 2.	Se tienen 75 chocolates para repartir equitativamente entre 9 niños. Usa la división entera (//) para determinar cuántos chocolates recibe exactamente cada niño.



# print(75//9)


# 3.	Un coche recorre 540 kilómetros en 6.5 horas. Calcula e imprime la velocidad promedio (distancia/tiempo).


# print(540//6.5)



# -------------------------------------------------#
#           MODULO                                 #
# -------------------------------------------------#


# Calcula e imprime el resto de la división de 45 entre 7.

# print(45%7)


# -------------------------------------------------#
#           CICLO  FOR                             #
# -------------------------------------------------#


# 1.	Iterar Rango: Usa un ciclo for con range() para imprimir los números pares del 2 al 20, ambos incluidos.

#-------------------------------------------------------------------------------------#
# for i in range(20):                                                                 #
# Corrección:                                                                         #
# 1. Inicio en 2.                                                                     #
# 2. Final en 21 (para incluir el 20, ya que range() excluye el límite superior).     #
# 3. Paso de 2 (para saltar de par en par).                                           #
#-------------------------------------------------------------------------------------#

# for i in range(2, 21, 2 ):
#     print(i)


# 2.	Iterar Lista: Dada la lista dias = ["lun", "mar", "mie", "jue", "vie"], usa un ciclo for para imprimir el mensaje: "Hoy es [día]" para cada elemento.


# num1 = int(input(" Enter a day of the week?:  "))

# days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

# counter = 1

# for day in days:
#     if num1 > 7:
    #  Compara el elemento individual (number), no la lista entera (numbers)
    # if number > 10:
        # Imprime el número que cumple la condición (opcional)
        # print(f"Encontrado: {number}") 
        
        #  Incrementa el contador
#         print("incorrect number, enter numbers from 1 - 7 ")
#         break
#     if counter == num1:
#         print(day)

#     counter = counter + 1




# 3.	Acumulador/Contador: Usa un ciclo for para iterar a través de la lista de números [12, 5, 8, 10, 3, 7] y cuenta e imprime cuántos de ellos son mayores que 10.
# 3.	Acumulador/Contador: Usa un ciclo for para iterar a través de la lista de números [12, 5, 8, 10, 3, 7] y cuenta e imprime cuántos de ellos son mayores que 10.




# numbers = [12, 5, 8, 10, 3, 7]
# # El contador debe empezar en 0
# counter = 0

# for number in numbers:
#     #  Compara el elemento individual (number), no la lista entera (numbers)
#     if number > 10:
#         # Imprime el número que cumple la condición (opcional)
#         print(f"Encontrado: {number}") 
        
#         #  Incrementa el contador
#         counter = counter + 1
        
        
# # Imprime el resultado final del contador fuera del ciclo
# print(f"\nTotal de números mayores a 10: {counter}")


# 4.	Iterar Cadena: Dada la palabra "programacion", usa un ciclo for para contar y luego imprimir cuántas veces aparece la letra 'o'.

# letters = ["programacion"]
# counter = 0

# # La palabra real a iterar está en el primer (y único) elemento de la lista.
# word_to_iterate = letters[0]

# for char in word_to_iterate:
#     if char == 'o':
#         counter += 1

# print(f"La letra 'o' aparece {counter} veces en '{word_to_iterate}'.")



# 5.	for con break: Itera sobre los números del 1 al 10. Imprime el número, pero detén (rompe) el ciclo tan pronto como encuentres el número 7.


# for numero in range(1, 11):
#     print(numero)
#     if numero == 7:
#         break


    # 4.	Iterar Cadena: Dada la palabra "programacion", usa un ciclo for para contar y luego imprimir cuántas veces aparece la letra 'o'.

# palabra = "promagramacion"
# print(len(palabra))

# -------------------------------------------------#
#           CICLO  IF ELSE                         #
# -------------------------------------------------#

# 1. Determinar Paridad: Escribe un programa que pida un número entero al usuario. Usa una sentencia if/else para determinar si el número es par o impar e imprime el resultado.
# number = int(input("Enter a number:  "))

# a=number%2

# if a==0:
#     print(" It is even")

# else:
#     print("It is not even")


# 2. Clasificación de Edad: Pide la edad al usuario. Usa sentencias if, elif y else para clasificar a la persona e imprimir si es "Menor de edad" (menor a 18), "Adulto" (entre 18 y 65) o "Adulto mayor" (mayor a 65).

age = int(input("Enter your age:   "))

if age<18:
    print("You are underage")
elif age>=18 and age<=65:
    print("Adult")
else:print("Senior")    
    





# 3. Verificar Múltiplos: Pide un número entero. Verifica e imprime si el número es divisible entre 5, si es divisible entre 3, o si no es divisible por ninguno de los dos.

# 4. Calificación con Letra: Pide la nota de un examen (un número entre 0 y 100). Asigna e imprime una calificación de letra ('A', 'B', 'C', 'D' o 'F') basada en los rangos estándar (A: 90-100, B: 80-89, etc.).

# 5. Lógica con Dos Variables: Define dos variables booleanas (tiene_llave y puerta_abierta). Escribe una condición que imprima "Puedes entrar" si se cumplen ciertas condiciones lógicas específicas, o "No puedes entrar" en caso contrario.







# -------------------------------------------------#
#           CICLO  WHILE                           #
# -------------------------------------------------#



# 1. Mostrar un menú al usuario y ejecutar diferentes acciones basadas en su elección, hasta que elija la opción de salir

# ejecutando = True # Bandera de control

# while ejecutando:
#     print("\n--- Menú de Opciones ---")
#     print("1. Saludar")
#     print("2. Mostrar Fecha")
#     print("3. Salir")

#     opcion = input("Elige una opción (1-3): ")

#     if opcion == '1':
#         print("¡Hola! Bienvenido al programa interactivo.")
#     elif opcion == '2':
#         # En un programa real aquí usarías librerías para obtener la fecha
#         print("Hoy es Jueves, 6 de noviembre de 2025.")
#     elif opcion == '3':
#         print("Saliendo del programa. ¡Hasta pronto!")
#         ejecutando = False # Cambia la bandera para terminar el bucle
#     else:
#         print("Opción no válida. Por favor, elige 1, 2 o 3.")








# Ejercicio 1: Conteo Descendente ⏳
# Objetivo: Imprime una cuenta regresiva que empiece en 10 y termine en 1.

# Ejercicio 2: Suma de Pares ➕
# Objetivo: Calcula e imprime la suma de todos los números pares que están entre 2 y 10 (incluyendo el 10).

# Ejercicio 3: Duplicador con Límite ⏫
# Objetivo: Comienza con el número 1. Duplica su valor en cada iteración e imprime el resultado. El ciclo debe detenerse tan pronto como el número supere el valor de 100.

# Ejercicio 4: Solicitud de Entrada Numérica 🔢
# Objetivo: Pídele al usuario que ingrese un número entero. Si la entrada no es un número válido o está vacía, el ciclo debe seguir pidiendo la entrada hasta que el usuario ingrese algo que pueda convertirse a entero.


