nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'D'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge', 'JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12,
13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18,
74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64,
87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15,
39, 15, 74, 33, 57, 10, 11]

notas = set(notas_1 + notas_2)
print(notas)

estudiantes = nombres.replace("'", "").split(",")
dicc = {}
count = 0
for alumno in estudiantes:
    promedio = 0
    promedio = (notas_1[count] + notas_2[count])/2
    dicc[alumno] = promedio
    count+=1
print(dicc)
promedioGral = notas_1 + notas_2
promedioGral = sum(promedioGral)/len(promedioGral)
print(promedioGral)
notaMax = 0
alumnoMax = ""

for i in dicc:
    if dicc[i] > notaMax:
        notaMax = dicc[i]
        alumnoMax = i

notaMin = 1000
alumnoMin = ""
count = 0
for alumno in estudiantes:
    if notas_1[count] < notaMin:
        notaMin = notas_1[count]
        alumnoMin = alumno
    if notas_2[count] < notaMin:
        notaMin = notas_2[count]
        alumnoMin = alumno
    count+=1
print(f"Alumno max: {alumnoMax}, Nota: {notaMax}")
print(f"Alumno min: {alumnoMin}, Nota: {notaMin}")