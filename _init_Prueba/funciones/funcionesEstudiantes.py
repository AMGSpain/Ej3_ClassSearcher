import json

with open('estudiantesJSON') as file2:
    data2 = json.load(file2) 

def estudianteFunc():
    estudianteOpcion = int(input("¿Que deseas hacer? Pulsa: 1-Conocer Notas, 2-Cambiar Password, 3-Registrarse,  4-Salir : "))

    if estudianteOpcion == 1:
        conocerNotas()
    elif estudianteOpcion == 2:
        cambiarPasswordAlumno()
    elif estudianteOpcion == 3:
        estudianteRegistro()
    elif estudianteOpcion == 4:
        exit
    else:
        estudianteFunc()
        
def conocerNotas():
    emailInput = input("¿Cual es tu Email?: ")
    passwordInput = input("¿Cual es tu Password?: ")

    for alumno in data2['alumnos']:
        email = alumno['email']
        password = alumno['password']
        nombre = alumno['nombre']
        nota = alumno['nota']

        while emailInput in email:
            if passwordInput == password:
                print(f"Hola {nombre}, tu nota es de: {nota}")
                estudianteFunc()
                break
            else:
                print("Error en el PASSWORD")
                estudianteFunc()
                break
            
def cambiarPasswordAlumno():
    emailInput = input("¿Cual es tu EMAIL?: ")
    passwordInput = input("¿Cual es tu PASSWORD?: ")
    
    for alumno in data2['alumnos']:
        email = alumno['email']
        password = alumno['password']
        nombre = alumno['nombre']
        
        while emailInput in email:
            if passwordInput == password:
                newPassword = input(f"{nombre} elige un NUEVO PASSWORD: ")
                alumno['password'] = newPassword
                with open("estudiantesJSON", "w") as file_write:
                    json.dump(data2, file_write)
                
                print("Password cambiado.")
                estudianteFunc()
                break
            else:
                print("Error en el password.")
                estudianteFunc()
                break    
                    
def estudianteRegistro():
    email = input("¿Cual es tu email? ")
    password = input("Elige un password: ")
    nombre = input("¿Cual es tu nombre? ")
    apellidos = input("¿Cuales son tus apellidos? ")
    nota = 0.0
    asignatura = input("¿Que asignatura tienes? ")
    
    data2['alumnos'].append({
            'email' : email,
            'password' : password,
            'nombre' : nombre,
            'apellidos' : apellidos,
            'nota' : nota,
            'asignatura' : asignatura
        })
    with open("estudiantesJSON", "w") as file_write:
        json.dump(data2, file_write)
        
    print(f"Bienvenido {nombre} {apellidos}, te has guardado con el email de {email} .")
 