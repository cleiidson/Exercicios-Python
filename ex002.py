#faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele
#usando as funcionalidades de um objeto --> variavel "a"

a = input('Digite algo: ')
#print('O tipo primitivo desse valor é', type(a))
#print('Só há espaços?', a.isspace())
#print('Possue número?', a.isnumeric())
#print('É alfabético?', a.isalpha())
#print('Começa com letra minúscula?', a.islower())
#print('É alfanumérico?', a.isalnum())
#print('Começa com letra maiúscula?', a.isupper())

#\n quebra linha - newline
print(f'Começa com letra maiúscula? {a.isupper()}\n',
      f'Só há espaços? {a.isspace()}\n',
      f'Possue número? {a.isnumeric()}\n',
      f'Começa com letra minúscula? {a.islower()}\n',
      f'É alfanumérico? {a.isalnum()}\n',
      f'Começa com letra maiúscula? {a.isupper()}\n'

      )