'''Faça um programa que leia 8 números inteiros digitados pelo usuário. Após ler todos os números, mostre quantos desses números são negativos.
'''
cont = 0  # Variável para contar quantos números negativos foram inseridos

for negativo in range(1, 9):  # Laço que se repete 8 vezes, de 1 a 8
    numeros = int(input(f'{negativo}- Informe números positivos e negativos: '))  # Pede ao usuário para inserir um número

    if numeros < 0:  # Verifica se o número é negativo (menor que 0)
        cont += 1  # Incrementa o contador de números negativos

print(f'Dos números inseridos, {cont} são negativos')  # Exibe a quantidade de números negativos
