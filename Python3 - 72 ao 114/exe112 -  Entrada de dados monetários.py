#Exercício Python #112 - Entrada de dados monetários

import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos'))) # Adiciona a pasta 'modulos' ao sys.path

from helpers import título
from moedas import leiaDinheiro,resumo

título('Entrada de dados monetários',4)
p = leiaDinheiro('Digite o preço: R$ ')
resumo(p,10,35)