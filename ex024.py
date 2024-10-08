'''faça um programa que leia um numero de 0 a 9999 e mostre na tela
cada um dos digitos separados
ex:
digite um numeo 1834
unidade:4 dezena:3 centena:8 milhar:1 '''
n1 = input('Digite um número do 0 a 9999: ')
# Solicita ao usuário que insira um número entre 0 e 9999 e armazena a entrada como uma string em `n1`.

n_str = n1.zfill(4)
# Utiliza o método `zfill` para garantir que a string tenha exatamente 4 dígitos,
# preenchendo com zeros à esquerda se necessário (por exemplo, '7' se torna '0007').

un = n_str[3]  # Extrai o dígito da unidade (4ª posição da string).
dz = n_str[2]  # Extrai o dígito da dezena (3ª posição da string).
cen = n_str[1] # Extrai o dígito da centena (2ª posição da string).
mil = n_str[0] # Extrai o dígito do milhar (1ª posição da string).

print(f'A unidade: {un}\n'
      f'dezena: {dz}\n'
      f'centena: {cen}\n'
      f'milhar: {mil}')
# Exibe cada uma das partes do número (unidade, dezena, centena e milhar) separadamente.
