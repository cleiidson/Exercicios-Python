'''
FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE.
'''
# Solicita ao usuário que insira seu nome completo e remove espaços em branco no início e no final
name = str(input('Insira o seu nome completo: ')).strip()

# Divide o nome em partes usando o espaço como delimitador e armazena em uma lista
separado = name.split()

# A última parte da lista 'separado' corresponde ao último nome
ultimo = separado[-1]

# Exibe o nome completo, o primeiro nome e o último nome do usuário
print(f'Seu nome é {name}\n'
      f'seu primeiro nome é {separado[0]}\n'  # A primeira parte da lista é o primeiro nome
      f'e o último é {ultimo}')  # O último nome é obtido da última posição da lista
