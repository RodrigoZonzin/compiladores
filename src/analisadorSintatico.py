from ClassToken import *

#fn main(x: int, y: int){
#}
tk0 = Token('FUNCTION', 'fn', 1)
tk1 = Token('ID', 'soma', 1)
tk1 = Token('LBRACKET', '(', 1)
tk2 = Token('ID', 'x', 1)
tk3 = Token('COLON', ':', 1)
tk4 = Token('INT', 'int', 1)
tk5 = Token('COMMA', ',', 1)
tk6 = Token('ID', 'y', 1)
tk7 = Token('INT', 'int', 1)
tk8 = Token('RBRACKET', ')', 1)
tk9 = Token('RBRACE', '{', 1)
tk10 = Token('LBRACE', '}', 2)


vetor_tokens =[tk0, tk1, tk2, tk3, tk4, tk5, tk6, tk7, tk8, tk9, tk10]

i = 0
token = vetor_tokens[i]


print(tk0.Tstring)

#FUNCOES AUXILIARES
def match(lexiema): 
    if token == lexiema:
        print(f"Reconehcido {token.Tstring}")
        i += 1
        token = vetor_tokens[i]
        

#DEFINICÇÃO DA GRMÁTICA
#Programa -> Funcao FuncaoSeq

def Programa(): 
    print("OI")
    print(token.Tstring)
    if(token.Tstring == 'FUNCTION'):
        print("OIII")
        Funcao()
        FuncaoSeq()

#FuncaoSeq -> Funcao FuncaoSeq | e
def FuncaoSeq(): 
    print("FUNCAOSEQ")
    if(token == 'FUNCTION'):
        Funcao()
        FuncaoSeq()


def NomeFuncao(): 
    print("NOME")
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
    if(token == 'COMMA'): 
        match('COMMA')
    elif(token == 'ID'):
        match('ID')
    elif(token == 'COLON'):
        match('COLON')
    print(f"Erro nos parametros da função. Linha {token.numLinhas}")
    ListaParams2()

#TipoRetornoFuncao -> Type | e

def TipoRetornoFuncao(): 
    if token == 'ARROW':
        match('ARROW')
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

#Bloco -> { Sequencia }
def Bloco():
    if(token == 'LBRACE'):
        match('LBRACE')
        Sequencia()
        match('RBRACE')
    

def Sequencia():
    print('Implementação de Sequencia pendnete')

Programa()