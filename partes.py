import sys
from écomentáriooustring import écomentáriooustring
def tem(str,caractere):
    '''
    Devolve true se o caractere informado estiver presente
    (No caaso, será usado apenas para verificar se # e """ estão no texto)
    ''' 
    
    presente=False
    if len(caractere)==1:
        for i in range(len(str)):
            presente=presente or caractere==str[i]
    elif len(caractere)==3:
        if len(str)>=3:
            for i in range(len(str)-2):
                presente = presente or str[i:i+3]==caractere
    return presente
            
def posição(str,caractere):
    """
    Devolve a posição de um caractere em uma string
    """
    for i in range(len(str)):
        if str[i]==caractere[0]:
            return i
def isfloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def letra(caractere):
    """
    Dado um caractere, verifica se é uma letra ou não
    """
    modelo="ABCDEFGHIJKLMNOPQRSTUVWXYZÇÃÂÁÀÊÉÈÍÌÎÓÒÔÕÚÙÛabcdefghijklmnopqrstuvwxyzçãâáàéèêíìîõôóòúùû"
    pertence=False
    for i in range(len(modelo)):
        pertence = pertence or modelo[i]==caractere
    return pertence

def na_lista(palavra,lista):
    """
    Dado uma palavra, devolve True se a palavra está na lista
    """
    pertence=False
    for elemento in lista:
        pertence = pertence or elemento==palavra
    return pertence

def remove(arquivo): 
    arq = open(arquivo)
    linha = arq.readline()
    #S é a lista com cada linha tratada
    S = []
    #LIN é a lista com os índices de cada linha da entrada
    LIN=[]
    #-------Remove comentários-------
    apareceu=False  
    controle=False
    #a variável apareceu serve para ter informação sobre a aparição de """, 
    #enquanto controle serve para ter informação sobre a aparição de algum comentário
    numero_linha = 0
    while len(linha)>0:
        nova_linha=""
        
        if tem(linha,'"""'):
            if apareceu==False:
                nova_linha = linha[:posição(linha,'"""')]
                numero_linha+=1
                
                apareceu = True
                
            elif apareceu:
                nova_linha = linha[posição(linha,'"""')+3:]
                numero_linha+=1
                apareceu = False
            controle = True
                
            
        elif tem(linha,"'''"):
            if apareceu==False:
                nova_linha = linha[:posição(linha,"'''")]
                numero_linha+=1
                apareceu = True
            elif apareceu:
                nova_linha = linha[posição(linha,"'''")+3:]
                numero_linha+=1
                apareceu=False
            controle = True

        elif not tem(linha,'"""') and apareceu:
            numero_linha+=1

        elif not tem(linha,"'''") and apareceu:
            numero_linha+=1


        elif tem(linha,'#') and apareceu==False and écomentáriooustring(linha,posição(linha,"#")):
            nova_linha = linha[:posição(linha,"#")]
            numero_linha+=1
            controle = True
        
        

        if apareceu==False and controle==False:
            nova_linha = linha
            numero_linha+=1
        
        if apareceu==False:
            controle = False

        #Tratamento da linha a fim de remover o sinalizador de fim de linha
        s=""
        for i in range(len(nova_linha)):
            if nova_linha[i]!="\n":
                s+= nova_linha[i]


        #Conclusão de cada etapa do laço
        if s!="":
            S.append(s)
            LIN.append(numero_linha)
        linha=arq.readline()
        
    M=[]
    M.append(S)
    M.append(LIN)
    return M
y=remove(sys.argv[1])
print(y)
x = remove(sys.argv[1])[0]
print(x)
#DÁ ERRO QUANDO TEMOS QUE IDENTIFICAR SE "#opa" É uma string, que deveria ser, e ele acaba apagando

