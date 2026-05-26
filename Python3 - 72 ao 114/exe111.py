#Exercício Python #111 - Transformando módulos em pacotes

import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos'))) # Adiciona a pasta 'modulos' ao sys.path

from helpers import título
from moedas import resumo

título(' Formatando Moedas em Python - Resumo',2)
num = float(input('Digite o preço: R$ '))
resumo(num,80,35)
