'''
CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO
ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES.
'''
from datetime import datetime  # Importa a biblioteca para trabalhar com datas

anoAtual = datetime.today().year  # Pega o ano atual
menorId = 0  # Contador para pessoas que NÃO atingiram a maioridade
maiorId = 0  # Contador para pessoas que atingiram a maioridade

# Laço para pedir o ano de nascimento de 7 pessoas
for c in range(1, 8):
    dataNasc = int(input(f'{c}- Insira seu ano de nascimento: '))  # Pede o ano de nascimento
    idade = anoAtual - dataNasc  # Calcula a idade da pessoa

    if idade >= 21:  # Se a idade for maior que 18, a pessoa é maior de idade
        maiorId += 1  # Incrementa o contador de pessoas maiores de idade

    else:  # Se a idade for menor ou igual a 18, a pessoa é menor de idade
        menorId += 1  # Incrementa o contador de pessoas menores de idade

# Exibe os resultados finais
print(f'Tivemos {maiorId} pessoas que atingiram a maior idade')
print(f'E {menorId} não atingiram a maior idade')
