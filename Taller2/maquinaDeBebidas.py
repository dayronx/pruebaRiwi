option=""

while option != '4':
        print("-"*50)
        print("-----MENU------")
        print("1::    Cafe $3")
        print("2::    Jugo $2")
        print("3::    Agua $1.5")
        print("-"*50)
        option = input("elija una opcion:    ")

        if option =='1': 
                precioCafe=3.0
                print("El precio del Cafe es de $3")
                dinero=float(input("Ingresa tu dinero:   "))
                print("-"*50)
                if precioCafe>dinero:
                        print("Dinero insuficente para hacer esta compra")
                elif dinero==precioCafe:
                        print("retira el producto")
                if precioCafe<dinero:
                        print("retira el producto")
                        cambio=dinero-precioCafe
                        print(f"Tu cambio es de: {cambio}")                


        elif option =='2':
                precioJugo=2.0
                print("El precio del Jugo es de $2")
                dinero=float(input("Ingresa tu dinero:  "))
                print("-"*50)
                if precioJugo>dinero:
                        print("Dinero insuficente para hacer esta compra")
                elif dinero==precioJugo:
                        print("retira el producto")
                if precioJugo<dinero:
                        print("retira el producto")
                        cambio=dinero-precioJugo
                        print(f"Tu cambio es de: {cambio}") 

        elif option == '3':
                precioAgua=1.5
                print("El precio del Jugo es de $2")
                dinero=float(input("Ingresa tu dinero:  "))
                print("-"*50)
                if precioAgua>dinero:
                        print("Dinero insuficente para hacer esta compra")
                elif dinero==precioAgua:
                        print("retira el producto")
                if precioAgua<dinero:
                        print("retira el producto")
                        cambio=dinero-precioAgua
                        print(f"Tu cambio es de: {cambio}") 

        else:
                print("digite un numero de la lista")                






