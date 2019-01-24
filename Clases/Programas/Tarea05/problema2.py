#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

    
import math

def t (h):
    L = [34,9.81,h]
    t1= ((-L[0]) + math.sqrt(L[0]**2-2*L[1]*(h)))/(-L[1])
    L.append(t1)
    t2= ((-L[0]) - math.sqrt(L[0]**2-2*L[1]*(h)))/(-L[1])
    L.append(t2)
    
    
    return t1,t2
