from classeToken import *

class AnalisadorSintatico():
    
    def __init__(self, resultado_lexico):
        self.i = 0
        self.vetor_tokens = resultado_lexico
        self.token = self.vetor_tokens[0]

    def match(self, expected):
        if self.token == expected:
            print(f"Reconhecido: {self.token.Tstring}. Linha: {self.token.nlinhas}")
            self.i += 1
            self.token = self.vetor_tokens[self.i] if self.i < len(self.vetor_tokens) else None
        else:
            raise Exception(f"Erro sintático: esperado {expected}. Encontrado {self.token.Tstring} na linha {self.token.nlinhas}.")

    # Implementação da gramática
    def Programa(self):
        if self.token == 'FUNCTION':
            self.Fucao()
            self.FuncaoSeq()
        else:
            raise Exception(f"Erro no início do programa: esperado 'FUNCTION', encontrado {self.token.Tstring}.")

    def FuncaoSeq(self):
        while self.token == 'FUNCTION':
            self.Fucao()

    def Fucao(self):
        self.match('FUNCTION')
        self.NomeFuncao()
        self.match('LBRACKET')
        self.ListaParams()
        self.match('RBRACKET')
        self.TipoRetornoFuncao()
        self.Bloco()

    def NomeFuncao(self):
        if self.token == 'MAIN':
            self.match('MAIN')
        elif self.token == 'ID':
            self.match('ID')
        else:
            raise Exception(f"Erro: esperado 'MAIN' ou 'ID', encontrado {self.token.Tstring}.")

    def ListaParams(self):
        if self.token == 'ID':
            self.match('ID')
            self.match('COLON')
            self.Type()
            self.ListaParams2()

    def ListaParams2(self):
        while self.token == 'COMMA':
            self.match('COMMA')
            self.match('ID')
            self.match('COLON')
            self.Type()

    def TipoRetornoFuncao(self):
        if self.token == 'ARROW':
            self.match('ARROW')
            self.self.Type()

    def Type(self):
        if self.token in ['INT', 'FLOAT', 'CHAR']:
            self.match(self.token.Tstring)
        else:
            raise Exception(f"Erro: esperado tipo (INT, FLOAT, CHAR), encontrado {self.token.Tstring}.")

    def Bloco(self):
        self.match('LBRACE')
        self.Sequencia()
        self.match('RBRACE')

    def Sequencia(self):
        print('token atual', self.token)
        if self.token == 'LET':
            self.Declaracao()
            self.Sequencia()
        else: 
            self.Comando()
            self.Sequencia()

        #print()        

    def Declaracao(self):
        self.match('LET')
        self.VarList()
        self.match('COLON')
        self.Type()
        self.match('SEMICOLON')

    def VarList(self):
        self.match('ID')
        while self.token == 'COMMA':
            self.match('COMMA')
            self.match('ID')

    def Comando(self):
        if self.token == 'ID':
            self.match('ID')
            self.AtribuicaoOuChamada()
        elif self.token == 'IF':
            self.ComandoSe()
        elif self.token == 'WHILE':
            self.match('WHILE')
            self.Expr()
            self.Bloco()
        elif self.token == 'PRINTLN':
            self.match('PRINTLN')
            self.match('LBRACKET')
            self.match('FMT_STRING')
            if self.token != 'RBRACKET':
                self.ListaArgs()
            self.match('RBRACKET')
            self.match(';')
        elif self.token == 'RETURN':
            self.match('RETURN')
            self.Expr()
            self.match(';')

    def AtribuicaoOuChamada(self):
        if self.token == 'EQUAL':
            self.match('EQUAL')
            self.Expr()
            self.match(';')

        elif self.token == 'LBRACKET':
            self.match('LBRACKET')
            self.ListaArgs()
            self.match('RBRACKET')
            self.match(';')

    def ComandoSe(self):
        self.match('IF')
        self.Expr()
        self.Bloco()
        if self.token == 'ELSE':
            self.match('ELSE')
            if self.token == 'IF':
                self.ComandoSe()
            else:
                self.Bloco()

    def Expr(self):
        self.Rel()
        
        while self.token in ['EQUAL_EQUAL', 'NOT_EQUAL']:
            self.OpIgual()
            self.Rel()

    def OpIgual(self):
        if self.token in ['EQUAL_EQUAL', 'NOT_EQUAL']:
            self.match(self.token.Tstring)
        else:
            raise Exception(f"Erro: esperado operador relacional, encontrado {self.token.Tstring}.")

    def Rel(self):
        self.Adicao()
        while self.token in ['LESS', 'LESS_EQUAL', 'GREATER', 'GREATER_EQUAL']:
            self.OpRel()
            self.Adicao()

    def OpRel(self):
        if self.token in ['LESS', 'LESS_EQUAL', 'GREATER', 'GREATER_EQUAL']:
            self.match(self.token.Tstring)
        else:
            raise Exception(f"Erro: esperado operador relacional, encontrado {self.token.Tstring}.")

    def Adicao(self):
        self.Termo()
        while self.token in ['PLUS', 'MINUS']:
            self.OpAdicao()
            self.Termo()

    def OpAdicao(self):
        if self.token in ['PLUS', 'MINUS']:
            self.match(self.token.Tstring)

    def Termo(self):
        self.Fator()
        while self.token in ['STAR', 'SLASH']:
            self.OpMult()
            self.Fator()

    def OpMult(self):
        if self.token in ['STAR', 'SLASH']:
            self.match(self.token.Tstring)

    def Fator(self):
        if self.token == 'ID':
            self.match('ID')
            self.ChamadaFuncao()
        elif self.token in ['INT_CONST', 'FLOAT_CONST', 'CHAR_LITERAL']:
            self.match(self.token.Tstring)
        elif self.token == 'LBRACKET':
            self.match('LBRACKET')
            self.Expr()
            self.match('RBRACKET')

    def ChamadaFuncao(self):
        if self.token == 'LBRACKET':
            self.match('LBRACKET')
            self.self.ListaArgs()
            self.match('RBRACKET')

    def ListaArgs(self):
        self.Arg()
        while self.token == 'COMMA':
            self.match('COMMA')
            self.Arg()

    def Arg(self):
        if self.token in ['ID', 'INT_CONST', 'FLOAT_CONST', 'CHAR_LITERAL']:
            self.match(self.token.Tstring)
            if self.token == 'LBRACKET':
                self.ChamadaFuncao()