def tokenização(lista):
    """
    Passada uma lista cujos elementos são strings que repesentam as respectivas linhas do arquivo, devolve uma lista
    de strings com os elementos léxicos isolados.

    Elementos léxicos:
    1- sequências ininterruptas iniciadas por uma letra (incluindo o "_" ) seguida por letras e/ou dígitos
    2- sequências consecutivas de dígitos decimais
    3- quaisquer outros caracteres isolados, como parênteses, colchetes,pontuação,...
    """
    S=[]
    caso_1=False
    caso_2=False
    controle=False
    for elemento in lista:
        novo_elemento=""

        #Adição de "BEGGIN" e "END" se for o caso
        identação = len(elemento) - len(elemento.lstrip())
        if not controle:
            tamanho = identação
            controle = True
            
        elif controle and identação>tamanho:
            S.append("BEGGIN")
            controle=False
            
        elif controle and identação<tamanho:
            S.append("END")
            controle = False
        
        
        
        for i in range(len(elemento)):

            #Tratamento de identificadores
            if letra(elemento[i]) and not caso_1:
                
                if i== len(elemento)-1:
                    S.append(elemento[i])
                else:
                   novo_elemento+=elemento[i]
                caso_1=True 

            elif letra(elemento[i]) and caso_1:
                if i == len(elemento)-1:
                    novo_elemento+=elemento[i]
                    S.append(novo_elemento)
                else:
                    novo_elemento+=elemento[i]
            
            elif elemento[i].isdigit() and caso_1 and not caso_2:
                if i==len(elemento)-1:
                    novo_elemento+=elemento[i]
                    S.append(novo_elemento)
                else:
                    novo_elemento+=elemento[i]

            elif elemento[i]=="_" and caso_1:
                if i == len(elemento)-1:
                    novo_elemento+=elemento[i]
                    S.append(novo_elemento)
                else:
                    novo_elemento+=elemento[i]

            elif caso_1:
                S.append(novo_elemento)
                novo_elemento=""
                caso_1=False
            
            #Tratamento de números
            if elemento[i].isdigit() and not caso_1 and not caso_2:
                if i==len(elemento)-1:
                    S.append(elemento[i])
                else:
                    novo_elemento+=elemento[i]
                caso_2=True

            elif elemento[i].isdigit() and caso_2 and not caso_1:
                if i == len(elemento)-1:
                    novo_elemento+=elemento[i]
                    S.append(novo_elemento)
                else:
                    novo_elemento+=elemento[i]
            
            elif caso_2 and not caso_1:
                S.append(novo_elemento)
                novo_elemento=""
                caso_2=False
                
            
            #Tratamento de outros caracteres  
            if not elemento[i].isdigit() and not letra(elemento[i]) and not caso_1 and not caso_2:
                S.append(elemento[i])
        C=[]
        for elemento in S:
            if elemento!=" " and elemento!="":
                C.append(elemento)
        
    return C
   
x = tokenização(x)
print(x)
def generalização(lista):
    """
    Dada uma lista no modelo da saída da função tokenização, devolve uma lista em que:
    identificadores considerados reservados pelo python, mantém-se igual
    identificadores cujo caractere seguinte é '(' são considerados funções, logo, serão escritos como fun
    identificadores que não são função nem reservados, serão considerados variáveis
    
    """
    #reservados é uma lista cujos elementos são identificadores reservados do python
    reservados = "False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, form, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield".split(sep=", ")

    #string_1 refere-se ao uso de "" enquando string_2 refere-se ao uso de ''
    string_1=False
    string_2=False
    for i in range(len(lista)):
        if lista[i]=='"' and not string_1 and not string_2:
            string_1 = True
        elif lista[i]=="'" and not string_2 and not string_1:
            string_2=True
        elif not na_lista(lista[i],reservados) and i<len(lista)-1 and letra(lista[i][0]) and lista[i+1]=="(" and not string_1 and not string_2 :
            lista[i]="fun"
        elif not na_lista(lista[i],reservados) and i<len(lista)-1 and letra(lista[i][0]) and not string_1 and not string_2 :
            lista[i]="var"
        elif not na_lista(lista[i],reservados) and i==len(lista)-1 and letra(lista[i][0]) and not string_1 and not string_2:
            lista[i]="var"
        elif string_1 and lista[i]=='"':
            string_1=False
        elif string_2 and lista[i]=="'":
            string_2=False

    return lista
print(generalização(x))

def grava_resultado_lex(lista,arquivo):
    """
    Dada uma lista no modelo da saída da função generalização() e um arquivo, escreve um arquivo .lex contendo essa lista
    """
    nome_arq = arquivo[:-3]
    novo_arq = open(nome_arq+".lex","w")
    novo_arq.write(str(lista))

grava_resultado_lex(generalização(x),"generico.py")

def ngramas_comum(tokens1,tokens2,TAM_NGRAMA):
    M=[]
    controle = True
    for i in range(len(tokens1)-TAM_NGRAMA+1):
        for j in range(len(tokens2)-TAM_NGRAMA +1):
            if controle and tokens1[i:i+TAM_NGRAMA]==tokens2[j:j+TAM_NGRAMA]:
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
        L.append(''.join(ngrama))
    return L.sort()

def histograma(chaves,tokens,TAM_NGRAMA):
    """
    Dadas uma lista de chaves e outra de tokens, devolve um histograma com as ocorrências de cada chave no arquivo.
    """
    
    #Primeiro, vamos obter uma lista de ngramas a partir dos tokens.
    L=[]
    i=0
    while i<=len(tokens)-TAM_NGRAMA:
        L.append(''.join(tokens[i:i+TAM_NGRAMA]))
        i+=1
    L.sort()
    #Para facilitar a monstagem do histograma, sabemos que deve ter o mesmo número de elementos da lista de chaves,
    #Logo, inicializemos-o como uma lista com o mesmo número de elementos de chaves, porém, todos os valores são 0.
    H=[]
    for i in range(len(chaves)):
        H.append(0)
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
    print(chaves)
    
    
    #Construção dos histogramas
L=[1,2,3,4,5]
M=[4,5,6,7]
ngramas(L,M)
