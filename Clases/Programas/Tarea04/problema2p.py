#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import math
def t(h):

    v0 = 34
    g = 9.81
    t1= ((-v0) + math.sqrt(v0**2-2*g*(h)))/(-g)
    t2= ((-v0) - math.sqrt(v0**2-2*g*(h)))/(-g) 
    return t1, t2
    
