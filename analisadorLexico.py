import sys
import string
from ClassToken import *

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
        print(char, ESTADO)
    
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
                pass
            
                #tokens.append(Token(''))
            

            

    
    
    num_linha += 1