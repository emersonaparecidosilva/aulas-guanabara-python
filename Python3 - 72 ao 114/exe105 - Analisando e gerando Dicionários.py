#Exercício Python #105 - Analisando e gerando Dicionários -> https://www.youtube.com/watch?v=Kbs97l38vVQ&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=40

print(('==*==')*20)
print('Bem vindo(a) - Exercício Python #105 - Analisando e gerando Dicionários')
print(('==*==')*20)

def notas(*notas,sit=False):
    """_Função criada para analisar notas e situações de diversos alunos_

    Args:
        sit (bool, optional): Exibir ou não a situação do aluno

    Returns:
        dict: Total de notas, Maior, Menor e Média.
    """
    soma = 0
    situacao = ''
    resultado = {}
    for c in notas:
        soma += c
    total = len(notas)
    média = soma/total
    if média < 6:
        situacao = 'RUIM'
    elif média >=6 and média <8:
        situacao = 'REGULAR'
    else:
        situacao = 'BOA'
    resultado.update({"Total": total, "Maior": max(notas),"Menor": min(notas), "Média": f'{média:.2f}' } )
    if sit:
        resultado.update({"Situação": situacao})
        print(resultado)
    else:
        print(resultado)
notas(10,10,8,5,4,2,9,9,sit=True)
help(notas)