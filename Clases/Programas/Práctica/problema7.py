#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''Dada la función
	0, si x < - ,

H= ½ + x/(2)+  1/(2)sen((x)/) , si -  x  .
           1, si x > 

Implemente la funcion H_eps(x, eps=0.01)
haga una función prueba_H_eps() para probar
la implementación  función anterior con valores
x < -,  x = -,  x=0,  x = , x > -'''

import math as m
x1 = 3
e1 = 0.01
def Heps (x1,e1):
    if x1 < -(e1):
        return 0
    else:
        if x1 > e1:
            return 1
        else:
            H= 1/2.0 + x1/(2 *e1) + 1/(2*e1 * m.sin (m.pi * x1 / e1))
            return H



def prueba_H_eps(x,e):
    if x < -(e):
        return 0
    else:
        if x > e:
            return 1
        else:
            if x==0:
                return 'x no puede ser 0'
            else:
                
                H= 1/2.0 + x/(2 * e) + 1/(2*e * m.sin (m.pi * x / e))
                return H



    

