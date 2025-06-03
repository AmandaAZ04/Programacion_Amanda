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

def fn_agregar_producto(lnom,lpre,lsto):
    nom = input("Nombre del producto: ")    
    lnom.append( nom ) 
    precio = fn_get_num_valido("Precio del producto: ") #float(input("Precio del producto: ") )
    lpre.append( precio ) 
    canti = fn_get_num_valido("Cantidad del producto: ") #int(input("Cantidad del producto: ") )
    lsto.append( int(canti)) 
    print(f"Se ha agregado {nom}, con el precio {precio} y el stock {canti}")
    #fn_agregar_producto()

def fn_listar_producto(lnom,lpre,lsto):
    largo = len (lnom)
    for i in range(largo):
        fn_mostrar_producto(lnom[i], lpre[i], lsto[i])
    #fn_listar_producto()

def fn_buscar_producto(lnom,lpre,lsto):
    nom = input("Nombre del producto a buscar: ")    
    pos = fn_buscar(lnom, nom)
    if pos == -1:
        print(f"El producto {nom} no está en el inventario")
    else:
        fn_mostrar_producto(lnom[pos], lpre[pos], lsto[pos])
    #fn_buscar_producto()

def fn_eliminar_producto(lnom,lpre,lsto):
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
    #fn_eliminar_producto()

def fn_modificar_producto(lnom,lpre,lsto):
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
    #fn_modificar_producto()