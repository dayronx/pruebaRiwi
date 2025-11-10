# Tabla de multiplicar.


print("")
print("0")
print("1")
print("2")
print("3")
print("4")
print("5")
print("6")
print("7")
print("8")
print("9")
print("10")
print("")
number= int(input("Enter the number of the multiplication table you want:  "))


for i in range  (10):

    print(i)

print(f"\n--- Table of  {number} ---")

# 2. Usar el bucle for para iterar del 1 al 10
# range(1, 11) genera números desde 1 (inclusive) hasta 11 (exclusivo)
for i in range( 11):
    
 
    result = number * i
    
    

    # Imprimir la operación y el resultado
    print(f"{number} x {i} ={result}")