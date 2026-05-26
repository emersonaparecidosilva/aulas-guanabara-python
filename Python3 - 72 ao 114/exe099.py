#Exercício Python #099 - Função que descobre o maior

def escreva(txt):
    a = (len(txt))+4
    print(('=')*a)
    print(f'{txt:^{a}}')
    print(('=')*a)

escreva('Bem vindo(a) - Função que descobre o maior')
print()
from time import sleep

def maior(* num):
    print(('===')*30)
    print('Processando..')
    contador = maior = 0
    for e in num:
        print(f'{e}', end = ' ',flush=True)
        if e >= maior:
            maior = e
        contador +=1
        sleep(0.5)
    print(f'Foram informados {contador} valores ao todo') 
    print(f'O maior valor informado foi {maior}') 

maior(2,9,4,51,7,1)
maior(4,70,0)
maior(1,2)
maior(6)
maior()