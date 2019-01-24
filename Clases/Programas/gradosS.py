import grados
from grados import *
L1 = listaC(-15,32,10)
L2 = listaF (L1)
mostrarListas(L1,L2)

a = input ("¿Cuál es el extremo izquierdo del intervalo?")
b = input ("¿Cuál es el extremo izquierdo del intervalo?")
n = input ("Cuántos subintervalos?")

L1 = listaC (a, b, n)
L2 = listaF (L1)
mostrarListas (L1, L2)

