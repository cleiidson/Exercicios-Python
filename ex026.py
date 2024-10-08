#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome
nome = str(input('Insira um nome: ')).strip()
# Pede ao usuário para inserir um nome e armazena o valor na variável `nome`.

print('O nome inserido tem Silva?')
# Exibe a mensagem perguntando se o nome contém "Silva".

print('silva' in nome.lower())#operador in
# Verifica se "silva" está presente no nome inserido, convertendo a string para minúsculas para uma comparação insensível a maiúsculas e minúsculas.


