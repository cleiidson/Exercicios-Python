'''Escreva um programa que faça o computador 'pensar' em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o numero escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu'''

import random  # Importa a biblioteca random para gerar números aleatórios
from time import sleep
# Mensagem inicial para o usuário
print('Olá, vamos jogar um jogo?')

print('-=-'*20)
print('Irei sortear um número de 0 a 5 e caso você advinhe, você ganhou.')
print('-=-'*20)

# Solicita que o usuário escolha um número de 0 a 5
nmr = int(input('Por favor, escolha um número de 0 a 5: '))

print('PROCESSANDO...')
sleep(3)
# Gera um número aleatório entre 0 e 5 e o armazena na variável "sorteado"
sorteado = random.randint(0, 5)

# Verifica se o número escolhido pelo usuário é igual ao número sorteado
if nmr == sorteado:
    print(f'O número sorteado foi exatamente {nmr} você venceu.')  # Mensagem para quando o usuário acertar
else:
    print(f'O número sorteado não foi {nmr}. Você perdeu!')  # Mensagem para quando o usuário errar
