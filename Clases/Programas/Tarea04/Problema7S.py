#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#Problema: Calcular a partir de 10 datos el mayor, el menor y el promedio.

import Problema7
from Problema7 import mayor
from Problema7 import menor
from Problema7 import prom

a,b,c,d,e,f,g,h,i,j = input ("Ingresa 10 números separados por coma\n")
print "El mayor es %g, el menor es %g, el promedio es %.2f" % (mayor (a,b,c,d,e,f,g,h,i,j), menor (a,b,c,d,e,f,g,h,i,j), prom (a,b,c,d,e,f,g,h,i,j))
