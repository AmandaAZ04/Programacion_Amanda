#with open("archivo.txt", "w", encoding = "utf-8") as archivo:
#    archivo.write("Esta es la primera línea del archivo\n")
#    archivo.write("Esta es la segunda línea\n")


#archivo = open("archivo.txt", "a", encoding = "utf-8")
#archivo.write("Otro mas contenido\n")
#archivo.write("Otro mas sin sentido\n")
#archivo.close()

#archivo = open("archivo.txt", "r", encoding = "utf-8")
#contenido = archivo.read()
#print("Contenido del archivo: \n", contenido )


archivo = open("archivo.txt", "r", encoding = "utf-8")
lineas = archivo.readlines()
numlin = len (lineas)
for i in range (0,numlin):
    lin = lineas[i].strip() #.strip salta las lineas
    print(i+1,"\t",lin)