#!usr/bin/python2.7
# -*- coding: utf-8 -*-
'''¿Cómo representaría la
malla '''


def rangef(a, b, n):  
    L = []
    c = a
    while c < b:
        L.append(c)
        c += n
    return L


def Malla():  
    m = []
    for i in rangef(-7, 7.5, 0.5):
        for j in rangef(-5, 5.5 ,0.5):
            m.append([j, i])
     
    return m



    
