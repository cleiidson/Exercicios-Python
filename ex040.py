'''ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCARIO PARA A COMPRA DE UMA CASA.
O PROGRAMA VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS
ELE VAI PAGAR

CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER 30% DO SALÁRIO
OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO'''

print('-=' * 20)
print('Central de aprovação de empréstimo.')
print('-=' * 20)

# Lê o valor da casa, o salário do comprador e o tempo de pagamento
casa = float(input('Insira o valor da casa \nR$ '))
remuneracao = float(input('Qual é a sua atual remuneração? \nR$ '))
anos = int(input('Em quantos anos você quer quitar?\n'))

# Calcula 30% do salário e o valor da prestação mensal
excedente = remuneracao * 0.30
prestacao = casa / (anos * 12)

# Exibe uma mensagem sobre a regra do empréstimo
print('Se a sua prestação exceder 30% do seu salário, o empréstimo não será aceito.\n')

# Verifica se a prestação excede 30% do salário
if prestacao > excedente:
    print('Infelizmente o financiamento da casa foi negado.')
    print(f'A prestação mensal seria de R$ {prestacao:.2f},\n'
          f'que é superior aos R$ {excedente:.2f}, que equivale a 30% do seu salário.')
else:
    print('O financiamento foi aceito!')
    print(f'A prestação mensal será de R$ {prestacao:.2f}')
