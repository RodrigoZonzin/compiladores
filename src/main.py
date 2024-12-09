import sys
from analisadorLexico import *

filename = sys.argv[1] 

print(filename)

al = AnalisadorLexico(filename)
al.analise()
al.salvar_tokens()
al.salvar_txt()

#analisador sintativo
#vetor_tokens = al.tokens
#Programa()


