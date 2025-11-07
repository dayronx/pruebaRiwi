

# def tiene_documento(respuesta):
#     """Convierte la respuesta del usuario ('si'/'no') a True/False."""
   
#     return respuesta.lower() == 'si'


# edad = int(input("Ingrese su edad: "))
# respuesta_doc = input("¿Tiene documento de identidad? (Escriba 'si' o 'no'): ")


# es_mayor = (edad >= 18)
# tiene_doc_valido = tiene_documento(respuesta_doc) 


# puede_entrar = es_mayor and tiene_doc_valido

# mensaje_final = "Puede Entrar." if puede_entrar else "No Puede Entrar."


# print("\n" + mensaje_final)







CORREO_MAESTRO = "notengo@notengo"
CONTRASENA_MAESTRA = "123456789"


correo_ingresado_test1 = "admin@ejemplo.com" 
contrasena_ingresada_test1 = "Secreta123"     
correo_ingresado_test2 = "admin@ejemplo.com"  
contrasena_ingresada_test2 = "Incorrecta"     



resultado_test1 = (correo_ingresado_test1 == CORREO_MAESTRO) and \
                  (contrasena_ingresada_test1 == CONTRASENA_MAESTRA)
print(f"Resultado del Intento 1 (Correcto): {resultado_test1}")


resultado_test2 = (correo_ingresado_test2 == CORREO_MAESTRO) and \
                  (contrasena_ingresada_test2 == CONTRASENA_MAESTRA)
print(f"Resultado del Intento 2 (Incorrecto): {resultado_test2}")





# # Lista original
# numeros = [1, 2, 3, 4, 5]

# # Imprimir la lista al revés
# print(numeros[::-1])





# 🔢 Escribe un programa que imprima los números del 1 al 10 usando un bucle for.

# for i in range( 10+1):

#      print (i)


# ➕ Muestra la suma de los números del 1 al 100 usando un bucle for.

# suma =0

# for i in range (1, 100+1):
#       suma +=i
#       print(i)



# 🧮 Escribe un programa que imprima la tabla de multiplicar del 5.

# for i in range (5):
#     mul*=i
#     print(i)



# calculadora de edades 

# año_nacimiento = int(input("Ingrese su año de nacimiento: "))
# edad = 2025 - año_nacimiento
# print(f"Su edad es {edad}")



user = {

    "nombre"      :   "Dayron"                   ,
    "edad"        :    "29"                      ,
    "Correo"      :   "notengo@notengo"          ,
    "celular"     :    "3022220202"              ,
    "direccion"   :     "alOtroLadoDelParque"    ,

}
print(user["direccion"])
print(type(user["direccion"]))



lang = ["mango ","coco","pera","manzana","piña"]
print(lang[3])
print(type((lang[3])))
print(type(user))

