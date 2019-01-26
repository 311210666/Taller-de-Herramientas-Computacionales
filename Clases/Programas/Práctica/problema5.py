#!usr/bin/python2.7
# -*- coding: utf-8 -*-
'''¿Cómo representaría la
malla '''

a=input ('numero mas chico')
b=input ('numero mas grande')
#f=input ('numero mas chico')
#a=input ('numero mas grande')

def rangef (a, b, n):  
    L = []
    c = a
    while c < b:
        L.append(c)
        c += n
    return L


def Malla():  
    m = []
    for i in rangef( -5,  5 , 0.5):
        for j in rangef(-7 , 7 ,0.5):
            m.append([j, i])
     
    return m


def Fun (x,y):
    n = Malla [x-1][y-1]

print (Fun (3,4))

print (Malla())

