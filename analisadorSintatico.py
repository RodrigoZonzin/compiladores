from ClassToken import *

vetor_tokens =[Token(), Token(), Token()]
token = ''

#FUNCOES AUXILIARES

#DEFINICÇÃO DA GRMÁTICA
#Programa -> Funcao FuncaoSeq
def Programa(): 
    if(token == 'FUNCTION'):
        Funcao()
        FuncaoSeq()

#FuncaoSeq -> Funcao FuncaoSeq | e
def FuncaoSeq(): 
    if(token == 'FUNCTION'):
        Funcao()
        FuncaoSeq()

#Funcao -> fn NomeFuncao ( ListaParams ) TipoRetornoFuncao Bloco    
def Funcao():
    if(token == 'FUNCTION'):
        match()

