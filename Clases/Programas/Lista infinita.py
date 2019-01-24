def lista_infinita():
    i=1
    while True:
        yield i
        i+=1
for n in lista_infinita ():
    print n

