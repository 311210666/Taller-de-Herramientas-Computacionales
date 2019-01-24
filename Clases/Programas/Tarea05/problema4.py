#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def fib(n):
    
    sfib =[]

    if n == 1:
        return 0
    if n == 2:
        return 1

   
    
    else:
        a = fib (n-1)
        b = fib (n-2)
        c = b+a
        b = c
        a = b
        
        return b

def fiblist (sfib):
    for i in range (len(sfib)):
        A = sfib[i]
        
        print "%5g" % (A)

def fiblist(n): 
    fl = [0, 1] 
    for i in range(2, n+1):
        fl.append(fl[-1] + fl[-2])
    return fl
