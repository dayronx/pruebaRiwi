contactos=[]


amaount= int(input("cuantos contacto desea agregar "))



while amaount !=0:

    nombre = input("dijite el nombre")
    telefono =int(input("dijite el numero de telefono"))
    cel= int(input("Dijite el numero del celular"))

    contacto = {
    "nombre" : nombre,
    "telefono" :telefono,
    "cel" : cel,
    }
    contactos.append(contacto)
    amaount -= 1


print(contactos)