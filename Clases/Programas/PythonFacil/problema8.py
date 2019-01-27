'''Determine el propósito del siguiente algoritmo.
a) Defina un buen nombre'''

def g(l):
    a=0

    for i in l:
        for j in l:
            if abs (i-j)>a:
                a=abs (i-j)
    return a
'''Hace la diferencia entre el número
más grade y más chico de la lista
Nombre: rangolista'''

