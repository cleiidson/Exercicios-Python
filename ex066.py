'''Desafio: Média de Idades
Objetivo: Crie um programa que peça a idade de 5 pessoas e, ao final, mostre:

A média de idades.
Quantas pessoas têm mais de 18 anos.'''
soma = 0
maiorIdade = 0
for i in range (1,6):
    anos = int(input(f'Quantos anos a {i}º pessoa tem? '))

    soma += anos

    if 18 <= anos < 110:
        maiorIdade += 1

    elif anos <= 0 or anos > 110:
        print('\033[1;31mA idade inserida é inválida.\033[0m')

media = soma / 5
print(f'{maiorIdade} pessoas são +18.')
print(f'A média de idade é {media}')
