#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#suma de los primeros n naturales
def spnn (n): 
    L = [0,1] 
    for i in range(1, n):
        L.append(len(L))
        spnn=0
        for i in L:
            spnn += i
    return spnn
