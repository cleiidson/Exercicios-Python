'''
    DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE 3 RETAS E DIGA AO USUÁRIO SE
    ELAS PODEM OU NAO FORMAR UM TRIANGULO.
    REFAZENDO ESSE EXERCICIO, MAS ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE
    TRIANGULO SERÁ FORMADO:

    -EQUILÁTERO: TODOS LADOS IGUAIS
    -ISÓSCELES: DOIS LADOS IGUAIS
    -ESCALENO: TODOS OS LADOS DIFERENTES
'''

# Imprime uma linha decorativa com 40 caracteres "-=" repetidos 20 vezes, com cor azul e sublinhado
print('\033[4;34m' + '-=' * 20 + '\033[m')

# Exibe o título do programa
print('Analisador de Triângulos')

# Imprime novamente uma linha decorativa igual à primeira
print('\033[4;34m' + '-=' * 20 + '\033[m')

# Solicita ao usuário os três comprimentos dos lados de um possível triângulo
r1 = float(input('Primeiro comprimento: '))  # Recebe o primeiro comprimento como número decimal
r2 = float(input('Segundo comprimento: '))  # Recebe o segundo comprimento
r3 = float(input('Terceiro comprimento: '))  # Recebe o terceiro comprimento

# Condição para verificar se os três segmentos podem formar um triângulo
# Um triângulo é formado se a soma de dois lados for sempre maior que o terceiro lado
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo:')

    # Verificação do tipo de triângulo
    if r1 == r2 == r3:  # Se todos os lados forem iguais, o triângulo é equilátero
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:  # Se todos os lados forem diferentes, o triângulo é escaleno
        print('ESCALENO')
    else:  # Se dois lados forem iguais e um diferente, o triângulo é isósceles
        print('ISÓSCELES')

else:
    # Caso a condição de formação de triângulo não seja atendida
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo:')
