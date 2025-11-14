# Escribe un programa que recorra del 1 al 100:

#     Si el número es múltiplo de 3 → imprime Fizz
#     Si es múltiplo de 5 → imprime Buzz
#     Si es múltiplo de ambos → FizzBuzz
#     En otro caso imprime el número.
for i in range (1, 101):
    
    if i %3 == 0  and i %5 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i) 
