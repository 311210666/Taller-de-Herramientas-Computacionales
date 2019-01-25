#!usr/bin/python2.7
# -*- coding: utf-8 -*-

'''Calcular la suma del cuadrado de los primeros n enteros.
Comparar el resultado con la fórmula:
i=1ni² = ( n (n+1) (2n+1) )
/ 6.'''
#( n *(n+1)* (2*n+1) ) / 6
def sumcuad (n):
    if n ==1:
        return 1
    else:

        if n==2:
            return n**2 + (n-1)**2
        else:
            return n**2 + sumcuad (n-1)


    
