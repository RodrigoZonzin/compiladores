from ClassToken import *

vetor_tokens =[Token(), Token(), Token()]
token = vetor_tokens[0]
i = 0

#FUNCOES AUXILIARES
def match(): 
    pass


#DEFINICÇÃO DA GRMÁTICA
#Programa -> Funcao FuncaoSeq

def Programa(): 
    token = vetor_tokens[i]
    if(token == 'FUNCTION'):
        Funcao()
        FuncaoSeq()

#FuncaoSeq -> Funcao FuncaoSeq | e
def FuncaoSeq(): 
    if(token == 'FUNCTION'):
        Funcao()
        FuncaoSeq()


def NomeFuncao(): 
    if token == 'MAIN': 
        match('MAIN')
    elif token == 'ID': 
        match('ID')
    else: 
        print('ID ou MAIN Esperado na entrada')
    


#Funcao -> fn NomeFuncao ( ListaParams ) TipoRetornoFuncao Bloco    
def Funcao():
    match('FUNCTION')
    NomeFuncao()
    match('LBRACKET')
    ListaParams()
    match('RBRACKET')
    TipoRetornoFuncao()
    Bloco()

#NomeFuncao -> ID | MAIN
def NomeFuncao(): 
    if(token == 'ID'):
        match('ID')
    elif(token == 'MAIN'):
        match('MAIN')
    else:
        print(f"Erro no nome da Funcao. Linha {token.numLinhas}")

#ListaParams -> ID : Type ListaParams2 | e
def ListaParams(): 
    if(token == 'ID'):
        match('ID')
    match(":")
    ListaParams2()

#ListaParams2 -> , ID : Type ListaParams2 | e
def ListaParams2():
    if(token == ','): 
        match(',')
    elif(token == 'ID'):
        match('ID')
    elif(token == ':'):
        match(':')
    print(f"Erro nos parametros da função. Linha {token.numLinhas}")
    ListaParams2()

#TipoRetornoFuncao -> Type | e
def TipoRetornoFuncao(): 
    Type()

#Type -> int | float | char
def Type(): 
    if(token == 'INT'):
        match('INT')

    elif(token == 'FLOAT'):
        match('FLOAT')

    elif(token == 'CHAR'):
        match('CHAR')

    else: 
        print(f"Esperado  INT, FLOAT ou CHAR. Linha {token.numLinhas}")

def Bloco():
    pass

