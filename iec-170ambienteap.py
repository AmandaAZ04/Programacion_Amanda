#Sistema de gestion de inventario para una tienda
#autor: Manuel Sanchez

#import iec170funciones
from iec170funciones import *

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
#       03/06/2025 Se modulariza cada opcion del menu v2.1.0

def fn_guardar_inventario(lnom,lpre,lsto):
    with open("Inventario.txt", "w", encoding = "utf-8") as inventario:
        largo = len(lnom)
        for i in range(largo):
            inventario.write(lnom[i] + "\n")
            inventario.write(str(lpre[i]) + "\n")
            inventario.write(str(lsto[i]) + "\n")
        print("Inventario grabado en inventario.txt")

def fn_cargar_inventario(lnom,lpre,lsto):
    try:
        with open("inventario.txt", "r", encoding = "utf-8") as inventario:
            lineas = inventario.readlines()
            largo = len(lineas) #Con esto cuento el total de lineas
            for i in range(0, largo, 3): #Cada producto son 3 lineas
                nom = lineas[i].strip()
                pre = float(lineas[i+1].strip())
                sto = int(lineas[i+2].strip())
                lnom.append(nom)
                lpre.append(pre)
                lsto.append(sto)
        print("Inventario cargado exitosamente.")
    except FileNotFoundError:
        print("No se encontró el inventario, usado por defecto.")
#        lnom = ["Plumon", "Borrador", "Pizarra"]
#        lpre = [1280.0, 3500.0, 13500.0]
#        lsto = [20, 8, 10]
    except Exception as error:
        print("Error al cargar el inventario:", error)



#PROGRAMA PRINCIPAL (PP)
# listas para administrar los productos
lnombre = []
lprecio = []
lstock = []

try:
    version = "v2.1.0"
    fn_cargar_inventario(lnombre, lprecio, lstock)
    salir = False
    while not salir:
        print(f" *** Menú {version} ***")
        print("[1] Agrega producto")
        print("[2] Listar productos")
        print("[3] Buscar por nombre")
        print("[4] Eliminar producto")
        print("[5] Modificar cantidad")
        print("[6] Salir")
        op = input("Opcion: ")
        #****** Agrega producto 
        if (op == "1"):  
            fn_agregar_producto(lnombre,lprecio,lstock)

        #****** Listar producto 
        if (op == "2"):  
            fn_listar_producto(lnombre,lprecio,lstock)

        #****** Buscar por Nombre
        if (op == "3"):  
            fn_buscar_producto(lnombre,lprecio,lstock)

        #****** Eliminar por Nombre
        if (op == "4"):
            fn_eliminar_producto(lnombre,lprecio,lstock)

        #****** Modificar Cantidad
        if (op == "5"):
            fn_modificar_producto(lnombre,lprecio,lstock)

        #Salir del programa
        if (op == "6"):
            salir = True
            fn_guardar_inventario(lnombre,lprecio,lstock)
            print("Hasta luego")

except KeyboardInterrupt as error:
    print("\nUd. ha abandonado el programa por usar la combinacion Ctrl+C")