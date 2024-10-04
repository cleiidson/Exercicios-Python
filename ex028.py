'''
FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ULTIMO NOME SEPARADAMENTE.
'''

name = str(input('Insira o seu nome completo: ')).strip()

separado = name.split()
ultimo = separado[-1]
print(f'Seu nome é {name}\n'
      f'seu primeiro nome é {separado[0]}\n'
      f'e o ultimo é {ultimo}')