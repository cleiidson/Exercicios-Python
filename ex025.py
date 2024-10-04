#Crie um programa que leia o nome de uma cidade e diga se ela começa
#com 'SANTO'

city = str(input('Insira o nome de uma cidade: ')).strip()
# Pede ao usuário para inserir o nome de uma cidade e armazena na variável `city`.

dividido1 = city.split()
# Divide a string `city` em uma lista de palavras, usando o espaço como separador, e armazena na variável `dividido1`.
# Exemplo: Se o usuário inserir "Santo André", `dividido1` será ["Santo", "André"].

print('A palavra inserida começa com Santo?')
# Exibe a pergunta para o usuário.

print(dividido1[0].lower() == 'santo')
# Verifica se a primeira palavra (índice 0) da lista `dividido1` é igual a "santo".
# `.lower()` é usado para converter a palavra para letras minúsculas, garantindo que a comparação seja insensível a maiúsculas/minúsculas.
# O resultado será `True` se a cidade começar com "Santo" e `False` caso contrário.

''' FORMA FEITA PELO PROFESSOR
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO'
'''