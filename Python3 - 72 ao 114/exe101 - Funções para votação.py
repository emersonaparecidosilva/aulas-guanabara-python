#Exercício Python #101 - Funções para votação -> https://www.youtube.com/watch?v=czDcimdc3GU&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=37


print(('==*==')*20)
print('Bem vindo(a) - Funções para votação')
print(('==*==')*20)

from datetime import date

def eleitor(i):
    anoAtual = date.today().year
    idade = anoAtual - i
    if idade < 16:
        return f'Com {idade} anos, NÂO VOTA'
    elif idade >= 16 and idade < 18 or idade >= 70:
        return f'Com {idade} anos, VOTO OPCIONAL'  
    else:
        return f'Com {idade} anos, VOTO OBRIGATÓRIO'
    
anoNascimento = int(input('Digite o seu ano de nascimento: '))
print(eleitor(anoNascimento))