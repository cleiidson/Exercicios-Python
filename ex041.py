'''ESCREVA UM NÚMERO QUE LEIA UM NUMERO INTEIRO QUALQUER E PEÇA PARA O USUARIO ESCOLHER QUAL SERA A BASE DE CONVERSAO
- 1 PARA BINARIO
- 2 PARA OCTAL
- 3 PARA HEXADECIMAL '''

# Solicita que o usuário insira um número inteiro
valor = int(input('Insira um número inteiro: '))

# Solicita que o usuário escolha a base de conversão
conversao = int(input('Digite 1 para conversão em Binário.\n'
                      'Digite 2 para conversão em Octal.\n'
                      'Digite 3 para conversão em Hexadecimal.\n'))

# Verifica qual base de conversão o usuário escolheu
if conversao == 1:
    print('Aqui está a conversão em Binário.')
    print(bin(valor)[2:])  # Converte o número para binário e exibe
elif conversao == 2:
    print('Aqui está a conversão em Octal.')
    print(oct(valor)[2:])  # Converte o número para octal e exibe
elif conversao == 3:
    print('Aqui está a conversão em Hexadecimal.')
    print(hex(valor)[2:])  # Converte o número para hexadecimal e exibe
else:
    # Caso o usuário não escolha 1, 2 ou 3, exibe uma mensagem de erro
    print('\033[1;31m Por favor digite um número do 1 ao 3.')
