estudiantes  = {


    
}


nombre= input("ingresa nombre").strip().capitalize()
email= input("ingresa correo").strip().capitalize()
edad= input("ingresa edad").strip().capitalize()
direccion = input("ingresa direccion").strip().capitalize()
estudiantes= {
                "nombre": nombre,
                "Email" : email,
                "Edad"  : edad,
                "Direccion" : direccion,
            }


print(estudiantes)