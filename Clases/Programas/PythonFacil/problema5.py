#!usr/bin/python2.7
# -*- coding: utf-8 -*-


'''Diseñe y programe un algoritmo recursivo que encuentre la salida de un
laberinto, teniendo en cuenta que el laberinto se toma como entrada y que
es una matriz de valores True, False, (x,y), (a,b), donde True indica un
obstáculo; False, una celda por la que se puede caminar; (x,y), el punto
donde comienza a buscarse la salida y (a,b), la salida del laberinto.'''

L= [[True, True, True, True,True],
    [False, False, True, True,True],
    [True, False, True, True, True],
    [True, False, False,False,True],
    [True, True, True, False,True]]

def resolver (L,e):
    n=len (L[0])
    m=len(L)
    x=e[0]      y=e[1]
    if y== n-1 or x==m-1:
        return e[0]+1, e[1]+1
    else:
        if L[x] [y+1] == False:
            e = [x, y+1]
            return resolver (L,e)
        elif L[x+1][y] == False:
            e=[x+1,y]
            return resolver (L,e)
        else:
            print ('Ya no puede avanzar')
e=[0,1]
r = resolver (L,e)
print (r)
