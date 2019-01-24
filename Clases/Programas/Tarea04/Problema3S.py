#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import Problema3
from Problema3 import CF
from Problema3 import FC

a = input ('Escribe CF para convertir de °C a °F o FC para °F a °C \n')

if a == CF:
    x= input ("¿Cuántos °C quieres convertir a °F? \n")
    print ("%.2f °C = %.2f °F" % (x,CF (x)))

    
if a == FC:
    x= input ("¿Cuántos °F quieres convertir a °C?\n")
    print ("%.2f °F = %.2f °C" % (x,FC (x)))



