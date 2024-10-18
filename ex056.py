'''FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E DIGA SE ELE É OU NAO UM NUMERO PRIMO'''

p1 = int(input('Digite o primeiro termo: '))
tot = 0

for c in range(1, p1 + 1):  # Laço para verificar divisores do número
    if p1 % c == 0:  # Verifica se o número é divisível
        print('\033[33m', end=' ')  # Cor amarela para divisíveis
        tot += 1  # Conta quantas vezes o número foi divisível
    else:
        print('\033[31m', end=' ')  # Cor vermelha para não divisíveis
    print(f'{c}', end=' ')  # Exibe o divisor

print(f'\n\033[mO número {p1} foi divisível {tot} vezes')

# Verifica se o número é primo
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
