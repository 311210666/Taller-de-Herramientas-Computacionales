#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
def prom(n): 
    L = []
    for i in range(n):
        a = input("Número")
        L.append(a)
        suma=0
        for i in L:
            suma += i
            b = float(suma)/n
    return b




