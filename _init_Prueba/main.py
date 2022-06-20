from funciones import funcionesEstudiantes
from funciones import funcionesMaestros

estudiante = input("¿Eres Estudiante?: ")

if estudiante.lower() == "si":
    funcionesEstudiantes.estudianteFunc()
else:
    profesor = input("¿Eres Profesor?: ")

    if profesor.lower() == "si":
        funcionesMaestros.maestroFunc()
    else:
        print("Adios")