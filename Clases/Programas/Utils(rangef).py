def rangef (a, b, n):  
    L = []
    c = a
    while c < b:
        L.append(c)
        c += n
    return L
