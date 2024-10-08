#Faça um programa que leia um numero inteiro qualquer e mostre sua tabuada
print('Tabuada')
# Exibe um cabeçalho indicando que o programa irá mostrar a tabuada.

n1 = int(input('Sobre qual número você gostaria de ver a tabuada? '))
# Solicita ao usuário que insira um número para o qual deseja ver a tabuada, convertendo a entrada para um inteiro e armazenando em `n1`.

print(f' {n1} x {1:2} = {n1*1}\n'  # Utiliza :2 para garantir que o número da multiplicação ocupe dois dígitos, facilitando a formatação
      f' {n1} x {2:2} = {n1*2}\n' 
      f' {n1} x {3:2} = {n1*3}\n'
      f' {n1} x {4:2} = {n1*4}\n'
      f' {n1} x {5:2} = {n1*5}\n'
      f' {n1} x {6:2} = {n1*6}\n'
      f' {n1} x {7:2} = {n1*7}\n'
      f' {n1} x {8:2} = {n1*8}\n'
      f' {n1} x {9:2} = {n1*9}\n'
      f' {n1} x {10:2} = {n1*10}')
# Exibe a tabuada do número fornecido pelo usuário, utilizando f-strings para interpolar os valores.
# O formato :2 assegura que a multiplicação fique bem alinhada na saída, mesmo para números de um dígito.

# O código é eficiente, pois evita o uso de várias variáveis, mantendo tudo em um único bloco de impressão.
