'''FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE:
-SE ELE AINDA VAI SE ALISTAR AO SERVICO MILITAR.
-SE É A HORA DE SE ALISTAR.
- SE JÁ PASSOU DO TEMPO DO ALISTAMENTO.
TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO'''

from datetime import date  # Importa o módulo date para trabalhar com datas

# Solicita ao usuário o ano de nascimento e converte a entrada para um número inteiro
anoNasc = int(input('Em que ano você nasceu? '))

# Obtém o ano atual usando a função today() do módulo date
anoAtual = date.today().year

# Calcula a idade da pessoa subtraindo o ano de nascimento do ano atual
idade = anoAtual - anoNasc

# Mostra a idade atual da pessoa com base no ano de nascimento
print(f'Você tem {idade} anos em {anoAtual}.')

# Verifica se a pessoa tem 18 anos
if idade == 18:
    print('Seu alistamento é esse ano.')  # Caso tenha 18 anos, informa que é o ano do alistamento

# Verifica se a pessoa tem menos de 18 anos
elif idade < 18:
    saldo = 18 - idade  # Calcula quantos anos faltam para o alistamento
    print(f'Ainda faltam {saldo} anos para o alistamento.')  # Exibe a quantidade de anos restantes

    ano = anoAtual + saldo  # Calcula o ano em que o alistamento será obrigatório
    print(f'Seu alistamento será em {ano}')  # Informa o ano exato do alistamento

# Verifica se a pessoa tem mais de 18 anos
elif idade > 18:
    saldo = idade - 18  # Calcula quantos anos já passaram do prazo de alistamento
    print(f'Você já deveria ter se alistado há {saldo} anos.')  # Informa há quanto tempo passou do prazo

    ano = anoAtual - saldo  # Calcula o ano em que a pessoa deveria ter se alistado
    print(f'Seu alistamento foi em {ano}')  # Informa o ano em que o alistamento deveria ter ocorrido
