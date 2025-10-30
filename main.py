#Programa Principal

from front import menu,saudacao
from back import diagnostico,resultado

rodada=1
entrevistados= []

qtde_entrevistados=menu()
while rodada<=qtde_entrevistados:
    print ("Cadastre o usuário",rodada)
    print ("Digite no nome do usuário")
    nome = input()
    entrevistados.append(nome)
    rodada=rodada+1   

saudacao()
diagnostico()
resultado()

