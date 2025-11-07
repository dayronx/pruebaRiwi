# Calculadora básica con +, -, *, /.

print("What operation do you want to execute?")
print("")
number = int(input("Select the number of the operation to start  "))
print("")
print("Addition        (1)")
print("Subtraction     (2)")
print("Multiplication  (3)")
print("Division        (4)")


if number==1:

    number1=int(input("Enter the numbers to add:  "))
    number2=int(input("Enter another number to add:  "))
    add=number1+number2
    print(f"The sum of these two numbers is: {add}")

if number ==2:

    number1=int(input("Enter the numbers to subtract:  "))
    number2=int(input("Enter another number to subtract:  "))
    Subtract=number1-number2
    print(f"The difference between these two numbers is: {Subtract}")

if number ==3:

    number1=int(input("Enter the two numbers to multiply:  "))
    number2=int(input("Enter the another number to multiply: "))
    multiply=number1*number2
    print(f"The product of these numbers is: {multiply}")

if number ==4:

    number1=int(input("Enter the two numbers to divide:  "))
    number2=int(input("Enter the another numbers to divide:  "))
    Divide=number1/number2
    print(f"The quotient of these two numbers is{Divide}")

else:

    print("This number is not on the start menu")    




