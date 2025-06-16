import bcrypt

palabra = input("Ingrse palabra o frase: ")

contrasena = palabra.encode("utf-8")
print("contrasena:", contrasena)
salero = bcrypt.gensalt()
hash_contrasena = bcrypt.hashpw(contrasena, salero)
print(hash_contrasena)

otravez = input("Ingrésela de nuevo: ")
otra_vez_b = otravez.encode("utf-8") # Contraseña en formato byte
print("Coincide: ", bcrypt.checkpw(otra_vez_b, hash_contrasena))

#contra = otravez.encode("utf-8")
#print("contrasena:", contra)
#hash_contra = bcrypt.hashpw(contra, bcrypt.gensalt())
#print(hash_contra)