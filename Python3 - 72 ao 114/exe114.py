#Exercício Python #114 - Site está acessível? -> https://www.youtube.com/watch?v=8jAykqxIeqw&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=50

import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos'))) # Adiciona a pasta 'modulos' ao sys.path

from textos import título
import urllib
import urllib.request

título('Exercício Python #114 - Site está acessível?',2)

def check_site(url):
    try:
        response = urllib.request.urlopen(url)
        print(f'Tudo ok! O site {url} está acessível.')
    except:
        print(f'Deu erro! O site {url} não está acessível.')

# Exemplo de uso
check_site('https://www.google.com.br/')
