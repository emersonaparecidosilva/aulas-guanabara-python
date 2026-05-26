#Exercício Python #098 - Função de Contador

def escreva(txt):
    a = (len(txt))+4
    print(('=')*a)
    print(f'{txt:^{a}}')
    print(('=')*a)

escreva('Bem vindo(a) - Função de Contador')
from time import sleep

def contador(i,f,p):
    print(f'Contagem de {i} até {f}, de {p} em {p}')
    if f <=0:
        f = f-1
    else:
        f = f+1
    for e in range(i,f,p):
         print(f'{e} ',end = '',flush=True)
         sleep(0.5)
    print('FIM')
    

contador(1,10,1)
contador(10,0,-2)
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i,f,p)