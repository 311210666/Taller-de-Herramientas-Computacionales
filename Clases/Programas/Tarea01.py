# -*- coding: utf-8 -*-
#Un automóvil arranca desde el reposo y acelera uniformemente en un tiempo de 5.21 segundos para una distancia de 110 m. Determinar la aceleración del coche.
#Necesitamos usar la fórmula d = vi*t + 0.5*a*t^2
#110 m = (0 m/s)*(5.21 s)+ 0.5*(a)*(5.21 s)2
#Como la velocidad inicial vale 0, entonces d = 0.5 * (t²)* a y queremos saber el valor de a
# a =  d / (t²) * 0.5
#Pongamos los valores

print 110/((5.21**2) * 0.5)

#Ahora definimos las variables

d = 110
t = 5.21
a = d / (t**2 * 0.5)
print a


