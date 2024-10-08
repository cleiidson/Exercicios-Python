'''FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER
E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE
DESSE ANGULO'''
import math  # Importa o módulo math para realizar cálculos matemáticos

# Lê o ângulo informado pelo usuário e o converte para inteiro
angulo = float(input('Informe um angulo para que eu mostre o valor do \n'
                   'seno, cosseno e tangente desse angulo: '))

# Converte o ângulo de graus para radianos
radiano = math.radians(angulo)

# Calcula o seno, cosseno e tangente do ângulo em radianos
sen = math.sin(radiano)
cos = math.cos(radiano)
tan = math.tan(radiano)

# Exibe os resultados formatados com duas casas decimais
print(f'O angulo informado foi {angulo} e \n'
      f'tem o seno de {sen:.2f}, o \n'
      f'cosseno de {cos:.2f}\n'
      f'e a tangente de {tan:.2f}')