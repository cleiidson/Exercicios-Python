#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

print('Seja bem-vindo ao sistema da nossa loja!\n')
# Exibe uma mensagem de boas-vindas ao usuário, indicando que ele está no sistema da loja.

valor = float(input('Informe o valor do produto R$ '))
# Solicita ao usuário que insira o valor do produto e converte a entrada para um número decimal (float), armazenando em `valor`.

novo = valor - (valor * 5 / 100)
# Calcula o novo valor do produto aplicando um desconto de 5%.
# O desconto é calculado como 5% do valor original, e o resultado é subtraído do valor original.

print('Ofereceremos um desconto de 5% pra você.\n')
# Informa ao usuário que ele receberá um desconto de 5% no valor do produto.

print(f'Esse produto de R${valor} com desconto fica R${novo:.2f}. Agradecemos pela preferência!')
# Exibe o valor original do produto e o novo valor com o desconto aplicado, formatando a saída para mostrar duas casas decimais.
