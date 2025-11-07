# 4. Mostrar resultados en consola:

#     Usa la función print() para mostrar un mensaje con:
#         Nombre del producto
#         Precio unitario
#         Cantidad
#         Costo total calculado
#     El formato del mensaje debe ser claro, por ejemplo: "Producto: Lápiz | Precio: 500 | Cantidad: 3 | Total: 1500"


name       =input("Enter a prodcut name :  ")
price      =2.58
quantity   =int(input("Enter a quantity  :"))
total_price=(quantity*price)




print(f"Product : {name} | Price Unitary : {price} | Quantity {quantity}| Total Price: {total_price}")
