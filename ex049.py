'''CRIE UM PROGRAMA QUE FAÇA O COMPUTADO JOGAR JOKENPÔ COM VOCÊ'''
from random import randint
from time import sleep

# 'itens' armazena as opções disponíveis no jogo: Pedra, Papel e Tesoura
itens = ('Pedra', 'Papel', 'Tesoura')

# 'computador' escolhe um número aleatório entre 0 e 2, correspondendo às opções Pedra, Papel ou Tesoura
computador = randint(0, 2)

# Exibe as opções disponíveis para o jogador
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

# O jogador escolhe sua jogada (0, 1 ou 2)
jogador = int(input('Qual é a sua jogada? '))

# Efeitos de suspense com "JO", "KEN", "PÔ"
print('JO')
sleep(1)  # Espera 1 segundo
print('KEN')
sleep(1)  # Espera 1 segundo
print('PÔ')

# Exibe uma linha decorativa
print('-=' * 11)

# Mostra a escolha do computador, acessando a lista 'itens' com o índice 'computador'
print(f'Computador jogou {itens[computador]}')

# Mostra a escolha do jogador, acessando a lista 'itens' com o índice 'jogador'
print(f'Jogador jogou {itens[jogador]}')

# Exibe outra linha decorativa
print('-=' * 11)

# Verifica todas as condições para determinar o vencedor

if computador == 0:  # Se o computador jogou PEDRA
    if jogador == 0:  # Se o jogador jogou PEDRA
        print('EMPATE')
    elif jogador == 1:  # Se o jogador jogou PAPEL
        print('\033[32mJOGADOR VENCE')  # Jogador vence (Papel ganha de Pedra)
    elif jogador == 2:  # Se o jogador jogou TESOURA
        print('\033[4;34mCOMPUTADOR VENCE')  # Computador vence (Pedra ganha de Tesoura)
    else:
        print('\033[1;33;40mJOGADA INVÁLIDA')  # Entrada inválida

elif computador == 1:  # Se o computador jogou PAPEL
    if jogador == 0:  # Se o jogador jogou PEDRA
        print('\033[4;34mCOMPUTADOR VENCE')  # Computador vence (Papel ganha de Pedra)
    elif jogador == 1:  # Se o jogador jogou PAPEL
        print('EMPATE')
    elif jogador == 2:  # Se o jogador jogou TESOURA
        print('\033[32mJOGADOR VENCE')  # Jogador vence (Tesoura ganha de Papel)
    else:
        print('\033[1;33;40mJOGADA INVÁLIDA')  # Entrada inválida

elif computador == 2:  # Se o computador jogou TESOURA
    if jogador == 0:  # Se o jogador jogou PEDRA
        print('\033[32mJOGADOR VENCE')  # Jogador vence (Pedra ganha de Tesoura)
    elif jogador == 1:  # Se o jogador jogou PAPEL
        print('\033[4;34mCOMPUTADOR VENCE')  # Computador vence (Tesoura ganha de Papel)
    elif jogador == 2:  # Se o jogador jogou TESOURA
        print('EMPATE')
    else:
        print('\033[1;33;40mJOGADA INVÁLIDA')  # Entrada inválida
