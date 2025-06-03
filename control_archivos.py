#with open("archivo.txt", "w", encoding = "utf-8") as archivo:
#    archivo.write("Esta es la primera línea del archivo\n")
#    archivo.write("Esta es la segunda línea\n")


archivo = open("archivo.txt", "a", encoding = "utf-8")
archivo.write("Otro mas contenido\n")
archivo.write("Otro mas sin sentido\n")
archivo.close()