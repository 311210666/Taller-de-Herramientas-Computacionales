#!usr/bin/python2.7
# -*- coding: utf-8 -*-
'''Calcular la suma del cubo de los primeros n enteros.
Comparar el resultado con la fórmula:
i=1ni³ = (n(n+1)/2)^2.'''

import problema3
from problema3 import *

n= input('Dame un numero entero')
print 'La suma del cubo los primeros %d naturales es %d\n' % (n, sumcub (n))
