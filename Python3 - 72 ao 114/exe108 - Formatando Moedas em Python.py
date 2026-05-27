#Exercício Python #108 - Formatando Moedas em Python

import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos'))) # Adiciona a pasta 'modulos' ao sys.path

from moedas import aumentar,diminuir,dobro,metade,moeda
from helpers import título

título('Formatando Moedas - Colocando a vírgula',2)
num = float(input('Digite o preço: R$ '))

print(f'A metade de {moeda(num)} é {moeda(metade(num))}.')
print(f'O dobro de {moeda(num)} é {moeda(dobro(num))}.')
print(f'Aumentando 10% de {moeda(num)} é {moeda(aumentar(num,10))}.')
print(f'Diminuindo 10% de {moeda(num)} é {moeda(diminuir(num,10))}.')

