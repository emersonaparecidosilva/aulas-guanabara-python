#Exercício Python #109 - Formatando Moedas em Python


import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos'))) # Adiciona a pasta 'modulos' ao sys.path

from moedas import aumentar,diminuir,dobro,metade,moeda,resumo
from helpers import título

título(' Formatando Moedas em Python - Continuação - Opção Moeda',2)
num = float(input('Digite o preço: R$ '))

print(f'A metade de {moeda(num)} é {metade(num,True)}.')
print(f'O dobro de {moeda(num)} é {dobro(num,True)}.')
print(f'Aumentando 10% de {moeda(num)} é {aumentar(num,10,True)}.')
print(f'Diminuindo 10% de {moeda(num)} é {diminuir(num,13,True)}.')