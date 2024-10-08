'''Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar'''

# Solicita ao usuário que informe um número inteiro
valor = int(input('Informe um número e eu direi se ele é ímpar ou par: '))

# Calcula o resto da divisão do valor por 2
resultado = valor % 2

# A ideia é verificar se o resto da divisão de valor por 2 é zero ou não.
# Quando um número dividido por 2 não deixa resto (valor % 2 == 0), ele é par.
# Caso contrário, é ímpar.
if resultado == 0:
    # Se o resto for 0, o número é par
    print('O número informado é par.')
else:
    # Se o resto não for 0, o número é ímpar
    print('O número informado é ímpar.')
