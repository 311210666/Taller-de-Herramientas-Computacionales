# -*- coding: utf-8 -*-
v0 = 34
g = 9.81
t = 4.3
y = v0*t - 1.0/2*g*t**2
print 'La posición de la pelota en el t=%g es %.2f' % (t,y)
def posicion (t, v0):
    y = v0*t - 1.0/2*g*t**2
    return (y) 
