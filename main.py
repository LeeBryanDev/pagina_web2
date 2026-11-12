
def menu():
    # Introducción
    print("========== Menu ==========")
    print("1 . Registrar nuevo usuario")
    print("2. Iniciar sesion")
    print("3 . Salir")
    # Fin de la Introducción

def registrar_nuevos_usuarios(): # Función de registro 
    nombre = input("Introduce un nombre de usuario: ")
    contra = input("Introduce una contraseña: ")
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{nombre},{contra}\n") # Guarda el user + contraseña en un archivo de texto ("usuarios.txt")

def iniciar_sesion(): # Función de Inicio de Sesión
    with open("usuarios.txt","r") as archivo:
        lineas = archivo.readlines() # Extrae las lineas del archivo ("usuarios.txt")

    
    nombre = input("Introduce un nombre de usuario: ")
    contra = input("Introduce una contraseña: ")
    busqueda = f"{nombre},{contra}\n" # Pide al usuario que ingrese los datos de inicio de sesión y los guarda en una variable que se pueda relacionar con las lineas que extrae el readLines

    
    for linea in lineas:
        if busqueda == linea: # Si lo escrito por el usuario es igual a lo guardado lo da como válido y permitte la entrada del mismo dándole la bienvenida, si no, le comenta que no coincidieron los datos
            print("====================")
            print("Bienvenido")
            print("====================")
        else:
            print("El nombre o la contraseña son incorrectos")


    



def main():
    activo = True
    while activo:
        menu()

        opcion = int(input("Introduzca una opcion: "))
        match opcion:
            case 1: # Registro de nuevos users
                registrar_nuevos_usuarios()
            case 2: # Inicio de Sesión (Viejos users ya guardados)
                iniciar_sesion()
            case 3: # Salir
                print("Saliendo...")
                activo = False



main() # Fin del mejor