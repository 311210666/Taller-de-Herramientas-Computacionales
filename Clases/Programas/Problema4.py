#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def fib(n):
    
  
    if n == 1:
        return 0
    if n == 2:
        return 1

   
    
    else:
        a = fib (n-1)
        b= fib (n-2)
        c = b+a
        b = c
        a = b
        
        return b

