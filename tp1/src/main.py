import sys
from analisadorLexico import *
from analisadorSintatico import *

filename = sys.argv[1] 

print(filename)

al = AnalisadorLexico(filename)
al.analise()
al.salvar_tokens()
al.salvar_txt()


mainSintatico(al.tokens)


