'''FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO
CATETO ADJACENTE DE UM TRIANGULO RETANGULO, CALCULE E
MOSTRE O COMPRIMENTO DA HIPOTENUSA'''
from math import hypot

#forma que eu fiz
'''import math  # Importa o módulo math para realizar cálculos matemáticos

# Mensagem inicial para o usuário
print('Aula de matemática!\n'
      'Mostrando o valor do comprimento da hipotenusa de um triângulo retângulo.')

# Lê o valor do cateto oposto inserido pelo usuário e converte para float
cttOposto = float(input('Informe o valor do cateto oposto: '))

# Lê o valor do cateto adjacente inserido pelo usuário e converte para float
cttAdjacente = float(input('Informe o valor do cateto adjacente: '))

# Calcula o valor da soma dos quadrados dos catetos
valor = math.pow(cttOposto, 2) + math.pow(cttAdjacente, 2)  # Eleva cada cateto ao quadrado e soma

# Calcula a raiz quadrada do valor obtido para encontrar a hipotenusa
hipotenusa = math.sqrt(valor)

# Exibe o valor da hipotenusa, formatando para 2 casas decimais
print(f'A hipotenusa da soma dos quadrados dos catetos é {hipotenusa:.2f}')
'''

#forma que o professor fez
# Lê o valor do cateto oposto inserido pelo usuário e converte para float
cttOposto = float(input('Informe o valor do cateto oposto: '))

# Lê o valor do cateto adjacente inserido pelo usuário e converte para float
cttAdjacente = float(input('Informe o valor do cateto adjacente: '))

hipotenusa = hypot(cttOposto,cttAdjacente) #formula que é própria para hipotenusa
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
