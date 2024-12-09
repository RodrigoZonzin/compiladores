from classeToken import *
import json 
import sys
import pdb 

def carregar_tokens(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        dados = json.load(file)

    return [Token(d['Token'], d['Lexema'], d['Linhas']) for d in dados]


vetor_tokens = carregar_tokens(sys.argv[1])
vetor_tokens.append(Token('EOF', 'eof', 0))

i = 0
token = vetor_tokens[i]

#FUNCOES AUXILIARES
def match(lexema):
    global token, i
    
    if token == lexema:
        print(f"Reconhecido {token}. i: {i}")
        i += 1
        token = vetor_tokens[i]
        
         
        
#DEFINICÇÃO DA GRMÁTICA
#Programa -> Funcao FuncaoSeq
def Programa(): 
    #pdb.set_trace()
    if(token == 'FUNCTION'):
        Funcao()
        FuncaoSeq()
    
    #if(token == 'EOF'):
    #    print("Fim da compilacao :)")
    
    else:
        raise Exception(f"Esperado uma função no inicio do codigo. Linha {token.nlinhas}")
    
    print('Compilacao terminada com sucesso')

#FuncaoSeq -> Funcao FuncaoSeq | e
def FuncaoSeq(): 
    #pdb.set_trace()
    if(token == 'FUNCTION'):
        Funcao()
        FuncaoSeq()

#Funcao -> fn NomeFuncao ( ListaParams ) TipoRetornoFuncao Bloco    
def Funcao():
    #pdb.set_trace()
    match('FUNCTION')
    NomeFuncao()
    match('LBRACKET')
    ListaParams()
    match('RBRACKET')
    TipoRetornoFuncao()
    Bloco()

#NomeFuncao -> ID | MAIN
def NomeFuncao(): 
    #pdb.set_trace()
    if token == 'MAIN': 
        match('MAIN')

    elif token == 'ID': 
        match('ID')

    else: 
        raise Exception(f'ID ou MAIN esperado {token.nlinhas}')
    
#ListaParams -> ID : Type ListaParams2 | e
def ListaParams(): 
    #pdb.set_trace()
    if token == 'ID':
        match('ID')
        match('COLON')
        Type()
        ListaParams2()


#ListaParams2 -> , ID : Type ListaParams2 | e
def ListaParams2():
    #pdb.set_trace()
    if token == 'COMMA':
        match( 'COMMA')
        
        match('ID')
        match( 'COLON')

        Type()
        ListaParams2()    
    
    #print(f"Erro nos parametros da função. Linha {token.nlinhas}")


    

#TipoRetornoFuncao ->  -> Type | e
def TipoRetornoFuncao(): 
    #pdb.set_trace()
    if token == 'ARROW':
        match('ARROW')
        Type()
    

#Bloco -> { Sequencia }
def Bloco():
    #pdb.set_trace()
    if(token == 'LBRACE'):
        match('LBRACE')
        Sequencia()
        match('RBRACE')
    else: 
        raise Exception(f'Esperado: {{. Observado: {token.lex}')
    
#Sequencia -> Declaracao Sequencia | Comando Sequencia | e
def Sequencia():
    #pdb.set_trace()
    if token == 'LET': 
        Declaracao()
        Sequencia()
    elif token in ['ID', 'IF', 'WHILE', 'PRINTLN', 'RETURN']: 
        Comando()
        Sequencia()

#Declaracao -> let VarList : Type ;
def Declaracao():
    #pdb.set_trace()
    match('LET')
    VarList()
    match('COLON')
    Type()
    match('SEMICOLON')

#VarList -> ID VarList2
def VarList():
    #pdb.set_trace()
    if token == 'ID':
        match('ID')
        VarList2()

#VarList2 -> , ID VarList2 | ε
def VarList2():
    #pdb.set_trace()
    if token == 'COMMA':
        match('COMMA')
        match('ID')
        VarList2()
        
#Type -> int | float | char
def Type():
    #pdb.set_trace()
    if token == 'INT':
        match('INT')
    
    elif token == 'FLOAT':
        match('FLOAT')
    
    elif token == 'CHAR':
        match('CHAR')
    
    else: 
        raise Exception(f"Esperado int, float ou char. Encontrado: {token.lex}. Linha: {token.nlinhas}")
    
"""
Comando → ID AtribuicaoOuChamada |
ComandoSe |
while Expr Bloco |
println( FMT_STRING, ListaArgs ) ; |
return Expr ;
"""

def Comando():
    #pdb.set_trace()
    #print('estou no comando')
    if token == 'ID':  
        match('ID')
        AtribuicaoOuChamada()
    
    elif token == 'IF':
        ComandoSe()
    
    elif token == 'WHILE':
        Expr()
        Bloco()

    elif token == 'PRINTLN': 
        match('LBRACKET')
        match('FMT_STRING')
        match('COMMA')
        ListaArgs()
        match('RBRACKET')
        match('SEMICOLON')
    
    elif token == 'RETURN':
        match('RETURN')
        #print("Vou pro Expr")
        Expr()
        match('SEMICOLON')
    
    else: 
        raise Exception(f"Esperado variavel, if, while, println ou return. Encontrado: {token.lex}. Linha: {token.nlinhas}")

#AtribuicaoOuChamada -> = Expr ; | ( ListaArgs ) ;
def AtribuicaoOuChamada():
    #pdb.set_trace()
    if token == 'ASSIGN':
        match('ASSIGN')
        Expr()
        match('SEMICOLON')

    elif token == 'LBRACKET': 
        match('LBRACKET')
        ListaArgs()
        match('RBRACKET')
    else: 
        raise Exception(f"Esperado = ou (). Encontrado: {token.lex}. Linha: {token.nlinhas}")
    

#ComandoSe -> if Expr Bloco ComandoSenao | Bloco
def ComandoSe(): 
    #pdb.set_trace()
    if token == 'IF':
        match('IF')
        Expr()
        Bloco()
        ComandoSenao()
    
    else: 
        Bloco()


#ComandoSenao -> else ComandoSe | ε
def ComandoSenao():
    #pdb.set_trace()
    if token == 'ELSE':
        match('ELSE')
        ComandoSe()
    
#Expr -> Rel ExprOpc
def Expr():
    #pdb.set_trace()
    Rel()
    ExprOpc()

#ExprOpc -> OpIgual Rel ExprOpc | ε
def ExprOpc(): 
    #pdb.set_trace()
    if token == 'EQ':
        OpIgual()
        Rel()
        ExprOpc()

#OpIgual -> == | !=
def OpIgual():
    #pdb.set_trace()
    if token == 'EQ':
        match('EQ')
    elif token == 'NE':
        match('NE')

#Rel -> Adicao RelOpc
def Rel(): 
    #pdb.set_trace()
    #print('entrei no rel. token: ', token)
    Adicao()
    RelOpc()

#RelOpc -> OpRel Adicao RelOpc | ε
def RelOpc():
    #pdb.set_trace()
    if token in ['GT', 'GE', 'LT', 'LE']: 
        OpRel()
        Adicao()
        RelOpc()
    
#OpRel -> < | <= | > | >=
def OpRel():       
    #pdb.set_trace() 
    if token == 'GT':
        match('GT')
        
    elif token == 'GE':
        match('GE')
    
    elif token == 'LT': 
        match('LT')    

    elif token == 'LE': 
        match('LE')
    
    else:
        raise Exception(f"Esperado operador relacional. Encontradp: {token.lex}. Linha: {token.nlinhas}")

#Adicao -> Termo AdicaoOpc
def Adicao():
    #pdb.set_trace()
    #print("Estou no Adicao")
    Termo()
    AdicaoOpc()

#AdicaoOpc -> OpAdicao Termo AdicaoOpc | ε
def AdicaoOpc(): 
    #pdb.set_trace()
    if token == 'PLUS':
        OpAdicao()
        Termo()
        AdicaoOpc()

#OpAdicao -> + | -
def OpAdicao():
    #pdb.set_trace()
    if token == 'PLUS':
        match('PLUS')

    elif token == 'MINUS':
        match('MINUS')
    
    else: 
        raise Exception(f"Esperado + ou -. Encontradp {token.lex}. Linha: {token.nlinhas}")

#Termo -> Fator TermoOpc
def Termo(): 
    #pdb.set_trace()
    Fator()
    TermoOpc()

#TermoOpc -> OpMult Fator TermoOpc | ε
def TermoOpc():
    #pdb.set_trace()
    if token == 'MULT': 
        OpMult()
        Fator()
        TermoOpc()

#OpMult -> * | /
def OpMult():
    #pdb.set_trace()
    if token == 'MULT':
        match('MULT')
    
    elif token == 'DIV':
        match('DIV')
    
    else: 
        raise Exception(f"Esperado * ou /. Encontrado {token.lex}. Linha: {token.nlinhas}")


"""
Fator → ID ChamadaFuncao |
INT_CONST |
FLOAT_CONST |
CHAR_LITERAL |
( Expr )
"""
def Fator():
    #pdb.set_trace()
    if token == 'ID': 
        match('ID')
        ChamadaFuncao()
    
    elif token == 'INT_CONST':
        match('INT_CONST')

    elif token == 'FLOAT_CONST':
        match('FLOAT_CONST')

    elif token == 'CHAR_CONST':
        match('CHAR_CONST')
    
    else: 
        raise Exception(f"Esperado chamda de funcao, int, float ou char. Encontrado {token.lex}. Linha: {token.nlinhas}")
    
#ChamadaFuncao -> ( ListaArgs ) | ε
def ChamadaFuncao(): 
    #pdb.set_trace()
    if token == 'LBRACKET':
        match('LBRACKET')
        ListaArgs()
        match('RBRACKET')

#ListaArgs -> Arg ListaArgs2 | ε
def ListaArgs():
    #pdb.set_trace()
    if token == 'ID': 
        Arg()
        ListaArgs2()

#ListaArgs2 -> , Arg ListaArgs2 | ε
def ListaArgs2():
    #pdb.set_trace()
    if token == 'COMMA': 
        match('COMMA')
        Arg()
        ListaArgs2()

#Arg -> ID ChamadaFuncao | INT_CONST | FLOAT_CONST | CHAR_LITERAL
def Arg():
    #pdb.set_trace()
    if token == 'ID':
        ChamadaFuncao()
    
    elif token == 'INT_CONST':
        match('INT_CONST')

    elif token == 'FLOAT_CONST':
        match('FLOAT_CONST')

    elif token == 'CHAR_LITERAL':
        match('CHAR_LITERAL')
    
    else: 
        raise Exception(f'Esperado chamada de funcao, int, float ou char. Encontrado: {token.lex}. Linha: {token.linha}')
    



Programa()