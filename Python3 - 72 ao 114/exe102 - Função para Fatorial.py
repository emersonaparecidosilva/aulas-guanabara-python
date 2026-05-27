#Exercício Python #102 - Função para Fatorial -> https://www.youtube.com/watch?v=84jUX96cs7Q&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=37


print(('==*==')*20)
print('Bem vindo(a) - Função para Fatorial')
print(('==*==')*20)

def fatorial(núm,show=False):
    """_summary_

    Args:
        n (Inteiro): Define o valor do fatorial
        show (bool, optional): Apresenta os cálculos

    Returns:
        _type_: fatorial de n
    """
    f = 1
    for c in range(núm,0,-1):
        if show:
            print(c,end='')
            if c > 1:
                print(f' X ', end='')
            else:
                print(f' = ',end='')
        f *= c

    return f

# f2 = fatorial(4,True)
# f3 = fatorial(3,True)

print(fatorial(6,True))
print()
help(fatorial)