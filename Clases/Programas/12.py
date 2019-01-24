# -*- coding: utf-8 -*-

alumnos=[]
alumnos.append([9,8,10,9])
alumnos.append([9])
alumnos.append([6,9,10,8,9,10,10,9])


'''for i in range (len(alumnos)): #Para recorrer una lista por índices
    for j in range (len(alumnos[i])):
                    calificacion = alumnos[i][j]
                    print '%4d' % calificacion, #La coma omite el salto de linea 
                    
    print'''

for alumno in alumnos:
    for calificacion in alumno:
        print '%4d' % calificacion,
    print



  
    




