
print("***************************")
print("*  CAJERO MULTIFUNCIONAL  *")
print("***************************")
print("")



option = ""
saldo=1000000
pin = {"pin" :"ABCD"}

while option != 5:

    print("¿QUE DESEA HACER?")
    
    print("1::  Ver saldo")
    print("2::  Retirar efectivo")
    print("3::  Depositar")
    print("4::  Cambio de PIN")
    print("5::  Salir")
    print("")
    print("")


    option = input("Choose an option (1-5): ")

    if    option =='1':

        print("-------------------------------")
        print(f"Su saldo es de:  {saldo}")
        print("-------------------------------")

    elif  option =='2':

        retiro=float(input("Digite la cantidad a retirar"))
        if retiro<=saldo:
                print(f"su retiro es de. {retiro} ")
                action=saldo-retiro
                print("-------------------------------")
                print(f"tu nuevo saldo es de: {action}")
                print("-------------------------------")
        else:
                print("Saldo insufieciente")        

    elif  option =='3':

        ingreso=float(input("¿Cuanto dinero va a depositar?"))
        action=saldo+ingreso
        print("-------------------------------")
        print(f"saldo actual: {action}")
        print("-------------------------------")

    elif  option =='4':
        pincambiado = input("Cambia tu pin: ")
        pin["pin"] = pincambiado
        print(pin["pin"],"Pin actualizado ")
        print("-------------------------------")
    elif  option =='5': 

        print("Saliendo de la operacion...")
        print("")
        print("")
        print("")


    else:
        print("Elije una opciuon correcta")    



