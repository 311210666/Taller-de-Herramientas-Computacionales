#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def suma(n):
    if n == 1:
        return 1
    else:
        return suma (n-1)+n
        
print suma(5)
        
