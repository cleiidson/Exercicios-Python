'''FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS IMPARES QUE SÃO MULTIPLOS DE TRES E QUE
SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500.'''

soma = 0  # Inicializa a variável 'soma', que vai acumular os valores somados
cont = 0  # Inicializa a variável 'cont', que vai contar quantos números foram somados

# Laço for que percorre os números de 1 a 500, pulando de 2 em 2 (ou seja, somente números ímpares)
for c in range(1, 501, 2):
    if c % 3 == 0:  # Verifica se o número atual é múltiplo de 3
        cont += 1  # Incrementa o contador, pois o número é ímpar e múltiplo de 3
        soma += c  # Adiciona o número à variável 'soma'
        print(c, end=' ')  # Imprime o número, sem quebrar a linha (tudo na mesma linha)

print('Esses são os números ímpares múltiplos de 3.')  # Imprime uma mensagem informando o que foi listado
print(f'A soma dos {cont} números solicitados é {soma}')  # Exibe o total de números contados e a soma dos mesmos
