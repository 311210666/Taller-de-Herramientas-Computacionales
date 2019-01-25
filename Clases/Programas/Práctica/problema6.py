#!usr/bin/python2.7
# -*- coding: utf-8 -*-
'''Implemente una función recursiva que calcule
n! = n * (n-1) * (n-2) * …* 2 * 1'''

def Factorial (n):
    if n == 1:
        return 1
    else:
        if n == 2:
            return n * (n-1)
        else:
            return n * Factorial (n-1) 
    

