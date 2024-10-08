#OPERAÇÕES ARITMÉTICAS
'''
+ ADICAO 5+5 == 7
- SUBTRACAO 5-2 == 3
* MULTIPLICACAO 5*2 == 10
/ DIVISAO 5/2 == 2.5
** POTENCIA 5**2 == 25
// DIVISAO INTEIRA 5//2 == 2
% RESTO DA DIVISAO 5%2==1

ORDEM DE PROCEDENCIA
1- ()
2- **
3- *, /, // e % (CASO APAREÇA TODOS DE UMA VEZ, RESOLVER O QUE APARECER PRIMEIRO
4- + e -
'''

n1 = int(input('Digite um número: '))
# Solicita ao usuário que insira um número e converte a entrada para um inteiro, armazenando em `n1`.

n2 = int(input('Digite outro número: '))
# Solicita ao usuário que insira outro número e converte a entrada para um inteiro, armazenando em `n2`.

soma = n1 + n2
# Calcula a soma dos números `n1` e `n2` e armazena o resultado na variável `soma`.

div = n2 / n1
# Calcula a divisão de `n2` por `n1` e armazena o resultado na variável `div`.

mult = n1 * n1
# Calcula a multiplicação de `n1` por ele mesmo e armazena o resultado na variável `mult`.

exp = n1 ** n2
# Calcula `n1` elevado à potência de `n2` e armazena o resultado na variável `exp`.

divInt = n2 // n1
# Calcula a divisão inteira de `n2` por `n1` (resultado da divisão sem a parte decimal) e armazena em `divInt`.

# Exibe os resultados das operações realizadas.
# {:.3f} é usado para formatar a saída com 3 casas decimais.
print(f'A soma é {soma}, a divisão é {div:.3f}, a multiplicação é {n1 * n2},\n'
      f' a potência é {exp:.3f},\n'
      f' a divisão inteira é {divInt}')

