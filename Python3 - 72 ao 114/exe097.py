#Exercício Python #097 - Um print especial

def escreva(txt):
    a = (len(txt))+4
    print(('=')*a)
    print(f'{txt:^{a}}')
    print(('=')*a)

escreva('Bem vindo(a) - Um print especial')

escreva("Emerson Silva")
escreva("Curso de Python no Youtube")
escreva("CeV")



