#Sistema de gestion de inventario para una tienda
#autor: Manuel Sanchez

#import iec170funciones
from iec170funciones import *
import pwinput
import bcrypt

"""
version MAJOR.MINOR.PATCH
EJEMPLO v2.4.1

MAJOR: (version mayor): Se incrementa cuando se hacen cambios grandes (generalmente incomptaibles)
    con la version anterior.
MINOR: (version menor): Se incrementa cuando se agregan uevas funcionalidades al sistema, pero 
    sin romper la compatibilidad.
PATCH: (parche o revisión): Se incrementa, cuando se corrigen errores en el sistema, o mejoran 
    funcionalidades 

"""
#Historial 
#       15/04/2025 Inicio del desarrollo v1.0.0
#       22/04/2025 Agrega opción 5 Modificar Cantidad v1.1.0
#       22/04/2025 Mejora las funcionalidades de 3 y 4 al buscar con while v1.1.1
#       29/04/2025 Cambio de paradigma, inicio el trabajo con funciones v2.0.0
#       05/05/2025 Se reemplaza el buscar y mostrar producto por funciones y se 
#                  agregar control de keyboardInterrupt v2.0.1
#       03/06/2025 Se modulariza cada opcion del menu, v2.1.0
#       10/06/2025 Se crean funciones para administrar el inventario en archivos 
#                  texto y binario v3.0.0

def fn_cargar_usuarios():
    try:
        with open("usuarios.bin", "rb") as archivo:
            return pickle.load(archivo)
    except FileNotFoundError:
        return {}
    
def fn_clave_valida(clave_plana, clave_guardada):
    return bcrypt.checkpw(clave_plana.encode(), clave_guardada)

def fn_valida_usuario():
    users = fn_cargar_usuarios() #Carga de usuarios desde el archivo
    if not users:
        print("No hay usuarios, comuníquese con el administrador")
        return None
    
    cuenta = input("Usuario: ").strip() #Pide y valida cuenta
    if cuenta not in users:
        print(f"La cuenta {cuenta} no existe.")
        return None

    clave = pwinput.pwinput("Contraseña: ")  #Validando contraseña
    if fn_clave_valida(clave, users[cuenta]):
        print(f"Bienvenido {cuenta}")
        return cuenta
    else:
        print("Contraseña incorrecta.")
        return None

#PROGRAMA PRINCIPAL (PP)
# listas para administrar los productos
usuario = fn_valida_usuario()
if usuario:
    lnombre = []
    lprecio = []
    lstock = []
    try:
        version = "v3.0.0"
        # fn_cargar_inventario_txt(lnombre, lprecio, lstock)
        fn_cargar_inventario_bin(lnombre, lprecio, lstock)
        salir = False
        while not salir:
            print(f" *** Menú {version} ***")
            print("[1] Agrega producto")
            print("[2] Listar productos")
            print("[3] Buscar por nombre")
            print("[4] Eliminar producto")
            print("[5] Modificar cantidad")
            print("[6] Exportar Inventario")
            print("[7] Salir")
            op = input("Opcion: ")
            #****** Agrega producto 
            if (op == "1"):  
                fn_agregar_producto(lnombre, lprecio, lstock)
                fn_guardar_inventario_bin(lnombre, lprecio, lstock)
            #****** Listar producto 
            if (op == "2"):  
                fn_listar_producto(lnombre, lprecio, lstock)

            #****** Buscar por Nombre
            if (op == "3"):  
                fn_buscar_producto(lnombre, lprecio, lstock)

            #****** Eliminar por Nombre
            if (op == "4"):
                fn_eliminar_producto(lnombre, lprecio, lstock)
                fn_guardar_inventario_bin(lnombre, lprecio, lstock)
                
            #****** Modificar Cantidad
            if (op == "5"):
                fn_modificar_producto(lnombre, lprecio, lstock)
                fn_guardar_inventario_bin(lnombre, lprecio, lstock)

            if (op == "6"):
                fn_exportar_inventario_csv(lnombre, lprecio, lstock)

            if (op == "7"):
                salir = True
                # fn_guardar_inventario_txt(lnombre, lprecio, lstock)
                fn_guardar_inventario_bin(lnombre, lprecio, lstock)
                print("Hasta luego")

    except KeyboardInterrupt as error:
        print("\nUd. ha abandonado el programa por usar la combinacion Ctrl+C")
else:
    print("Acceso denegado.")
    print("Hasta luego.")