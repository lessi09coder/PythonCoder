import json

#carga de datos de usuarios con permanencia:
def cargar_usuarios():
    try:
        with open("usuarios.txt", "r") as file:
            usuarios = json.load(file)
    except FileNotFoundError:
        usuarios = {}
    return usuarios

def guardar_usuarios(usuarios):
    with open("usuarios.txt", "w") as file:
        json.dump(usuarios, file)

#registro de usuarios:
def registrar_usuario():
    usuarios = cargar_usuarios()

    while True:
        nombre_usuario = input("Ingrese un nombre de usuario: ")
        if nombre_usuario in usuarios:
            print("El nombre de usuario ya está en uso. Intente con otro.")
        else:
            break

    contrasena = input("Ingrese una contraseña: ")
    usuarios[nombre_usuario] = contrasena
    guardar_usuarios(usuarios)
    print("¡Registro exitoso!")

#Login de usuarios
def iniciar_sesion():
    usuarios = cargar_usuarios()

    intentos = 3

    while intentos > 0:
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        if nombre_usuario in usuarios and usuarios[nombre_usuario] == contrasena:
            print("Inicio de sesión exitoso. ¡Bienvenido, {}!".format(nombre_usuario))
            break
        else:
            intentos -= 1
            print("Nombre de usuario o contraseña incorrectos. Intentos restantes: {}".format(intentos))

    if intentos == 0:
        print("Se agotaron los intentos. Cierre del programa.")

def leer_informacion():
    try:
        with open("usuarios.txt", "r") as file:
            usuarios = json.load(file)
            print(usuarios)
    except FileNotFoundError:
        usuarios = {}
    return usuarios

if __name__ == "__main__":
    print("1. Registrar usuario")
    print("2. Iniciar sesion")
    print("3. Ver usuarios")

    opcion = input("Seleccione una opcion (1 , 2 o 3): ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        leer_informacion()
    else:
        print("Opción no válida. Por favor, seleccione 1 , 2 o 3.")
