#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
print('Para que eu forneça sua média em Matemática, me informe suas últimas 2 notas.')
# Exibe uma mensagem informativa ao usuário sobre a finalidade do programa.

n1 = float(input('Nota do Primeiro Bimestre: '))
# Solicita ao usuário que insira a nota do primeiro bimestre e armazena o valor na variável `n1`, convertendo a entrada para um número decimal (float).

n2 = float(input('Nota do Segundo Bimestre: '))
# Solicita ao usuário que insira a nota do segundo bimestre e armazena o valor na variável `n2`, também como um número decimal.

media = (n1 + n2) / 2
# Calcula a média das notas `n1` e `n2` e armazena o resultado na variável `media`.

print(f'Sua média é {media}. Parabéns! ')
# Exibe a média calculada ao usuário com uma mensagem de congratulação.
