'''
UM PROFESSOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS
FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E E MOSTRE A ORDEM SORTEADA.
'''

import random  # Importa o módulo random para gerar números aleatórios

print('Irei sortear a ordem dos alunos para a apresentação.')

# Lê os nomes dos alunos
nm1 = input('Aluno 1: ')
nm2 = input('Aluno 2: ')
nm3 = input('Aluno 3: ')
nm4 = input('Aluno 4: ')

# Cria uma lista com os nomes dos alunos
alunos = [nm1, nm2, nm3, nm4]

# Embaralha a lista de alunos
random.shuffle(alunos)

# Exibe a ordem dos alunos sorteados
print('A ordem de apresentação será:')
print(alunos)  # Imprime a lista de alunos em ordem aleatória
