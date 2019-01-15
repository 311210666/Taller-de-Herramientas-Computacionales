
#El programa que hicimos nosotros

def ulam (x):
    i=0
    print (x)
    while x>1:
        p = x / 2
    
        if x == 2*p:
            x = x/2
            i=i+1
            print (x)
        else:
            x = 3*x + 1
            i=i+1
            print (x)
    return ('se hizo %d veces' % (i))


print ulam (7)



#El ejemplo que hizo el profe con las correcciones
#Lo más conveniente era dividirlo

'''def ulam1 (x):
    #if (x/2)*2-x == 0: 
    if x%2 == 0:

        return x/2
    else:
        return 3*x + 1

def suc(x):
    i=0
    #while x>1:
    while x!=1:
        x=ulam1 (x)
        i=i+1
    return i

print suc (7)
print suc (26)'''


            




