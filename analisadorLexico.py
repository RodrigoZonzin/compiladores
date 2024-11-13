import sys
from Token import *

ARGUMENTOS = sys.argv

fileName = ARGUMENTOS[1] 
file = open(fileName, "r")

print(fileName)

linhas = []
tokens = []

with open(fileName, 'r') as file:
    for line in file:
        line = line.strip()

        for caractere in line:
            if True:
                pass
                if caractere == "":
                    pass


for tok in linhas:
    #print(tok, '\n\n')
    pass