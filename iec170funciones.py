import pickle

def fn_get_num_valido(mensaje):
    """
    funcion para validar el ingreso de un valor numérico.
    No termina hasta que el valor ingresado es válido
    """
    validos = ["0","1","2","3","4","5","6","7","8","9","-","."]
    malopos = False
    repite = True
    num = 0
    while repite:
        num = input( mensaje )
        l = len( num ) #obtener el largo
        malochar = False
        malog = False
        contg = 0
        contp = 0
        for i in range( l ):
            if not num[i] in validos:
                malochar = True
            if num[i] == "-":
                contg = contg+1
            if num[i] == ".":
                contp = contp+1
        malopos = contg == 1 and  num[0] != "-"
        malog = contg > 1
        malop = contp > 1
        if malochar or malog or malopos or malop:
            repite = True
            print("La entrada no es válida")
        else:
            repite = False
    numero = float(num)
    return(numero)
    #fn_get_valida_num

def fn_mostrar_producto(prod, precio, stock):
    """
    `uso`: muestra un producto del inventario;
    `entrada`: nombre, precio y cantidad del producto;
    `retorna`: nada;
    """
    print(f"Producto: {prod}") 
    print("Precio: %5.2f" % precio) 
    print(f"Stock: {stock}")
    print("=====================================")  
    #mostrar_producto()


def fn_buscar(lista, nombre):
    esta = False
    i = 0
    l = len (nombre)
    while i < l and not esta:
        if lista[i].upper() == nombre.upper():
            esta = True
        else:
            i = i + 1
    if esta:  #si lo encuentra "esta" vale True
        return i    #retornamos la posicion donde lo halló
    else:
        return -1    #retornamos -1 si no lo encuentra
    #buscar()

def fn_agregar_producto(lnom, lpre, lsto):
    nom = input("Nombre del producto: ")    
    lnom.append( nom ) 
    precio = fn_get_num_valido("Precio del producto: ") #float(input("Precio del producto: ") )
    lpre.append( precio ) 
    canti = fn_get_num_valido("Cantidad del producto: ") #int(input("Cantidad del producto: ") )
    lsto.append( int(canti)) 
    print(f"Se ha agregado {nom}, con el precio {precio} y el stock {canti}")

def fn_listar_producto(lnom, lpre, lsto):
    largo = len (lnom)
    for i in range(largo):
        fn_mostrar_producto(lnom[i], lpre[i], lsto[i])

def fn_buscar_producto(lnom, lpre, lsto):
    nom = input("Nombre del producto a buscar: ")    
    pos = fn_buscar(lnom, nom)
    if pos == -1:
        print(f"El producto {nom} no está en el inventario")
    else:
        fn_mostrar_producto(lnom[pos], lpre[pos], lsto[pos])

def fn_eliminar_producto(lnom, lpre, lsto):
    nom = input("Nombre del producto a Eliminar: ")    
    pos = fn_buscar(lnom, nom)
    if pos != -1: #indica que el producto si está
        fn_mostrar_producto(lnom[pos], lpre[pos], lsto[pos])
        resp = input("Seguro que desea eliminar [si/no]: ")
        if resp.upper() == "SI": # nos evitamos el si-Si-sI
            del lnom[pos]            # borramos la posicion donde hallamos el producto
            del lpre[pos]
            del lsto[pos]
            print(f"Producto {nom} eliminado!!.")
        else:
            print(f"Producto {nom} no se ha eliminado.")
    else:
        print(f"El producto {nom} no está en el inventario")

def fn_modificar_producto(lnom, lpre, lsto):
    nom = input("Nombre del producto a Modificar: ")   
    pos = fn_buscar(lnom,nom) 
    if pos == -1: # o sea, no está
        print(f"El producto {nom} no está en el inventario")
    else:    # si efectivamente esta
        fn_mostrar_producto(lnom[pos], lpre[pos],lsto[pos])
        resp = input("Seguro que desea modificar [si/no]: ")
        if resp.upper() == "SI": # nos evitamos el si-Si-sI
            cant = fn_get_num_valido("Ingrese nueva cantidad: ") #int(  input("Ingrese nueva cantidad: ") )
            lsto[pos] = int(cant)
            print(f"Stock de {nom} modificado!!.")
        else:
            print(f"Producto {nom} no se ha modificado.")

def fn_exportar_inventario_csv (lnom, lpre, lsto):
    with open("inventario.csv","w",encoding = "utf-8") as inventario:
        largo = len (lnom)
        for i in range(largo):
            inventario.write(lnom[i] + "; "+str( lpre[i]) + "; "+ str( lsto[i]) + "\n" )
        print("inventario Exportado en inventario.csv")

def fn_guardar_inventario_txt (lnom, lpre, lsto):
    with open("inventario.txt","w",encoding = "utf-8") as inventario:
        largo = len (lnom)
        for i in range(largo):
            inventario.write(lnom[i]+ "\n")
            inventario.write(str( lpre[i]) + "\n" )
            inventario.write(str( lsto[i]) + "\n" )
        print("inventario grabado en inventario.txt")

def fn_cargar_inventario_txt (lnom, lpre, lsto):
    try:
        with open("inventario.txt", "r", encoding="utf-8") as inventario:
            lineas = inventario.readlines()
            largo = len ( lineas ) #cuento el total de líneas
            for  i in range (0, largo, 3 ): #cada producto son 3 líneas
                nom = lineas[i].strip()
                pre = float(lineas[i+1].strip())
                sto = int(lineas[i+2].strip())
                lnom.append( nom )
                lpre.append( pre )
                lsto.append( sto )
        print("Inventario cargado exitosamente.")
    except FileNotFoundError:
        print("No se encontró el inventario, usando por defecto")
        # lnom = ["Plumon", "Borrador", "Pizarra"]
        # lpre = [1280.0, 3500.0, 13500.0]
        # lsto = [20,8, 10]
    except Exception as err:
        print("Error al cargar el inventario:", err)

def fn_guardar_inventario_bin (lnom, lpre, lsto):
    with open("inventario.dat","wb") as inventario:
        pickle.dump((lnom, lpre, lsto), inventario)
    print("inventario grabado en inventario.dat")

def fn_cargar_inventario_bin(lnom, lpre, lsto):
    try:
        with open("inventario.dat","rb") as inventario:
            datos = pickle.load(inventario)
            lnom.extend(datos[0])
            lpre.extend(datos[1])
            lsto.extend(datos[2])
        print("Inventario cargado exitosamente.")
    except FileNotFoundError:
        print("No se encontró el inventario, inventario vacio")
    except Exception as error:
        print("Oops!!, algo salió mal, error:", error)