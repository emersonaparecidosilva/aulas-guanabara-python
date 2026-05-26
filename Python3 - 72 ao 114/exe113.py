#Exercício Python #113 - Funções aprofundadas em Python - https://www.youtube.com/watch?v=KowQ_UIMuI8&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=49

import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos'))) # Adiciona a pasta 'modulos' ao sys.path

from numeros import leiaFloat,leiaInt
from textos import título

título('Funções aprofundadas em Python',2)

numFloat = leiaFloat('Digite um valor Real: ')
print(f'O valor digitado foi: {numFloat}')

print()
numInteiro = leiaInt('Digite um valor inteiro: ')
print(f'O valor digitado foi: {numInteiro}')


# try: #tente isso
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a/b
# except Exception as erro:
#     print(f'O Problema encontrado foi {erro.__class__}')
# else: #deu certo
#     print(f'O resultado é {r}')
# finally: #saudação final
#     print('Volte sempre! Muito Obrigado!')