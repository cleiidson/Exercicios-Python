#Escreva um programa que converta a tempretatura de Cº PARA ºF
c = float(input('Informe a temperatura em ºC: '))
# Solicita ao usuário que insira a temperatura em graus Celsius e converte a entrada para um número decimal (float), armazenando em `c`.

f = ((9 * c) / 5) + 32
# Calcula a temperatura em graus Fahrenheit utilizando a fórmula de conversão.
# Os parênteses são usados para garantir a ordem de precedência na operação.

print(f'A temperatura de {c}ºC corresponde a {f}ºF ')
# Exibe a temperatura original em graus Celsius e o valor convertido para Fahrenheit.

