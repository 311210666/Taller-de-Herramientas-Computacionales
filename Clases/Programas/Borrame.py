import problema1
from problema1 import mcd
n = []
n1= input("Introduce el primer número: ")
n2 =input("Introduce el segundo número: ")
n.append(n1)
n.append(n2)
 
print "El máximo común divisor de %d y %d es %d" % (n[0],n[1], mcd(n1,n2))



