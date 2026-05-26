#Exercício Python #096 - Função que calcula área - https://www.youtube.com/watch?v=oV1s53YGtvE&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=30

print(('==*==')*20)
print('Bem vindo(a) - Função que calcula área')
print(('==*==')*20)

def area(largura,comprimento):
    a = largura*comprimento
    print(f'A área de um terreno de {largura}X{comprimento} é de {a}m²')

largura = float(input("Digite a largura do Terreno (m): "))
comprimento = float(input("Digite o comprimento do Terreno (m): "))
area(largura,comprimento)
