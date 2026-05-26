#Exercício Python #094 - Unindo dicionários e listas - https://www.youtube.com/watch?v=ETnExBCFeps&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=27

print(('====')*20)
print('Bem vindo(a) - Unindo dicionários e listas')
print(('====')*20)

pessoas = {}
mulheres = []
listaPessoas = []
soma = 0
while True:
    pessoas['Nome:'] = input('Nome: ')
    while True:
        pessoas['Sexo:'] = input('Sexo: [F/M]: ').strip().upper()
        if pessoas['Sexo:'] not in 'FM':
            pessoas['Sexo:'] = input('Opção Incorreta, Digite Sexo: [F/M]: ').strip().upper()
        elif pessoas['Sexo:'] in 'FM':
            break    
    if pessoas['Sexo:'] == 'F':
        mulheres.append(pessoas['Nome:'])
    pessoas['Idade:'] = int(input('Idade: '))
    soma += pessoas['Idade:']
    listaPessoas.append(pessoas.copy())
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break        
mediaPessoas = soma/(len(listaPessoas))
print(f'A) Ao todo, temos {len(listaPessoas)} pessoas cadastradas')
print(f'B) A média de idade é de {mediaPessoas:.2f}')
print(f'C) As mulheres cadastradas foram: ',end = '')
for i in mulheres:
    print(f'{i}', end= ',')
print(f'\nD) Pessoas acima da média: ')
for e in listaPessoas:
    if e['Idade:'] >= mediaPessoas:
        for k, v in e.items():
            print(f'  {k} {v}', end = ' ')
        print()
print()
print('<<<< Encerrado')