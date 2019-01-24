
gradosC=[-5 + i * 0.5 for i in range(12)]

gradosF = [(9/5.0) * C +32 for C in gradosC]

Lista = [-5 + i * 0.5 for i in range(12)], [(9/5.0) * C +32 for C in gradosC]

Tabla = [[gradosC, gradosF] for gradosC, gradosF in zip(gradosC, gradosF)]

print Tabla
 
#Se tienen  que identificar dos partes cuando hacemos listas, el esquema general y cómo se tiene que sustituir.

from pprint import pprint

pprint (Tabla)

for gradosC,gradosF in Tabla [gradosC.index(10):gradosC.index(35)]:
	print '%5.0f %5.1f' %(gradosC,gradosF)
