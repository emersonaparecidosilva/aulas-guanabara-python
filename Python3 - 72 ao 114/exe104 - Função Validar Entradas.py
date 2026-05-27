#Exercício Python #104 - Validando entrada de dados em Python

print(('==*==')*20)
print('Bem vindo(a) - Validando entrada de dados em Python')
print(('==*==')*20)

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\33[0;31mERRO! Digite um número inteiro válido.\33[m')
        if ok:
            break
    return valor

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')