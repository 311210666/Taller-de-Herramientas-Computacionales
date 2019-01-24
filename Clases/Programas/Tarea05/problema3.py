#!usr/bin/python2.7
# -*- coding: utf-8 -*-

def listaC(Cmin, Cmax, n):
    gC = [] 
    dC = (Cmax - Cmin)/float (n-1)
    for i in range(n):
        C = Cmin + i*dC
        gC.append(C)
    return gC

def listaF(gC):
    gF=[]
    for C in gC:
        F =  (9.0/5)* C + 32
        gF.append (F)
    return gF

def Listas(gC,gF):
    for i in range (len(gC)):
        C = gC[i]
        F = gF[i]
        print "%5.1f %5.1f" % (C,F)

