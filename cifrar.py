import bcrypt

palabra = input("Ingrse palabra o frase: ")

contrasena = palabra.encode("utf-8")
print("contrasena:", contrasena)
hash_contrasena = bcrypt.hashpw(contrasena, bcrypt.gensalt())
print(hash_contrasena)
