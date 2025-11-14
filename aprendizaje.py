

# de esta manera dse hace un diccionario

diccionario_carlos = {
                "nombre": "Carlos",
                "edad": 25,
                "carrera": "Ingeniería",
                "promedio": 8.9

}
# de esta manera almacenamos informacion en un diccionario

# nombre= input("ingresa nombre").strip().capitalize()
# edad= input("ingresa edad").strip().capitalize()
# promedio= input("ingresa el promedio").strip().capitalize()
# carrera = input("ingresa la carrera que cursa").strip().capitalize()
# estudiantes= {
#                 "nombre"      : nombre,
#                 "Edad"        : edad,
#                 "Carrera"     : carrera,
#                 "Promedio"    : promedio,

#             }





# # como mostrar infioamcion de un diccionario

# # ➡️ Extrayendo el valor 'Carlos'
nombre_del_estudiante = diccionario_carlos["nombre"]
print(f"El nombre es: {nombre_del_estudiante}")

# # ➡️ Extrayendo el valor '25'
edad_del_estudiante = diccionario_carlos["edad"]
print(f"La edad es: {edad_del_estudiante}")


print(f"la edad es: {edad_del_estudiante} y el nombre: {nombre_del_estudiante}")


# agreagdon informacion al diccionario 

# ➡️ Añadiendo la clave 'semestre' con el valor 5
diccionario_carlos["semestre"] = 5

semestre = diccionario_carlos["semestre"]
print(f" el semestrees: {semestre}")


print(f"la edad es: {edad_del_estudiante} y el nombre: {nombre_del_estudiante},el semestrees: {semestre}")





# no podemos gusradar mas objetos en la lista si quiero hacerlo debo crear una lista

# 1. Creamos una LISTA para guardar a todos los estudiantes
lista=[]




# --- 👨‍🎓 Información de Carlos --- ya esta arriba en el dic


# ➡️ Agregamos a Carlos a la lista
lista.append(diccionario_carlos)

# --- 👩‍🎓 Información de Ana ---
diccionario_ana = {

    "nombre"    : "Ana",
    "edad"      : 22,
    "carrera"   : "Literatura",
    "promedio"  : 9.5
}


# ➡️ Agregamos a Ana a la lista
lista.append(diccionario_ana)

# 3. Imprimir la estructura completa
print("--- Lista de Estudiantes Completa ---")
# Imprimimos la lista de diccionarios
print(lista) 

print("\n--- Impresión Detallada ---")
# Usamos un bucle para recorrer e imprimir cada persona
for diccionarios  in lista:
    print(f"Nombre: {diccionarios['nombre']}, Edad: {diccionarios['edad']}")


# ahora quiero sumar los promedios dos datos de diferentes diccionarios pero de la misma lista


# creamos una variable donde haremos la operacion
suma_de_promedios = 0


# # Recorremos la lista
for diccionarios in lista:
    # Extraemos el promedio de cada estudiante usando la clave "promedio"
    promedio_actual = diccionarios["promedio"] 
    
    # Lo sumamos al acumulador
    suma_de_promedios += promedio_actual 

# # Imprimimos el resultado
print(f"El promedio de Carlos es: {lista[0]['promedio']}")
print(f"El promedio de Ana es: {lista[1]['promedio']}")
print("-" * 30)
print(f"La suma total de los promedios es: {suma_de_promedios}")