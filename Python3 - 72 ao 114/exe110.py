#exercicio 110 - Tema XYZ

#Exercício Python #109 - Formatando Moedas em Python


import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos'))) # Adiciona a pasta 'modulos' ao sys.path

from moedas import aumentar,diminuir,dobro,metade,moeda,resumo
from helpers import título

título(' Formatando Moedas em Python - Resumo',2)
num = float(input('Digite o preço: R$ '))
resumo(num,80,35)