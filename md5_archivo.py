import hashlib

def calcular_md5_archivo(ruta):
    hash_md5 = hashlib.md5()
    with open(ruta, "rb") as file:
        bloque = file.read(4096)
        while bloque != b"": #b para que sea byte
            hash_md5.update(bloque)
            bloque = file.read(4096)
    return hash_md5.hexdigest()

##pp
ruta = r"ruta" #aqui poner la ruta
ruta2 = r"ruta2" #poner la otra ruta donde se dejo el archivo
print(calcular_md5_archivo(ruta))
print(calcular_md5_archivo(ruta2))