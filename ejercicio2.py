#El estudiante obtiene la nota de la asignatura con 3 items de evaluacion
#item 1: 3 notas cuyo promedio vale un 40% de la nota final
#item 2: 1 nota de un proyecto, vale el 30% de la nota final
#item 3: 1 nota de trabajo practico, vale 30% de la nota final
#solicite 5 notas, en el orden que se indican, calcule y muestre
#la nota promedio de las 3 primeras notas
#la nota final
#Lanzar una excepcion cuando ocurra una nota fuera de rango

def fn_obtener_notas():
    notas = [] #Aqui se guardaran las notas
    for i in range(5):
        try:
            nota = float(input(f"Ingrese la nota {i+1} (de 1.0 a 7.0): "))
            #verificar si la nota esta en el rango permitido
            if nota < 1.0 or nota > 7.0:
                raise ValueError("La nota esta fuera del rango permitido (1.0 a 7.0)")
            notas.append(nota) #Si es valida se agrega a la lista
        except ValueError as error:
            print("Error: ", error)
            return
    return notas #retornamos las notas que son validas
#fn_obtener_notas()

def fn_calcular_nota_final(notas):
    promedio_item1 = sum(notas[0:3]) / 3 #promedio de las 3 primeras notas
    nota_final = (promedio_item1 * 0.40) + (notas[3] * 0.30) + (notas[4] * 0.30) #nota final ponderada
    print(f"\nPromedio del item 1 (40%): {promedio_item1:.2f}")
    print(f"Nota proyecto (30%): {menor}")
    print(f"Promedio: {promedio: .2f}")
#fn_calcular_resultado()

#pp
notas = fn_obtener_notas()
if notas:
    fn_calcular_resultado(notas)