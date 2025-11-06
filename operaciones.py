
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




numbers = [12, 5, 8, 10, 3, 7]
# El contador debe empezar en 0
counter = 0

for number in numbers:
    #  Compara el elemento individual (number), no la lista entera (numbers)
    if number > 10:
        # Imprime el número que cumple la condición (opcional)
        print(f"Encontrado: {number}") 
        
        #  Incrementa el contador
        counter = counter + 1
        
        
# Imprime el resultado final del contador fuera del ciclo
print(f"\nTotal de números mayores a 10: {counter}")


# 4.	Iterar Cadena: Dada la palabra "programacion", usa un ciclo for para contar y luego imprimir cuántas veces aparece la letra 'o'.


letters = ["programacion"]




# 5.	for con break: Itera sobre los números del 1 al 10. Imprime el número, pero detén (rompe) el ciclo tan pronto como encuentres el número 7.
