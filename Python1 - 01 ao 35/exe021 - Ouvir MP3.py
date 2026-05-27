# Exercicio 21 - Ouvir Mp3 pelo Python - Funcionou no VSCode -> https://www.youtube.com/watch?v=9FiEji_fzvk&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=22&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Ouvir MP3')
print(('==*==')*20)

# Para ouvir um arquivo mp3, é necessário instalar a biblioteca pygame. Rode antes de executar o script: pip install pygame
import os
import pygame

pygame.init()

# Salve o arquivo mp3 na pasta raiz do projeto.
caminho_musica = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'musica.mp3'))

pygame.mixer.music.load(caminho_musica)
pygame.mixer.music.play()
input()
pygame.event.wait()
