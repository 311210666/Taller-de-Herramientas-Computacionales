#!usr/bin/python2.7
# -*- coding: utf-8 -*-

'''Programe una función que dado un número x devuelva una lista infinita con
todos los múltiplos de x.'''

def lista_infinita():
    i=x
    while True:
        yield i
        i += x
for x in lista_infinita ():
    print (x)
