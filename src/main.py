import sys
from src.analisadorLexico import *
from src.analisadorSintatico import *

filename = sys.argv[1] 

al = AnalisadorLexico(filename)
#as = analisadorSintatico()
al.analise()
al.salvar_tokens()
al.salvar_txt()