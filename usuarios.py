import bcrypt
import pwinput
import pickle

ARCHIVO_USUARIOS = "usuarios.bin"

def fn_hashear_clave(clave):
    clave_byte = clave.encode()
    clave_hash = bcrypt.hashpw(clave_byte, bcrypt.gensalt())
    return clave_hash

def fn_crear_usuario(users):
    print("Crear usuario")
    cuenta = input("Ingrese nombre de usuario: ").strip()
    if cuenta in users:
        print("La cuenta ya existe !!")
    else:
        clave = pwinput.pwinput("Contraseña: ")
        clave2 = pwinput.pwinput("Repita contraseña: ")
        if clave == clave2:
            users[cuenta] = fn_hashear_clave(clave)
            print("Usuario creado !!")
        else:
            print("Las contraseñas son diferentes, cuenta no creada")

def fn_eliminar_usuario(users):
    print("Eliminar usuario")
    cuenta = input("Ingrese nombre de usuario: ").strip()
    if cuenta not in users:
        print(f"La cuenta {cuenta} NO existe !!")
    else:
        confirmacion = input(f"Está seguro de eliminar la cuenta {cuenta}? [si/no]: ").lower().strip()
        if confirmacion == "si":
            del users[cuenta]
            print(f"Usuario {cuenta} eliminado")
        else:
            print(f"La cuenta {cuenta} no se ha eliminado")

def fn_cambiar_clave(users):
    print("Cambiar contraseña")
    cuenta = input("Cuenta: ").strip()
    if cuenta in users:
        clave = pwinput.pwinput("Contraseña nueva: ")
        clave2 = pwinput.pwinput("Repita contraseña: ")
        if clave == clave2:
            users[cuenta] = fn_hashear_clave(clave)
            print("Contraseña cambiada !!")
        else:
            print("Las contraseñas son diferentes, no se ha cambiado.")
    else:
        print(f"La cuenta {cuenta} no existe.")

def fn_guardar_usuarios(users):
    with open(ARCHIVO_USUARIOS, "wb") as archivo:
        pickle.dump(users, archivo)
    print("Lista de usuarios actualizada.")

def fn_cargar_usuarios():
    try:
        with open(ARCHIVO_USUARIOS, "rb") as archivo:
            return pickle.load(archivo)
    except FileNotFoundError:
        return {}

#pp
usuarios = {}
usuarios = fn_cargar_usuarios()
if usuarios:
    print("Lista de usuarios cargada.")
else:
    print("No hay usuarios.")
salir = False
while not salir:
    print("***GESTION DE USUARIOS***")
    print("[1] Crear usuario")
    print("[2] Eliminar usuario")
    print("[3] Cambiar contraseña")
    print("[4] Listar usuarios")
    print("[5] Salir")
    op = input("Opcion: ")

    if op == "1":
        fn_crear_usuario(usuarios)
        fn_guardar_usuarios(usuarios)

    if op == "2":
        fn_eliminar_usuario(usuarios)
        fn_guardar_usuarios(usuarios)

    if op == "3":
        fn_cambiar_clave(usuarios)
        fn_guardar_usuarios(usuarios)

    if op == "4":
        print("Usuario registrados:", list(usuarios.keys()))

    if op == "5":
        fn_guardar_usuarios(usuarios)
        salir = True
print("¡Hasta luego!")