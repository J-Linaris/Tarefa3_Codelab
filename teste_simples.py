lista = [1,2,3,4,5,6,7]
def busca_binária(elemento,lista):
    """
    Por busca binária, encontra um elemento em uma lista ordenada e devolve seu índice.
    """
    imin = 0
    imax = len(lista)-1
    while imax-imin>1:
        imed = (imax+imin)//2
        if lista[imed]>elemento:
            imax = imed
        else:
            imin = imed
    
    if lista[imax]==elemento:
        return imax
    elif lista[imin]==elemento:
        return imin
    else:
        return -1

print(busca_binária(1,lista))