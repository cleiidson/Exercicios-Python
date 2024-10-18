'''Escreva um programa que leia 6 números inteiros informados pelo usuário. No final, mostre a soma apenas dos números que forem múltiplos de 5.
'''

soma = 0  # Inicializa a variável para somar os múltiplos de 5
cont = 0  # Inicializa a variável para contar quantos múltiplos de 5 foram informados

for c in range(1, 7):  # Laço que se repete 6 vezes, de 1 a 6
    num = int(input(f'Insira o valor {c}: '))  # Pede ao usuário para inserir um número inteiro
    if num % 5 == 0:  # Verifica se o número é múltiplo de 5
        cont += 1  # Incrementa o contador de múltiplos de 5
        soma += num  # Adiciona o número à soma dos múltiplos de 5

print(f'A soma dos {cont} números múltiplos de 5 é {soma}')  # Exibe o resultado final
