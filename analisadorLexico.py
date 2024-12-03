import sys
import string
from classeToken import *

fileName = sys.argv[1] 
file = open(fileName, "r")

#estado inicial 0
ESTADO = 0

lexeme = []
tokens = []

num_linha = 1

for line in file:
    ibuf = line.strip('\n')
    i = 0
    print(num_linha, line)
    while i< len(ibuf):
        char = ibuf[i]
        print(ESTADO, char)
    
        if ESTADO == 0: 
            if char == '(': 
                tokens.append(Token('LBRACKET', '(', num_linha))
                ESTADO = 0
            
            elif char == ')': 
                tokens.append(Token('RBRACKET', 'R', num_linha))
                ESTADO = 0
            
            elif char == ':': 
                tokens.append(Token('COLON', ':', num_linha))
                ESTADO = 0
            
            elif char == ',': 
                tokens.append(Token('COMMA', ',', num_linha))
                ESTADO = 0
            
            elif char == '{': 
                tokens.append(Token('LBRACE', '{', num_linha))
                ESTADO = 0
            
            elif char == '}': 
                tokens.append(Token('RBRACKET', '}', num_linha))
                ESTADO = 0
            
            elif char == ';': 
                tokens.append(Token('PCOMMA', ';', num_linha))
                ESTADO = 0

            elif char == '+': 
                tokens.append(Token('PLUS', '+', num_linha))
                ESTADO = 0
            
            elif char == '-': 
                tokens.append(Token('MINUS', '-', num_linha))
                ESTADO = 0
            
            elif char == '*': 
                tokens.append(Token('MULTI', '*', num_linha))
                ESTADO = 0
            
            elif char == '/': 
                tokens.append(Token('DIV', '/', num_linha))
                ESTADO = 0
            

            elif char == '=': 
                ESTADO = 1
            
            elif char == '!': 
                ESTADO = 2
            
            elif char == '>': 
                ESTADO = 3
            
            elif char == '<': 
                ESTADO = 4
            
            elif char == '-': 
                ESTADO = 5
            
            elif char in string.digits: 
                inicio = i
                lexeme.append(char)

                if i+1 == len(ibuf): 
                    palavra = ''.join(lexeme)
                    tokens.append(Token("INT_CONST", i, num_linha))
                    lexeme = []
                else: 
                    ESTADO = 6

            elif char in string.ascii_letters:
                inicio = i
                lexeme.append(char)
                if i+ 1 == len(ibuf):
                    tokens.append(inicio, i+1, num_linha)
                    lexeme =[]
                else: 
                    ESTADO = 9
            
            elif char == "'": 
                inicio = i
                ESTADO = 10
            
            elif char == '"': 
                inicio = i
                ESTADO = 12

            i += 1
        
        elif ESTADO == 1: 
            if char == '=':        
                tokens.append(Token('EQ', '==', num_linha))
                ESTADO = 0
            
            else:        
                tokens.append(Token('ASSIGN', '=', num_linha))
                ESTADO = 0
            
            i += 1

        elif ESTADO == 2: 
            if char == '=':
                tokens.append(Token("NE", '!=', num_linha))
                ESTADO = 0
            
            else: 
                raise Exception(f"{num_linha}: Errro após o token: {char}")
        
        elif ESTADO == 3: 
            if char == '=':
                tokens.append(Token('GE', '>=', num_linha))
                ESTADO = 0
            else: 
                tokens.append(Token('GT', '>', num_linha))
                ESTADO = 0
            
        elif ESTADO == 4:
            if char == '=':
                tokens.append(Token('LE', '<=', num_linha))
                ESTADO = 0
            
            else: 
                tokens.append(Token('LT', '<', num_linha))
                ESTADO = 0

            i += 1

        elif ESTADO == 5: 
            if char == '>':
                tokens.appendt(Token("ARROW", '>', num_linha))
                ESTADO = 0
            else: 
                tokens.append("MINUS", '-', num_linha)
                ESTADO = 0
        
        elif ESTADO == 6:
            if char == '.':
                lexeme.append(char)
                i += 1
                ESTADO = 7
            
            elif char in string.digits:
                lexeme.append(char)
                i += 1

                if i == len(ibuf):
                    ibuf = ibuf + " "
            
            else: 
                palavra = ''.join(lexeme)
                tokens.append(Token("INT_CONST", palavra, num_linha))
                ESTADO = 0
                lexeme = []

        elif ESTADO == 7:
            if char in string.digits:
                lexeme.append(char)
                i += 1
                ESTADO = 8
        
        elif ESTADO == 8:
            if char == '.':
                raise Exception(f"{num_linha}: Erro em {char}")
            
            elif char in string.digits:
                lexeme.append(char)
                i += 1
                if i == len(ibuf):
                    ibuf = ibuf + " "
            
            else:
                palavra = ''.join(lexeme)
                tokens.append(Token("FLOAT_CONST", palavra, num_linha))
                ESTADO = 0
                lexeme = []

        elif ESTADO == 9: 
            if char in string.digits or char in string.ascii_letters or char == '_':
                lexeme.append(char)
                i += 1
                if i == len(ibuf):
                    ibuf + " "
                
            else: 
                palavra = ''.join(lexeme)
                palavrasReservadas = ['fn', 'main', 'return', 'int', 'float', 'char', 'if', 'else', 'while', 'println', 'return']
                token_correspondente = ['FUNCTION', 'MAIN', 'LET', 'INT', 'FLOAT', 'CHAR', 'IF', 'ELSE', 'PRINTLN', 'RETURN']
                
                if palavra == 'main':
                    tokens.append(Token('MAIN', palavra, num_linha))
                    ESTADO = 0

                elif palavra == 'let':
                    tokens.append(Token('LET', palavra, num_linha))
                    ESTADO = 0

                elif palavra == 'int':
                    tokens.append(Token('INT', palavra, num_linha))
                    ESTADO = 0

                elif palavra == 'float':
                    tokens.append(Token('FLOAT', palavra, num_linha))
                    ESTADO = 0

                elif palavra == 'char':
                    tokens.append(Token('CHAR', palavra, num_linha))
                    ESTADO = 0

                elif palavra == 'if':
                    tokens.append(Token('IF', palavra, num_linha))
                    ESTADO = 0

                elif palavra == 'else':
                    tokens.append(Token('ELSE', palavra, num_linha))
                    ESTADO = 0

                elif palavra == 'while':
                    tokens.append(Token('WHILE', palavra, num_linha))
                    ESTADO = 0

                elif palavra == 'println':
                    tokens.append(Token('PRINTLN', palavra, num_linha))
                    ESTADO = 0

                elif palavra == 'return':
                    tokens.append(Token('RETURN', palavra, num_linha))
                    ESTADO = 0

                else: 
                    tokens.append(Token('ID', palavra, num_linha))
                    ESTADO = 0
                    
                lexeme = []
            
        elif ESTADO == 10:
            i += 1
            if char == "'": 
                tokens.append('CHAR_LITERAL', char, num_linha)
                i += 1
                ESTADO = 0

            else: 
                lexeme.append(char)
                ESTADO = 11
        
        elif ESTADO == 11: 
            if char == "'": 
                palavra = ''.join(lexeme)
                tokens.append('CHAR_LITERAL',palavra, num_linha)
                i += 1
                ESTADO = 0
                lexeme = []
            else:
                raise Exception(f"{num_linha}: Erro em {char}")
            
        elif ESTADO == 12: 
            lexeme.append(char)
            i += 1

            if char == '"':
                tokens.append('FMT_STRING', '', num_linha)
                i += 1
                ESTADO = 0
                lexeme = []
            
            else: 
                ESTADO = 13
            
        elif ESTADO == 13: 
            if char == '"':
                palavra = ''.join(lexeme)
                tokens.append('FMT_STRING', palavra, num_linha)
                i += 1
                ESTADO = 0
                lexeme = []

            else: 
                lexeme.append(char)
                i += 1               
    
    num_linha += 1


arq_saida = open('saida.tkn', 'w')

for token in tokens:
    arq_saida.write(f"{str(token)}\n")

arq_saida.close()