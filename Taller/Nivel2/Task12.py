# Comparador de tres números: mayor y menor..


number1=(int(input("Enter a first number.  ")))
number2=(int(input("Enter a second number.  ")))
number3=(int(input("Enter a third number.  ")))



if number1>number2 and number1>number3:
     print(f"This number is the largest: {number1}" )
if number2>number1 and number2>number3:
     print(f"This number is the largest: {number2}" )
if number3>number1 and number3>number2:
     print(f"This number is the largest: {number3}" )          



