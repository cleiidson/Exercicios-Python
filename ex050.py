'''FAÇA UM PROGRAMA QUE MOSTRE UMA CONTAGEM REGRESIVA PARA O ESTOURO DE FOGOS DE ARTIFICIO,
INDO DE 10 ATÉ 0, COM PAUSA DE 1 SEGUNDO ENTRE ELES.'''

from time import sleep  # Importa a função 'sleep' da biblioteca 'time', que permite pausar o programa por um tempo

print('COMEÇA AGORA A CONTAGEM REGRESSIVA PARA A VIRADA DE ANO!')
# Exibe a mensagem inicial de contagem regressiva

sleep(0.5)  # Pausa o programa por 0.5 segundos antes de iniciar a contagem

# 'for' que começa a contagem de 10 até 0, decrementando 1 a cada iteração
for c in range(10, -1, -1):
    sleep(1)  # Pausa por 1 segundo a cada número da contagem
    print(c)  # Exibe o número atual da contagem regressiva

print('FELIZ ANO NOVO!')  # Quando a contagem chega a 0, imprime a mensagem de Feliz Ano Novo
