#exercicio 106 - Exercício Python #106 - Sistema interativo de ajuda em Python

print(('==*==')*20)
print('Bem vindo(a) - Sistema interativo de ajuda em Python')
print(('==*==')*20)

from time import sleep

while True:
    print(f'\033[0;37;43m')
    print(('~~~~~~')*20)
    print(f'    Sistema de Ajuda PyHELP')
    print(('~~~~~~')*20,'\033[m')
    comando = input('Função ou Bliblioteca > ').strip()
    if comando == 'fim' or comando == '':
        break
    print(f'\033[0;37;46m')
    print(('~~~~~~')*20)
    print(f'\033[0;37;46m   Acessando o manual do comando {comando}')
    print(('~~~~~~')*20,'\033[m')
    sleep(2)
    print(f'\033[0;37;47m')
    print(f'\033[0;37;47m {help(comando)} \033[m')
print(f'\033[0;37;41m')
print(('~~~~~~')*20)
print(f'\033[0;37;41m   Até logo!')
print(('~~~~~~')*20,'\033[m')