import hashlib

def hash_md5(texto):
    #Convertir el texto a byte
    texto_bytes = texto.encode()
    #Creamos el hash (objeto)
    hashmd5 = hashlib.md5(texto_bytes)
    return hashmd5.hexdigest()

#pp
frase = input("Ingrese una frase: ")
elhash = hash_md5(frase)
print("La huella digital es: ", elhash)
