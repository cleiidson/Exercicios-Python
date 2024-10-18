'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

-A VISTA DINHEIRO/ CHEQUE: 10% DE DESCONTO
-A VISTA NO CARTAO: 5% DE DESCONTO
- EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
- 3X OU MAIS NO CARTÃO 20% DE JUROS'''
# Início do programa - imprime o cabeçalho estilizado da loja
print('=' * 10 + ' G.O.A.T S.T.O.R.E ' + '=' * 10)

# Recebe o valor das compras digitado pelo usuário
preco = float(input('Preço das compras: R$ '))

# Exibe as opções de forma de pagamento disponíveis
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/pix
[ 2 ] À vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x no cartão ''')

# Recebe a escolha do usuário sobre a forma de pagamento
opção = int(input('Qual é a opção? '))

# Verifica a forma de pagamento escolhida
if opção == 1:
    # Se for à vista em dinheiro/pix, aplica um desconto de 10%
    total = preco - (preco * 0.10)
elif opção == 2:
    # Se for à vista no cartão, aplica um desconto de 5%
    total = preco - (preco * 0.05)
elif opção == 3:
    # Se for 2x no cartão, o preço se mantém e calcula o valor de cada parcela
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcela 2x de R$ {parcela}')  # Exibe o valor da parcela
elif opção == 4:
    # Se for 3x ou mais no cartão, aplica um juros de 20%
    total = preco + (preco * 0.20)

    # Pergunta quantas parcelas o usuário deseja
    totparc = int(input('Quantas parcelas? '))

    # Calcula o valor de cada parcela com os juros
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de {parcela} COM JUROS.')  # Exibe o valor de cada parcela
else:
    # Se o usuário escolheu uma opção inválida, define o total como o preço original e exibe mensagem de erro
    total = preco
    print('\033[1;31mOPÇÃO INVÁLIDA. Tente novamente')

# Exibe o valor final das compras, independentemente da forma de pagamento escolhida
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
