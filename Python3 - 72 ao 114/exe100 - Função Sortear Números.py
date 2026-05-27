#exercicio 100 - Tema XYZ

def escreva(txt):
    a = (len(txt))+4
    print(('=')*a)
    print(f'{txt:^{a}}')
    print(('=')*a)

escreva('Bem vindo(a) - Função que descobre o maior')
print()

from random import randint,choice
from time import sleep

lista = []
sorteados = []
listaPares = []

def sortear(valor):
    somaPares = 0
    for e in range(15):
        lista.append(randint(1,10))
    print('Sorteando 5 valores da lista: ',end='')
    for i in range(valor):
        s = choice(lista)
        print(f'{s}', end = ' ',flush=True)
        sleep(0.5)
        sorteados.append(s)
    print('Pronto!')
    for a in sorteados:
        if a % 2 == 0:
            somaPares += a
            listaPares.append(a)
    print(f'Somando os valores pares de {sorteados}, temos {somaPares}')   
sortear(5)
