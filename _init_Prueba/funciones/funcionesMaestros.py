import json
from re import A

with open('profesoresJSON') as file:
    data = json.load(file) 
    
with open('estudiantesJSON') as file2:
    data2 = json.load(file2) 

def maestroFunc():
    maestroOpcion = int(input("¿Que deseas hacer? Pulsa: 1-Poner o Cambiar Notas, 2-Cambiar Password, 3-Registrarse,  4-Salir : "))

    if maestroOpcion == 1:
        ponerNotas()
    elif maestroOpcion == 2:
        cambiarPasswordMaestro()
    elif maestroOpcion == 3: 
        maestroRegistro()  
    elif maestroOpcion == 4:
        exit
    else:
        maestroFunc()  
        
def ponerNotas():
    nombreInput = input("¿Cual es el Nombre del alumno que deseas buscar?: ")
    
    for alumno in data2['alumnos']:
        nombre = alumno['nombre']
        apellidos = alumno['apellidos']
        #nota = alumno['nota']
        
        if nombreInput in nombre:
           notaInput = float(input(f"Escribe la nota para {nombre} {apellidos}: ")) 
           alumno['nota'] = notaInput
           with open("estudiantesJSON", "w") as file_write:
                json.dump(data2, file_write)
           print(f"La nota final para {nombre} {apellidos} es de: {notaInput}")
           maestroFunc() 
           break
    else:
        print(f"Alumno no encontrado por el nombre: {nombreInput}")
        maestroFunc()
        
        
def cambiarPasswordMaestro():
    emailInput = input("¿Cual es tu EMAIL?: ")
    passwordInput = input("¿Cual es tu PASSWORD?: ")
    
    for profesor in data['profesores']:
        email = profesor['email']
        password = profesor['password']
        nombre = profesor['nombre']
        
        while emailInput in email:
            if passwordInput == password:
                newPassword = input(f"{nombre} elige un NUEVO PASSWORD: ")
                profesor['password'] = newPassword
                with open("profesoresJSON", "w") as file_write:
                    json.dump(data, file_write)

                print("Password cambiado.")
                maestroFunc()
                break
            else:
                print("Error en el password.")
                maestroFunc()
                break

def maestroRegistro():
    email = input("¿Cual es tu email? ")
    password = input("Elige un password: ")
    nombre = input("¿Cual es tu nombre? ")
    apellidos = input("¿Cuales son tus apellidos? ")
    edad = int(input("¿Que edad tienes? "))
    asignatura = input("¿Que asignatura impartes? ")
        
    data['profesores'].append({
            'email' : email,
            'password' : password,
            'nombre' : nombre,
            'apellidos' : apellidos,
            'edad' : edad,
            'asignatura' : asignatura
        })
        
    with open("profesoresJSON", "w") as file_write:
        json.dump(data, file_write)
        
    print(f"Bienvenido {nombre} {apellidos}, te has guardado con el email de {email} y eres profesor de la asignatura de {asignatura}")
            
    
    
        
        