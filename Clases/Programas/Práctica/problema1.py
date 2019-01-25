#!usr/bin/python2.7
# -*- coding: utf-8 -*-

'''Una forma rápida para convertir grados
Fahrenheit a Celsius es utilizando la
aproximación C(F-30)/2. Recuerde que la
fórmula para convertir Celsius a Farheneit
es F= 9/5C +32 Mostrar una tabla con cuatro
columnas en la que la primera columna sean
los grados Fahrenheit, la segunda los
grados Celsius y la tercera la diferencia
entre la fórmula exacta y la aproximación
a celsius'''

F = input ('¿Cuántos grados F quieres convertir?')

C = (F-32) * 5.0/9

Caprox = (F-30)/2

Dif = C - Caprox

L=[F, C, Caprox, Dif]






        
