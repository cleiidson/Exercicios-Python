''' UM PROFFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO.
FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO.
'''
import random  # Importa o módulo random para gerar números aleatórios

print('Irei sortear o aluno para apagar a lousa.')

# Lê os nomes dos alunos
nm1 = input('Aluno 1: ')
nm2 = input('Aluno 2: ')
nm3 = input('Aluno 3: ')
nm4 = input('Aluno 4: ')

# Cria uma lista com os nomes dos alunos
alunos = [nm1, nm2, nm3, nm4]

# Sorteia um aluno aleatoriamente da lista
sorteado = random.choice(alunos)

# Exibe o nome do aluno sorteado
print(f'O sorteado foi o aluno {sorteado}.')

a = 19 // 2
o = 19 % 2

print(f'o {a} e o {o}')