#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import problema5
from problema5 import spnn

n= input ("¿Del 1 al cuál quieres calcular la suma?\n")

print "La suma de los primeros %d naturales es %d" % (n, spnn (n))
