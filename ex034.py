'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''
from datetime import date  # Importa a função date da biblioteca datetime para trabalhar com datas

# Solicita que o usuário insira o ano que deseja analisar. Se o valor for 0, o código analisará o ano atual.
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

# Verifica se o usuário digitou 0. Se sim, o ano a ser analisado será o ano atual.
if ano == 0:
    ano = date.today().year  # A função date.today().year retorna o ano atual.

# Verifica se o ano é bissexto.
# Um ano é bissexto se for divisível por 4 e não divisível por 100, exceto se for divisível por 400.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')  # Se a condição for verdadeira, imprime que o ano é bissexto.
else:
    print(f'O ano {ano} não é BISSEXTO')  # Caso contrário, imprime que o ano não é bissexto.

