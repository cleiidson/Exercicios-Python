''' CRIE UM PROGRAA QUE LEIA UM NÚMERO REAL QUALQUER E
MOSTRE NA TELA A SUA PORÇÃO INTEIRA EX: DIGITE UM NUMERO: 6.127
O NÚMERO 6.127 TEM A PARTE INTEIRA 6'''
import math
# Importa a biblioteca matemática que contém funções úteis para operações matemáticas.

nr = float(input('Digite um número real qualquer: '))
# Solicita ao usuário que insira um número real e converte a entrada para um número decimal (float), armazenando em `nr`.

inteiro = math.trunc(nr)
# Utiliza a função `trunc` da biblioteca `math` para remover a parte decimal do número,
# obtendo apenas a parte inteira e armazenando o resultado na variável `inteiro`.

print(f'A porção inteira de {nr} é {inteiro}')
# Exibe a porção inteira do número informado pelo usuário.
