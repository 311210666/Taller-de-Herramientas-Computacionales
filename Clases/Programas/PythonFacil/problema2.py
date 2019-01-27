#!usr/bin/python2.7
# -*- coding: utf-8 -*-

'''Programe una función que reciba una matriz de enteros y devuelva una
tupla con la lista o vector de la suma de cada fila y otro vector con la suma
de cada columna.'''

def sumatriz(m):
    l1 = []
    l2 = []
    s1 = 0
    s2 = 0 

    for fila in range(len(m)):
        for columna in range(len(m[fila])):
            s1 += m[fila][columna]
        l1.append(s1)
        s1 = 0

    for columna in range(len(m[0])):
        for fila in range(len(m)):
            s2 += m[fila][columna]
        l2.append(s2)
        s2 = 0
    return tuple ([l1, l2])

m= [[1,1],[1,1]]
print (sumatriz(m))

