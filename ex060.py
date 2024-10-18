# Variáveis para armazenar informações relevantes
maiorIdadeHom = 0  # Para armazenar a maior idade entre os homens
nomeVelho = ''      # Para armazenar o nome do homem mais velho
somaidade = 0       # Para somar as idades de todas as pessoas
totMulher20 = 0     # Para contar quantas mulheres têm menos de 20 anos
mediaidade = 0

# Loop para coletar dados de 4 pessoas
for pessoa in range(1, 5):
    # Pede o nome da pessoa
    nome = str(input(f'----Qual o nome da {pessoa}º pessoa? ----\n')).strip()

    # Pede a idade da pessoa
    idade = int(input(f'Qual a idade:  '))

    # Pede o sexo da pessoa (M para masculino, F para feminino)
    sexo = str(input('Qual o sexo?\n'
                     ' Insira [M/F]: ')).strip()

    # Soma as idades para calcular a média depois
    somaidade += idade

    # Verifica se o primeiro homem é o mais velho
    if pessoa == 1 and sexo in 'Mm':
        maiorIdadeHom = idade
        nomeVelho = nome

    # Se for homem e tiver mais idade que o anterior, atualiza o nome e a idade
    if sexo in 'Mm' and idade > maiorIdadeHom:
        maiorIdadeHom = idade
        nomeVelho = nome

    # Se for mulher e tiver menos de 20 anos, incrementa o contador de mulheres
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1

# Calcula a média de idade do grupo
mediaidaede = somaidade / 4

# Exibe os resultados
print(f'A média de idade do grupo é de {mediaidaede}.')
print(f'O homem mais velho tem {maiorIdadeHom} anos e se chama {nomeVelho}.')
print(f'Ao todo são {totMulher20} mulheres com menos de 20 anos.')
