L= [[True, True, True, True],
    [False, False, False, True],
    [True, True, False, True]]

'''def resolver (L,e):
    n=len (L[0])
    m=len(L)
    x=e[0]  #e es la lista que contiene las cordenadas de conde quiero entrar
    y=e[1]
    if y== n-1:
        return e[0]+1, e[1]+1
    else:
        if L[x][y+1] == False:
            e = [x, y + 1] #y es la posicion en la que estoy 
            return resolver(L, e)
        else:
            if y == m-1:
                f = [x+1, y]
                return f[0]+1, f[1]+1
            else:
                if L[x+1][y] == False:
                    
                    return resolver (L,e)
                else:
                    print 'Ya no puede ir hacia abajo'
            
#esperamos 1,3 porque lo que nos regresa son índices.
r = resolver (L,[1,0]) '''      

#respuesta del profe

def resolver (L,e):
    n=len (L[0])
    m=len(L)
    x=e[0]  #e es la lista que contiene las cordenadas de conde quiero entrar
    y=e[1]
    if y== n-1 or x==m-1:
        return e[0]+1, e[1]+1
    else:
        if L[x] [y+1] == False:
            e = [x, y+1]
            return resolver (L,e)
        elif L[x+1][y] == False:
            e=[x+1,y]
            return resolver (L,e)
        else:
            print 'Ya no puede avanzar'
e=[0,1]
r = resolver (L,e)
import numpy as np
print (np.matrix(L))

            
