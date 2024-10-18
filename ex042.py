'''ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM
- O PRIMEIRO VALOR É MAIOR
- O SEGUNDO VALOR É MAIOR
- NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS'''

# Lê o primeiro valor inteiro do usuário
a1 = int(input('Insira um valor inteiro: '))

# Lê o segundo valor inteiro do usuário
a2 = int(input('Insira outro valor inteiro: '))

# Compara os dois valores
if a1 > a2:
    # Se o primeiro valor é maior, exibe esta mensagem
    print(f'O valor {a1} é maior!')
elif a2 > a1:
    # Se o segundo valor é maior, exibe esta mensagem
    print(f'O valor {a2} é maior!')
else:
    # Se os valores são iguais, exibe esta mensagem
    print('Não existe valor maior, os dois são iguais.')
