def ngramas_comum(tokens1,tokens2,TAM_NGRAMA):
    M=[]
    controle = True
    for i in range(len(tokens1)-TAM_NGRAMA+1):
        for j in range(len(tokens2)-TAM_NGRAMA +1):
            if controle and tokens1[i:i+TAM_NGRAMA]==tokens2[j:j+TAM_NGRAMA]:
                print("entrou")
                M.append(tokens1[i:i+TAM_NGRAMA])
                controle = False
        controle = True
    return M

def cria_chaves(M):
    """
    Dada uma matriz M com os ngramas que aparecem em ambos os arquivos, devolve uma lista de chaves.
    """
    
    L=[]
    for ngrama in M:
        
        L.append("".join(ngrama))
    L.sort()
    return L

def histograma(chaves,tokens,TAM_NGRAMA):
    """
    Dadas uma lista de chaves e outra de tokens, devolve um histograma com as ocorrências de cada chave no arquivo.
    """
    
    #Primeiro, vamos obter uma lista de ngramas a partir dos tokens.
    L=[]
    i=0
    while i<=len(tokens)-TAM_NGRAMA:
        L.append("".join(tokens[i:i+TAM_NGRAMA]))
        i+=1
    L.sort()
    #Para facilitar a monstagem do histograma, sabemos que deve ter o mesmo número de elementos da lista de chaves,
    #Logo, inicializemos-o como uma simples cópia da lista de chaves e mudaremos todos os valores para 0
    H=chaves.copy()
    for i in range(len(H)):
        H[i] = 0
    #Agora, para cada chave, vamos registrar suas ocorrências nessa lista de ngramas.
    for i in range(len(L)):
        busca = busca_binária(L[i],chaves)
        if busca !=-1:
            H[busca] += 1
    return H

"""
Pelo que eu entendi, devo, depois de converter essa lista de tokens para uma lista de ngramas,
ver quantas vezes os meus ngramas de L correspondem a uma chave. Assim, para acessar o índice
que devo incrementar no histograma, devo fazer uma busca binária na lista de chaves até achar
a chave corresponde ao meu ngrama considerado da vez. Se eu realmente achar, a função da busca binária
irá me retornar um índice. Assim, eu posso incrementar 1 no índice encontrado, visto que meu ngrama
realmente corresponde a uma chave, logo, a chave apareceu uma vez.

Exemplo: L = ["abc","bcd","abc"] chaves = ["abc","def"] H=[0,0] 
PARA:
L[0] ---> busca binária devolve 0 (pois aparece no indice 0 de chaves) ----> H[0]+=1
L[1] ---> busca binária devolve -1, logo, não pertence à lista, ou seja, não faço nada.
L[2] ---> busca binária devolve 0 (pois aparece no índice 0 de chaves) ----> H[0]+=1
portanto, no fim, terei:
H = [2,0].

"""
        
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
    #Por conveção, se a busca retornar -1, então o elemento não pertenceà lista.
    else:
        return -1

    

def ngramas(tokens1,tokens2,TAM_NGRAMA=5):
    """
    Dadas duas listas léxicas devolve a correlação entre dois arquivos por N-gramas.
    """
    chaves = cria_chaves(ngramas_comum(tokens1,tokens2,TAM_NGRAMA))
    return print(chaves)
    
    
    #Construção dos histogramas
L=["var","5","=","var","fun","var"]
M=["var","5","=","var","fun","var"]
var = ngramas_comum(L,M,TAM_NGRAMA=5)
print(ngramas_comum(L,M,TAM_NGRAMA=5))
ngramas(L,M)