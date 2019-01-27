#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''Programe una función que determine si un número entero suministrado
como argumento es primo.'''



def primo (n):
    if n<=2:
        return 'es primo'
    else:
        for i in range (2,n):
            if n%i == 0:
                return 'no es primo'
            else:
                return 'es primo'

