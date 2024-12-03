import string
import json
from src.classeToken import *

class AnalisadorLexico():
    def __init__(self, filename): 
        self.filename = filename
        self.lexeme = []
        self.tokens = []
        self.ESTADO = 0         #estado inicial 0

    def analise(self):
        file = open(self.filename, "r")

        num_linha = 1

        for line in file:
            ibuf = line.strip('\n')
            i = 0
            print(num_linha, line)
            while i< len(ibuf):
                char = ibuf[i]
                print(self.ESTADO, char)
            
                if self.ESTADO == 0: 
                    if char == '(': 
                        self.tokens.append(Token('LBRACKET', '(', num_linha))
                        self.ESTADO = 0
                    
                    elif char == ')': 
                        self.tokens.append(Token('RBRACKET', 'R', num_linha))
                        self.ESTADO = 0
                    
                    elif char == ':': 
                        self.tokens.append(Token('COLON', ':', num_linha))
                        self.ESTADO = 0
                    
                    elif char == ',': 
                        self.tokens.append(Token('COMMA', ',', num_linha))
                        self.ESTADO = 0
                    
                    elif char == '{': 
                        self.tokens.append(Token('LBRACE', '{', num_linha))
                        self.ESTADO = 0
                    
                    elif char == '}': 
                        self.tokens.append(Token('RBRACKET', '}', num_linha))
                        self.ESTADO = 0
                    
                    elif char == ';': 
                        self.tokens.append(Token('PCOMMA', ';', num_linha))
                        self.ESTADO = 0

                    elif char == '+': 
                        self.tokens.append(Token('PLUS', '+', num_linha))
                        self.ESTADO = 0
                    
                    elif char == '-': 
                        self.tokens.append(Token('MINUS', '-', num_linha))
                        self.ESTADO = 0
                    
                    elif char == '*': 
                        self.tokens.append(Token('MULTI', '*', num_linha))
                        self.ESTADO = 0
                    
                    elif char == '/': 
                        self.tokens.append(Token('DIV', '/', num_linha))
                        self.ESTADO = 0
                    

                    elif char == '=': 
                        self.ESTADO = 1
                    
                    elif char == '!': 
                        self.ESTADO = 2
                    
                    elif char == '>': 
                        self.ESTADO = 3
                    
                    elif char == '<': 
                        self.ESTADO = 4
                    
                    elif char == '-': 
                        self.ESTADO = 5
                    
                    elif char in string.digits: 
                        inicio = i
                        self.lexeme.append(char)

                        if i+1 == len(ibuf): 
                            palavra = ''.join(self.lexeme)
                            self.tokens.append(Token("INT_CONST", i, num_linha))
                            self.lexeme = []
                        else: 
                            self.ESTADO = 6

                    elif char in string.ascii_letters:
                        inicio = i
                        self.lexeme.append(char)
                        if i+ 1 == len(ibuf):
                            self.tokens.append(inicio, i+1, num_linha)
                            self.lexeme =[]
                        else: 
                            self.ESTADO = 9
                    
                    elif char == "'": 
                        inicio = i
                        self.ESTADO = 10
                    
                    elif char == '"': 
                        inicio = i
                        self.ESTADO = 12

                    i += 1
                
                elif self.ESTADO == 1: 
                    if char == '=':        
                        self.tokens.append(Token('EQ', '==', num_linha))
                        self.ESTADO = 0
                    
                    else:        
                        self.tokens.append(Token('ASSIGN', '=', num_linha))
                        self.ESTADO = 0
                    
                    i += 1

                elif self.ESTADO == 2: 
                    if char == '=':
                        self.tokens.append(Token("NE", '!=', num_linha))
                        self.ESTADO = 0
                    
                    else: 
                        raise Exception(f"{num_linha}: Errro após o token: {char}")
                
                elif self.ESTADO == 3: 
                    if char == '=':
                        self.tokens.append(Token('GE', '>=', num_linha))
                        self.ESTADO = 0
                    else: 
                        self.tokens.append(Token('GT', '>', num_linha))
                        self.ESTADO = 0
                    
                elif self.ESTADO == 4:
                    if char == '=':
                        self.tokens.append(Token('LE', '<=', num_linha))
                        self.ESTADO = 0
                    
                    else: 
                        self.tokens.append(Token('LT', '<', num_linha))
                        self.ESTADO = 0

                    i += 1

                elif self.ESTADO == 5: 
                    if char == '>':
                        self.tokens.appendt(Token("ARROW", '>', num_linha))
                        self.ESTADO = 0
                    else: 
                        self.tokens.append("MINUS", '-', num_linha)
                        self.ESTADO = 0
                
                elif self.ESTADO == 6:
                    if char == '.':
                        self.lexeme.append(char)
                        i += 1
                        self.ESTADO = 7
                    
                    elif char in string.digits:
                        self.lexeme.append(char)
                        i += 1

                        if i == len(ibuf):
                            ibuf = ibuf + " "
                    
                    else: 
                        palavra = ''.join(self.lexeme)
                        self.tokens.append(Token("INT_CONST", palavra, num_linha))
                        self.ESTADO = 0
                        self.lexeme = []

                elif self.ESTADO == 7:
                    if char in string.digits:
                        self.lexeme.append(char)
                        i += 1
                        self.ESTADO = 8
                
                elif self.ESTADO == 8:
                    if char == '.':
                        raise Exception(f"{num_linha}: Erro em {char}")
                    
                    elif char in string.digits:
                        self.lexeme.append(char)
                        i += 1
                        if i == len(ibuf):
                            ibuf = ibuf + " "
                    
                    else:
                        palavra = ''.join(self.lexeme)
                        self.tokens.append(Token("FLOAT_CONST", palavra, num_linha))
                        self.ESTADO = 0
                        self.lexeme = []

                elif self.ESTADO == 9: 
                    if char in string.digits or char in string.ascii_letters or char == '_':
                        self.lexeme.append(char)
                        i += 1
                        if i == len(ibuf):
                            ibuf + " "
                        
                    else: 
                        palavra = ''.join(self.lexeme)
                        palavrasReservadas = ['fn', 'main', 'return', 'int', 'float', 'char', 'if', 'else', 'while', 'println', 'return']
                        token_correspondente = ['FUNCTION', 'MAIN', 'LET', 'INT', 'FLOAT', 'CHAR', 'IF', 'ELSE', 'PRINTLN', 'RETURN']
                        
                        if palavra == 'main':
                            self.tokens.append(Token('MAIN', palavra, num_linha))
                            self.ESTADO = 0

                        elif palavra == 'let':
                            self.tokens.append(Token('LET', palavra, num_linha))
                            self.ESTADO = 0

                        elif palavra == 'int':
                            self.tokens.append(Token('INT', palavra, num_linha))
                            self.ESTADO = 0

                        elif palavra == 'float':
                            self.tokens.append(Token('FLOAT', palavra, num_linha))
                            self.ESTADO = 0

                        elif palavra == 'char':
                            self.tokens.append(Token('CHAR', palavra, num_linha))
                            self.ESTADO = 0

                        elif palavra == 'if':
                            self.tokens.append(Token('IF', palavra, num_linha))
                            self.ESTADO = 0

                        elif palavra == 'else':
                            self.tokens.append(Token('ELSE', palavra, num_linha))
                            self.ESTADO = 0

                        elif palavra == 'while':
                            self.tokens.append(Token('WHILE', palavra, num_linha))
                            self.ESTADO = 0

                        elif palavra == 'println':
                            self.tokens.append(Token('PRINTLN', palavra, num_linha))
                            self.ESTADO = 0

                        elif palavra == 'return':
                            self.tokens.append(Token('RETURN', palavra, num_linha))
                            self.ESTADO = 0

                        else: 
                            self.tokens.append(Token('ID', palavra, num_linha))
                            self.ESTADO = 0
                            
                        self.lexeme = []
                    
                elif self.ESTADO == 10:
                    i += 1
                    if char == "'": 
                        self.tokens.append('CHAR_LITERAL', char, num_linha)
                        i += 1
                        self.ESTADO = 0

                    else: 
                        self.lexeme.append(char)
                        self.ESTADO = 11
                
                elif self.ESTADO == 11: 
                    if char == "'": 
                        palavra = ''.join(self.lexeme)
                        self.tokens.append('CHAR_LITERAL',palavra, num_linha)
                        i += 1
                        self.ESTADO = 0
                        self.lexeme = []
                    else:
                        raise Exception(f"{num_linha}: Erro em {char}")
                    
                elif self.ESTADO == 12: 
                    self.lexeme.append(char)
                    i += 1

                    if char == '"':
                        self.tokens.append('FMT_STRING', '', num_linha)
                        i += 1
                        self.ESTADO = 0
                        self.lexeme = []
                    
                    else: 
                        self.ESTADO = 13
                    
                elif self.ESTADO == 13: 
                    if char == '"':
                        palavra = ''.join(self.lexeme)
                        self.tokens.append('FMT_STRING', palavra, num_linha)
                        i += 1
                        self.ESTADO = 0
                        self.lexeme = []

                    else: 
                        self.lexeme.append(char)
                        i += 1               
            
            num_linha += 1

    def salvar_txt(self):
        nome_arq_saida = self.filename[:-2]+".txt"
        arq_saida = open(nome_arq_saida, 'w')
        
        for token in self.tokens: 
            arq_saida.write(str(token)+"\n")
        
        arq_saida.close()

    def salvar_tokens(self):
        nome_arq_saida = self.filename[:-2]+".json"
        print(nome_arq_saida)
        with open(nome_arq_saida, 'w', encoding='utf-8') as arq_saida:

            json.dump([token.to_dict() for token in self.tokens], arq_saida, indent=4, ensure_ascii=False)


