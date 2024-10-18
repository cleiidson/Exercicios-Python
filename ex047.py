''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

print('Cálculo de IMC')  # Exibe o título do programa

# Entrada de dados: Solicita ao usuário que insira seu peso e altura
peso = float(input('Insira o seu peso (em kg): '))  # Recebe o peso do usuário e converte para tipo float
altura = float(input('Insira sua altura (em metros): '))  # Recebe a altura do usuário e converte para tipo float

# Cálculo do IMC: Fórmula padrão IMC = peso / (altura * altura)
imc = peso / (altura * altura) #ou imc = peso / (altura **2)

# Estrutura condicional para verificar a faixa de IMC e exibir o status correspondente
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}. Você está abaixo do peso!')  # Abaixo de 18.5: Abaixo do peso
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.2f}. Você está no peso ideal!')  # Entre 18.5 e 25: Peso ideal
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.2f}. Você está na faixa de Sobrepeso!')  # Entre 25 e 30: Sobrepeso
elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.2f}. Você está na faixa de obesidade!')  # Entre 30 e 40: Obesidade
else:
    print(f'Seu IMC é {imc:.2f}. Você está na faixa de Obesidade Mórbida. Tome cuidado!')  # Acima de 40: Obesidade Mórbida


