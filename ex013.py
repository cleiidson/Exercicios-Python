#FAÇA UM ALGORITMO QUE LEIA O SLARIO DE UM FUNCIONARIO E MOSTRE SEU NOVO SALARIO, COM 15 DE AUMENTO.

print('Seja bem-vindo ao sistema da estimativas!\n'
      'Daremos um aumento de 15% em seu salário.\n')
# Exibe uma mensagem de boas-vindas ao usuário e informa que um aumento de 15% será aplicado ao salário.

salario = float(input('Informe quanto você ganha hoje R$'))
# Solicita ao usuário que insira o valor do seu salário atual e converte a entrada para um número decimal (float), armazenando em `salario`.

porcentagem = salario * 0.15
# Calcula o valor do aumento de 15% sobre o salário fornecido pelo usuário, armazenando o resultado na variável `porcentagem`.

aumento = salario + porcentagem
# Calcula o novo salário somando o valor do aumento (`porcentagem`) ao salário original, armazenando o resultado em `aumento`.

print(f'O salário com aumento fica em torno de R${aumento:.2f}.')
# Exibe o novo salário após o aumento, formatando a saída para mostrar duas casas decimais, o que é útil para valores monetários.
