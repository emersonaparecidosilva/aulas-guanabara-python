#Exercício Python #103 - Ficha do Jogador

print(('==*==')*20)
print('Bem vindo(a) - Ficha do Jogador')
print(('==*==')*20)

def ficha(jog = '<Desconhecido>',gol = 0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato!')

nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols=int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol = gols)
else:
    ficha(nome,gols)