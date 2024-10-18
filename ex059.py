'''FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS. NO FINAL, MOSTRE
QUAL FOI O MAIOR E O MENOR PESO LIDOS'''
menor = 0  # Variável para armazenar o menor peso
maior = 0  # Variável para armazenar o maior peso

# Laço que vai se repetir 5 vezes para coletar os pesos
for p in range(1, 6):
    peso = float(input(f'Informe o peso da {p}ª pessoa: '))  # Solicita o peso da pessoa

    if p == 1:  # Para o primeiro peso, ele é definido como maior e menor
        maior = peso
        menor = peso
    else:
        if peso > maior:  # Verifica se o peso atual é maior que o maior peso registrado
            maior = peso
        if peso < menor:  # Verifica se o peso atual é menor que o menor peso registrado
            menor = peso

# Exibe o maior e o menor peso
print(f'O maior peso lido foi {maior}Kg.')
print(f'O menor peso lido foi {menor}Kg.')
