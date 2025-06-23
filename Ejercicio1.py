#Ingrese 5 notas, de 1.0 a 7.0, obtenga:
# nota mayor, nota menor, promedio
# Lanzar un excepcion cuando ocurra una nota fuera de rango

def fn_obtener_notas():
    notas = [] #Aqui se guardaran las notas
    for i in range(5):
        try:
            nota = float(input(f"Ingrese la nota {i+1} (de 1.0 a 7.0): "))
            #verificar si la nota esta en el rango permitido
            if not 1.0 <= nota <= 7.0:
                raise ValueError("La nota esta fuera del rango permitido (1.0 a 7.0)")
            notas.append(nota) #Si es valida se agrega a la lista
        except ValueError as error:
            print("Error: ", error)
        except Exception as error:
            print("Error: ", error)
            return
    return notas #retornamos las notas que son validas
#fn_obtener_notas()

def fn_calcular_resultado(notas):
    mayor = max(notas)
    menor = min(notas)
    promedio = sum(notas) / len(notas)
    print(f"\nNota mayor: {mayor}")
    print(f"Nota menor: {menor}")
    print(f"Promedio: {promedio: .2f}")
#fn_calcular_resultado()

#pp
notas = fn_obtener_notas()
if notas:
    fn_calcular_resultado(notas)