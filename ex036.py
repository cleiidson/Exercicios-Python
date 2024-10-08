'''ESCREVA UM PROGRAMA QUE PERGUNTE UM SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO
PARA SALÁRIO SUPERIORES A R$ 1250.00, CALCULE UM AUMENTO DE 10%.
PARA OS INFERIORES OU IGUAIS, O AUMENTO DE 15%.'''

# Solicita ao usuário que insira o valor do salário para calcular o aumento
salario = float(input('Insira o valor do seu salário para calcular o valor do seu aumento: '))

# Verifica se o salário é maior que R$ 1250,00 para calcular o aumento adequado
if salario >= 1250:
    # Calcula o novo salário, adicionando 10% ao salário atual
    novo_salario = salario + (salario * 0.10)

else:
    # Calcula o novo salário, adicionando 15% ao salário atual
    novo_salario = salario + (salario * 0.15)

# Exibe o valor do novo salário, informando o aumento
print(f'Quem ganhava RS{salario} passa a receber {novo_salario}')