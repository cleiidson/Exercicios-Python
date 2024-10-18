'''Escreva um programa que leia 10 números inteiros fornecidos pelo usuário. No final, mostre quantos desses números são pares e quantos são ímpares.
'''

par = 0
impar = 0

for c in range(1, 11):
    valor = int(input(f'Insira o valor {c}: '))

    if valor % 2 == 0:  # Se o número for divisível por 2, é par
        par += 1
    else:  # Se não for par, é ímpar
        impar += 1

print(f'Dos valores inseridos, {par} são pares e {impar} são ímpares.')
