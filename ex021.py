"""Faça um programa em python que abra e reproduza o audio de um arquivo mp3"""

import pygame
pygame.init()#dando inicio ao import pygame
pygame.mixer.music.load('ex021.mp3')#chamando o arquivo mp3 para tocar a musica
pygame.mixer.music.play()
pygame.event.wait()
