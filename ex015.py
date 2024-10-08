#Escreva um program que pergunte a quantidade de km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#calcule o preco a pagar, sabendo que o carro custa 60 reais por dia e 0,15 por km rodado

dias = int(input('Informe por quantos dias você alugou o carro: '))
# Solicita ao usuário que informe a quantidade de dias em que o carro foi alugado e converte a entrada para um número inteiro (int), armazenando em `dias`.

km = float(input('Informe quantos Kms você rodou: '))
# Solicita ao usuário que informe a quantidade de quilômetros rodados e converte a entrada para um número decimal (float), armazenando em `km`.

aPagar = (dias * 60) + (km * 0.15)
# Calcula o valor total a pagar, onde cada dia de aluguel custa R$60 e cada quilômetro rodado custa R$0,15.
# O resultado é armazenado na variável `aPagar`.

print(f'O valor total a pagar é {aPagar:.2f}')
# Exibe o valor total a pagar, formatando a saída para mostrar duas casas decimais, o que é útil para valores monetários.
