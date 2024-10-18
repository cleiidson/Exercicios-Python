'''
Aqui está outro desafio diferente:

Desafio: Classificação de Notas

Objetivo: Crie um programa que peça a nota de 6 alunos e classifique cada um deles com base nas seguintes faixas:

Nota entre 0 e 4: Reprovado
Nota entre 5 e 7: Recuperação
Nota entre 8 e 10: Aprovado
Ao final, o programa deve mostrar:

Quantos alunos foram reprovados.
Quantos alunos estão em recuperação.
Quantos alunos foram aprovados.'''

# Inicializa contadores para cada classificação de nota
reprovados = 0
recuperação = 0
aprovados = 0

# Loop que itera por 6 alunos
for c in range(1, 7):
    # Solicita a nota do aluno e converte para float
    nota = float(input(f'Insira a nota do {c}º aluno: '))

    # Verifica se a nota está na faixa de reprovados (0 a 4.99)
    if 0 <= nota < 5:
        reprovados += 1  # Incrementa o contador de reprovados

    # Verifica se a nota está na faixa de recuperação (5 a 7)
    elif 5 <= nota <= 7:
        recuperação += 1  # Incrementa o contador de recuperação

    # Verifica se a nota está na faixa de aprovados (8 a 10)
    elif 8 <= nota <= 10:
        aprovados += 1  # Incrementa o contador de aprovados

    # Se a nota não se encaixar em nenhuma faixa, exibe mensagem de erro
    else:
        print('\033[1;31mInsira uma nota de 0 a 10!\033[0m')

# Exibe o resultado final
print(f'{aprovados} alunos foram aprovados.')  # Mostra total de alunos aprovados
print(f'{reprovados} alunos foram reprovados.')  # Mostra total de alunos reprovados
print(f'{recuperação} alunos estão de recuperação')  # Mostra total de alunos em recuperação
