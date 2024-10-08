#Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
#dolar hoje: R$ 1,00 = U$ 5,43
#CONVERSOR DE MOEDA

print('Me informe quanto você tem na carteira nesse momento ')
# Exibe uma mensagem solicitando ao usuário que informe o valor que possui na carteira.

reais = float(input('Insira o valor R$'))
# Pede ao usuário para inserir o valor em reais, convertendo a entrada para um número decimal (float) e armazenando em `reais`.

dolar = reais / 5.43
# Calcula quantos dólares o usuário poderia comprar com o valor em reais, dividindo `reais` pela taxa de câmbio de 5,43 reais por dólar.

print(f'Você conseguiria comprar {dolar:.2f} dólares')
# Exibe o resultado da conversão, formatando a saída para mostrar duas casas decimais, tornando a informação mais legível.
