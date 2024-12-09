import json
from classeToken import *
import sys

def carregar_tokens(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        dados = json.load(file)

    return [Token(d['Token'], d['Lexema'], d['Linhas']) for d in dados]

# Controladores globais
vetor_tokens = carregar_tokens(sys.argv[1])


# Controladores globais
i = 0
token = vetor_tokens[i]

def match(expected):
    global token, i
    if token == expected:
        print(f"Reconhecido: {token.Tstring}. Linha: {token.nlinhas}")
        i += 1
        token = vetor_tokens[i] if i < len(vetor_tokens) else None
    else:
        raise SyntaxError(f"Erro sintático: esperado {expected}, encontrado {token.Tstring} na linha {token.nlinhas}.")

# Implementação da gramática
def Programa():
    if token == 'FUNCTION':
        Funcao()
        FuncaoSeq()
    else:
        raise SyntaxError(f"Erro no início do programa: esperado 'FUNCTION', encontrado {token.Tstring}.")

def FuncaoSeq():
    while token == 'FUNCTION':
        Funcao()

def Funcao():
    match('FUNCTION')
    NomeFuncao()
    match('LBRACKET')
    ListaParams()
    match('RBRACKET')
    TipoRetornoFuncao()
    Bloco()

def NomeFuncao():
    if token == 'MAIN':
        match('MAIN')
    elif token == 'ID':
        match('ID')
    else:
        raise SyntaxError(f"Erro: esperado 'MAIN' ou 'ID', encontrado {token.Tstring}.")

def ListaParams():
    if token == 'ID':
        match('ID')
        match('COLON')
        Type()
        ListaParams2()

def ListaParams2():
    while token == 'COMMA':
        match('COMMA')
        match('ID')
        match('COLON')
        Type()

def TipoRetornoFuncao():
    if token == 'ARROW':
        match('ARROW')
        Type()

def Type():
    if token in ['INT', 'FLOAT', 'CHAR']:
        match(token.Tstring)
    else:
        raise SyntaxError(f"Erro: esperado tipo (INT, FLOAT, CHAR), encontrado {token.Tstring}.")

def Bloco():
    match('LBRACE')
    Sequencia()
    match('RBRACE')


def Sequencia():
    while token in ['LET', 'ID', 'IF', 'WHILE', 'PRINTLN', 'RETURN']:
        if token == 'LET':
            print('entrei em Declaracao')
            Declaracao()
            print(f'sai de Declaracao. Token atual: {token}')
            Sequencia()
        else:
            print(f'entrei em comando')
            Comando()
            Sequencia()



def Declaracao():
    match('LET')
    VarList()
    match('COLON')
    Type()
    match('SEMICOLON')

def VarList():
    match('ID')
    while token == 'COMMA':
        match('COMMA')
        match('ID')

def Comando():
    if token == 'ID':
        match('ID')
        AtribuicaoOuChamada()

    elif token == 'IF':
        ComandoSe()

    elif token == 'WHILE':
        match('WHILE')
        Expr()
        Bloco()

    elif token == 'PRINTLN':
        match('PRINTLN')
        match('LBRACKET')
        match('FMT_STRING')

        if token != 'RBRACKET':
            ListaArgs()

        match('RBRACKET')
        match(';')

    elif token == 'RETURN':
        match('RETURN')
        Expr()
        match(';')

def AtribuicaoOuChamada():
    if token == 'EQUAL':
        match('EQUAL')
        Expr()
        match(';')
        
    elif token == 'LBRACKET':
        match('LBRACKET')
        ListaArgs()
        match('RBRACKET')
        match(';')

def ComandoSe():
    match('IF')
    Expr()
    Bloco()
    if token == 'ELSE':
        match('ELSE')
        if token == 'IF':
            ComandoSe()
        else:
            Bloco()

def Expr():
    Rel()
    while token in ['EQUAL_EQUAL', 'NOT_EQUAL']:
        OpIgual()
        Rel()

def OpIgual():
    if token in ['EQUAL_EQUAL', 'NOT_EQUAL']:
        match(token.Tstring)
    else:
        raise SyntaxError(f"Erro: esperado operador relacional, encontrado {token.Tstring}.")

def Rel():
    Adicao()
    while token in ['LESS', 'LESS_EQUAL', 'GREATER', 'GREATER_EQUAL']:
        OpRel()
        Adicao()

def OpRel():
    if token in ['LESS', 'LESS_EQUAL', 'GREATER', 'GREATER_EQUAL']:
        match(token.Tstring)
    else:
        raise SyntaxError(f"Erro: esperado operador relacional, encontrado {token.Tstring}.")

def Adicao():
    Termo()
    while token in ['PLUS', 'MINUS']:
        OpAdicao()
        Termo()

def OpAdicao():
    if token in ['PLUS', 'MINUS']:
        match(token.Tstring)

def Termo():
    Fator()
    while token in ['STAR', 'SLASH']:
        OpMult()
        Fator()

def OpMult():
    if token in ['STAR', 'SLASH']:
        match(token.Tstring)

def Fator():
    if token == 'ID':
        match('ID')
        ChamadaFuncao()
    elif token in ['INT_CONST', 'FLOAT_CONST', 'CHAR_LITERAL']:
        match(token.Tstring)
    elif token == 'LBRACKET':
        match('LBRACKET')
        Expr()
        match('RBRACKET')

def ChamadaFuncao():
    if token == 'LBRACKET':
        match('LBRACKET')
        ListaArgs()
        match('RBRACKET')

def ListaArgs():
    Arg()
    while token == 'COMMA':
        match('COMMA')
        Arg()

def Arg():
    if token in ['ID', 'INT_CONST', 'FLOAT_CONST', 'CHAR_LITERAL']:
        match(token.Tstring)
        if token == 'LBRACKET':
            ChamadaFuncao()

Programa()