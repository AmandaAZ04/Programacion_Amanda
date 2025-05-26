lista_estudiantes = [
    ['Armando Casas',[['Biología',[4.5,5.6,6.7,7.0]],['Física',[4.5,5.6,6.7,7.0]],['Química',[4.5,5.6,6.7,7.0]]]],
    ['Aquiles Baeza',[['Biología',[5.6,6.5,5.0,5.9]],['Física',[5.6,6.5,5.0,5.9]],['Química',[5.6,6.5,5.0,5.9]]]], 
    ['Delfín Quispe',[['Biología',[4.5,3.9,4.7,4.0]],['Física',[4.5,3.9,4.7,4.0]],['Química',[4.5,3.9,4.7,4.0]]]],
    ['Wendy Sulca',[['Biología',[4.5,5.0,4.8,5.1]],['Física',[4.5,5.0,4.8,5.1]],['Química',[4.5,5.0,4.8,5.1]]]],
    ['Dolores de Cabeza',[['Biología',[5.6,4.7,6.2,6.4]],['Física',[5.6,4.7,6.2,6.4]],['Química',[5.6,4.7,6.2,6.4]]]]
]

suma = 0
for estudiante in lista_estudiantes:
    print()
    print(f'Nombre: {estudiante[0]}')
    for asignatura in estudiante[1]:
        print(f'Asignatura: {asignatura[0]}')
        for nota in asignatura[1]:
            suma = suma + nota
        print(f'Notas: {asignatura[1]}, Promedio: {suma/len(asignatura[1])}')
        suma = 0