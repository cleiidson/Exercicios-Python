''' A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO
DE UM ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE.
-ATÉ 9 ANOS - MIRIM   19 ANOS -JUNIOR
 14 ANOS - INFANTIL   20 ANOS - SENIOR
 ACIMA - MASTER
'''
from datetime import date
atual = date.today().year
# Solicita a ano de nascimento
nascimento = int(input('Em que ano você nasceu? '))
idade = atual -nascimento
print(f'O atleta tem {idade} anos.')
# Verifica se a idade está entre 6 e 9 anos, ou seja, na categoria Mirim
if 5 < idade <= 9:
    print('Você é da categoria Mirim!')

# Verifica se a idade está entre 10 e 14 anos, ou seja, na categoria Infantil
elif idade <= 14:
    print('Você é da categoria Infantil!')

# Verifica se a idade está entre 15 e 19 anos, ou seja, na categoria Junior
elif idade <= 19:
    print('Você é da categoria Junior!')

# Verifica se a idade é exatamente 20 anos, ou seja, na categoria Sênior
elif idade == 20:
    print('Vocè é da categoria Sênior!')

# Verifica se a idade está entre 21 e 80 anos, ou seja, na categoria Master
elif 21 <= idade <= 80:
    print('Você é da categoria Master!')

# Caso a idade seja menor que 6 ou maior que 80, exibe uma mensagem de erro
else:
    print('\033[1;31mCom essa idade não é possível competir. Insira uma idade válida!')
