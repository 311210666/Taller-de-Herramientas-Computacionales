# -*- coding: utf-8 -*-
A= '\n____________________'
def fib (n):
    """Calcula el nsimo trmino de la suc
de fib con n natural
"""
    if n>2:
        return fib (n-1)+fib(n-2)
    else:
        return 1

fib(1)
fib(2)
fib(5)
fib(10)

print A
def suma(n):
    if n == 1:
        return 1
    else:
        return suma (n-1)+n
        
print suma(5)

print A


L=[1,2,3,4,5]

#Como lo hice yo

def printr (L):
    if len (L)==1:
        print L[0]
    else:
        print L[0], L[1:]
    
printr (L)
print A

#Las dos opciones que nos dio el profe

def printr1 (L):
    if L:
        print L[0], #La coma omite el salto de linea
        printr1 (L[1:])

printr1 (L)



print A

def printr2 (L):
    if len(L)>1:
        print L[0],
        printr2 (L[1:])
    else:
        print (L[0])
printr2 (L)


def mifuncion(n):
    sum = n + 1
    print sum
    return sum

sum = mifuncion (2)+1

print A

def yfunc(t,v0):
    g = 9.81
    return v0*t-0.5*g*t**2


    
