import bcrypt
import pwinput

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
#        clave_byte = clave.encode()
#        clave_hash = bcrypt.hashpw(clave_byte, bcrypt.gensalt())
        users[cuenta] = fn_hashear_clave(clave)
        print("Usuario creado !!")

def fn_eliminar_usuario(users):
    print("Eliminar usuario")
    cuenta = input("Ingrese nombre de usuario: ").strip()
    if cuenta not in users:
        print(f"La cuenta {cuenta} NO existe !!")
    else:
        del users[cuenta]
        print(f"Usuario {cuenta} eliminado")


#pp
usuarios = {"admin" : 123}
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

    if op == "2":
        fn_eliminar_usuario(usuarios)


    if op == "4":
        print("Usuario registrados:", list(usuarios.keys()))

    if op == "5":
        salir = True
print("¡Hasta luego!")