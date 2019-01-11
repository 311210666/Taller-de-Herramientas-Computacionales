# -*- coding: utf-8 -*-
i = 62
r = 189876545.7654675432

# Print out numbers with quotes "" such that we see the
# width of the field
print '"%d"' % i       # minimum field
#Lo muestra en su forma mínima 
print '"%5d"' % i      # field of width 5 characters
#5 espacios antes
print '"%05d"' % i     # pad with zeros
#Pone 5 caracteres y lo rellena con ceros si el numero es más chico 
print '"%g"' % r       # r is big number so this is scientific notation
# Notación cientifica
print '"%G"' % r       # E in the exponent
#Exponencial
print '"%e"' % r       # compact scientific notation
#Notación cientifica compacta
print '"%E"' % r       # compact scientific notation
#Notación cientifica compacta
print '"%20.2E"' % r   # 2 decimals, field of width 20
#Da una línea de 20 caracteres y pone espacios si los numeros no son suficientes. Y lo pone con exponencial.
print '"%30g"' % r     # field of width 30 (right-adjusted)
#Lo ajusta a 30 caracteres, si faltan los rellena con espacios 
print '"%-30g"' % r    # left-adjust number
#Acomoda el número a la izquierda y lo pone en notación cientifica
print '"%-30.4g"' % r  # 3 decimals
#Lo ajusta a solo 3 decimales
print '%s' % i   # can convert i to string automatically
#Convierte el numero a cadena
print '%s' % r
#Muestra la cadena que se definio antes
# Use %% to print the percentage sign
print '%g %% of %.2f Euro is %.2f Euro' % \
      (5.1, 346, 5.1/100*346)
