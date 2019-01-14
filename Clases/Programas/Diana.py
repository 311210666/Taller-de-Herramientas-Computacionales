    
def Puntaje (x, y):
    if 5<= x<= 25 and 10 <= y <=30:
        return 10
    if (x <5 or x >=25) and 10 < y <30:
        return 5
    if 5< x <=25 and (y <10 or y>30):
        return 7
    else:
        return 3
    
    
    
