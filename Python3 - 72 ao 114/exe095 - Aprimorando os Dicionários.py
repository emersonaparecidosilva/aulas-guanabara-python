#Exercício Python #095 - Aprimorando os Dicionários - https://www.youtube.com/watch?v=mw1So0r317Y&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH

print(('==*==')*20)
print('Bem vindo(a) - Exercício Python #095 - Aprimorando os Dicionários')
print(('==*==')*20)

jogador = {}
listaJogadores = []
while True:
    jogador['nomeJogador'] = input('Nome do jogador: ')
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nomeJogador"]} jogou? '))
    golsPartidas = []
    totalGolPartidas = 0
    for p,i in enumerate(range(0,jogador["partidas"])):
        gols = int(input(f'     Quantos gols {jogador["nomeJogador"]} fez na {p+1} partida? '))
        golsPartidas.append(gols)
        totalGolPartidas += gols
    jogador['gols'] = golsPartidas
    jogador['total'] = totalGolPartidas
    listaJogadores.append(jogador.copy())
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break    
print(('=====')*20)
print(f'{"Cód.":<4}{"Jogador":<20}{"gols":>10}{"Total":>25}')
print(('=====')*20)
max_len_gols = max(len(str(jogador['gols'])) for jogador in listaJogadores)

for p,e in enumerate(listaJogadores):
    gols_str = str(e['gols']).rjust(max_len_gols) # Ajustar o preenchimento da coluna "gols" com base no comprimento máximo
    print(f'{p:<4}{e["nomeJogador"].upper():<20}',end='')
    print(f'{gols_str:>10}',end='')
    print(f'{e["total"]:>25}')
print(('=====')*20)

while True:
    mostrarJogador = int(input('\nEscolha um jogador para ver as partidas: [999 para parar]: '))
    if mostrarJogador == 999:
        break
    elif mostrarJogador < len(listaJogadores):
        print(f'===LEVANTAMENTO DO JOGADOR {listaJogadores[mostrarJogador]["nomeJogador"]}===')
        for p,i in enumerate(listaJogadores[mostrarJogador]["gols"]):
                print(f'    Na partida {p+1}, fez {i} gols.')
        print(('=====')*20)
    else:
        mostrarJogador = int(input('\nOpção incorreta, escolha um jogador para ver as partidas: [999 para parar]: '))
    
            