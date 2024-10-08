'''
    DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE 3 RETAS E DIGA AO USUÁRIO SE
    ELAS PODEM OU NAO FORMAR UM TRIANGULO.
'''

print('-='*20)  # Imprime uma linha decorativa com 40 caracteres "-=" repetidos 20 vezes
print('Analisador de Triângulos')  # Exibe o título do programa
print('-='*20)  # Imprime outra linha decorativa

# Solicita ao usuário os três comprimentos dos lados de um possível triângulo
r1 = float(input('Primeiro comprimento: '))  # Armazena o primeiro valor como um número de ponto flutuante (decimal)
r2 = float(input('Segundo comprimento: '))  # Armazena o segundo valor como um número de ponto flutuante
r3 = float(input('Terceiro comprimento: '))  # Armazena o terceiro valor como um número de ponto flutuante

# Condição para verificar se os três segmentos podem formar um triângulo:
# A soma de dois lados deve ser sempre maior que o comprimento do terceiro lado para formar um triângulo.
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo:')  # Se a condição for verdadeira, imprime que os segmentos podem formar um triângulo
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo:')  # Caso contrário, imprime que os segmentos não podem formar um triângulo
