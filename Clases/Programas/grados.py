#!usr/bin/python2.7
# -*- coding: utf-8 -*-

def listaC(Cmin, Cmax, n):
    gradosC = [] #Es porque tenemos que hacer una lista vacía para referenciarla después "Ejemplo ciencia básica"
    # for (i=0; i<n; i++) en ptros lenguajes porque es una lista
    dC = (Cmax - Cmin)/float (n-1)
    for i in range(n):
        C = Cmin + i*dC #mínimo + c veces el incremento
        gradosC.append(C)
    return gradosC

def listaF(gradosC):
    gradosF=[]
    for C in gradosC:
        F =  (9.0/5)* C + 32
        gradosF.append (F)
    return gradosF

def mostrarListas(gradosC,gradosF):
    for i in range (len(gradosC)):
        C = gradosC[i]
        F = gradosF[i]
        print "%5.1f %5.1f" % (C,F)
    
#Las primeras dos funciones me regrasan un objeto, y la ultima solo imprime el valor. Lo importante es que regrese algo 


def mostrarListas1 (gradosC, gradosF):
    for C, F in zip (gradosC, gradosF):
        print '%5d %5.1f' % (C,F)
        

        
    
