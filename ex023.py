'''
crie um programa que leia o nome completo de uma pessoa e mostre
-o nome com todas as letras maiusculas
- o nome com todas as letras minusculas
-quantas letras tem ao todo (sem considerar espaços)
-quantas letras tem o primeiro nome
'''
# Solicitando o nome do usuário
nome = str(input('Qual é o seu nome? ')).strip()#utilizando o strip para eliminar os espaços de antes e depois caso o usúario insira

# Imprimindo o nome com todas as letras maiúsculas e depois com todas as letras minúsculas
print(f'Seu nome com todas as letras maiúsculas fica {nome.upper()}\n '
      f'com as letras minúsculas fica {nome.lower()}')

# Dividindo o nome em uma lista de palavras
dividido = nome.split()

# Calculando e exibindo o número de caracteres do primeiro nome (primeira palavra)
print(f'O primeiro nome {dividido[0]} tem {len(dividido[0])} caracteres.')

# Removendo todos os espaços e exibindo o número de caracteres restantes
semEspaço = nome.replace(" ", "")
print(f'O nome completo inserido tem {len(semEspaço)} letras sem considerar os espaços')
