from animal import Animal
from acuatico import animalAcuatico
from aereo import animalAereo
from terrestre import animalTerrestre
from corral import corral
from empleados import Empleado
from granja import Granja

granja=Granja("Mi Gente","Grande",2,3)
corral1=corral("A1")
granja._corrales.append(corral)
while True:
    print("MENU:")
    print("1. Ingresar un animal")
    print("2. Registrar un empleado")
    print("3. Gestionar un corral")
    print("4. Salir")

    opc = input("Selecciona el número de la acción a realizar: ")

    match opc:
        case "1":
            print("Ingresando un animal...")
        case "2": 
            print("Registrando un empleado...")
        case "3":
            print("Gestionando el corral...")
        case "4":
            print("Saliendo del programa.")
            break
        case _:
            print("Opción inválida.")
