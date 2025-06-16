from cryptography.fernet import Fernet

#Generar clave
clave = Fernet.generate_key()
fernet = Fernet(clave)

#texto llano o plano
frase = input("Ingrese texto a cifrar: ")

#cifrar
cifrado = fernet.encrypt(frase.encode())
print("Cifrado: ", cifrado)

#descifrar
descifrado = fernet.decrypt(cifrado)
print("Descifrado: ", descifrado)

