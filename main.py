import sys
from analisadorLexico import *
from analisadorSintatico import *

filename = sys.argv[1] 

al = AnalisadorLexico(filename)
#as = analisadorSintatico()
al.analise()
al.salvar_tokens()
al.salvar_txt()