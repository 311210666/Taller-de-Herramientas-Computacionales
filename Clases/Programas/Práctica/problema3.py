#!usr/bin/python2.7
# -*- coding: utf-8 -*-
'''Calcular la suma del cubo de los primeros n enteros.
Comparar el resultado con la fórmula:
i=1ni³ = (n(n+1)/2)^2.'''

def sumcub (n):
    if n ==1:
        return 1
    else:

        if n==2:
            return n**3 + (n-1)**3
        else:
            return n**3 + sumcub (n-1)


   

