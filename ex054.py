'''DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA
APENAS DAQUELAS QUE FOREM PARES. SE O VALOR DIGITADO FOR ÍMPAR, DESCONSIDERE-O'''
soma = 0  # Inicializa a variável 'soma', que vai acumular a soma dos números pares
cont = 0  # Inicializa a variável 'cont', que vai contar quantos números pares foram somados

# Laço for que se repete 6 vezes, de 1 a 6 (o valor de 'c' será 1, 2, 3, ..., até 6)
for c in range(1, 7):
    valor = int(input(f'Informe o valor {c}: '))  # Solicita ao usuário para digitar um número inteiro

    # Verifica se o número informado pelo usuário é par
    if valor % 2 == 0:
        soma += valor  # Se for par, adiciona o valor à variável 'soma'
        cont += 1  # Incrementa o contador, pois esse número foi par

# Exibe quantos números pares foram informados e a soma total dos números pares
print(f'Você informou {cont} números pares e a soma foi {soma}')
