#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Insira um número inteiro: '))
# Solicita ao usuário para inserir um número inteiro e armazena o valor na variável `n1`, convertendo a entrada para um inteiro.

antecessor = n1 - 1
# Calcula o antecessor do número `n1`, que é um a menos, e armazena na variável `antecessor`.

sucessor = n1 + 1
# Calcula o sucessor do número `n1`, que é um a mais, e armazena na variável `sucessor`.

print(f'O número que você escolheu foi o {n1}. O seu antecessor é {antecessor} e o sucessor é {sucessor}')
# Exibe uma mensagem formatada mostrando o número escolhido pelo usuário, seu antecessor e seu sucessor.

print('Obrigado pela interação :)')
# Exibe uma mensagem de agradecimento ao usuário pela interação.
