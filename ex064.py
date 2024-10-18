'''Exercício 1: Média de Notas e Maior Nota
Enunciado: Desenvolva um programa que leia o nome e a nota de 4 alunos. No final, mostre:

A média de notas da turma.
O nome do aluno com a maior nota.
Quantos alunos tiveram nota maior ou igual a 7 (considerando aprovação com 7 ou mais).'''

alunoMaiorNota = ''
notaMaior = 0
somaNotas = 0
maiorQ7 = 0

print('Analisando a nota de 4 alunos.')
for i in range(1, 5):
    aluno = str(input(f'Insira o nome do {i}º aluno: ')).strip()
    sexo = str(input('Insira o sexo: [M/F] ')).strip().upper()
    nota = float(input('Insira sua nota: '))

    # Verifica se a nota é maior que 7
    if nota > 7:
        maiorQ7 += 1

    # Atualiza o aluno com a maior nota
    if nota > notaMaior:
        notaMaior = nota
        alunoMaiorNota = aluno

    # Soma as notas para calcular a média
    somaNotas += nota

    # Validação para o sexo
    if sexo not in 'MF':
        print('Sexo inválido. Por favor, insira M ou F.')


# Calcula a média das notas
mediaNota = somaNotas / 4

# Exibe os resultados
print(f'A média das notas é {mediaNota:.2f}.')
print(f'O aluno com a maior nota foi {alunoMaiorNota} com a nota {notaMaior}.')
print(f'{maiorQ7} alunos tiveram nota maior que 7.')
