'''DESENVOLVA UM PROGRAMA QUE PERGUNTA A DISTANCIA DE UMA VIAGEM EM KM.
CALCULE O PREÇO DA PASSAGEM, COBRANDO RS0.50 POR KM PARA VIAGENS DE ATÉ 200KM
E R$0.45 PARA VIAGENS MAIS LONGAS.'''

# Solicita ao usuário o destino da viagem e remove espaços em branco
destino = str(input('Qual o destino da sua viagem? ')).strip()

# Solicita ao usuário a distância da viagem em quilômetros e converte para um número de ponto flutuante
kms = float(input('São quantos quilômetros no total? '))

# Verifica se a distância é menor ou igual a 200 km
if kms <= 200:
    # Calcula o custo da passagem para viagens até 200 km
    passagem = kms * 0.50
    # Exibe a informação sobre o custo da passagem
    print(f'Sua viagem com destino para {destino} é inferior a 200km, portanto\n'
          f'sua passagem fica R${passagem:.2f} sendo R$0,50 por km.')
else:
    # Calcula o custo da passagem para viagens acima de 200 km, considerando o desconto
    passagem2 = kms * 0.45
    # Exibe a informação sobre o custo da passagem
    print(f'Sua viagem com destino para {destino} é superior a 200km, portanto\n'
          f'sua passagem fica R${passagem2:.2f} sendo R$0,45 por km.')
