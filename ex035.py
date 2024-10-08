'''FAÇA UM PROGRAMA QUE LEIA TRÊS NUMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR'''
#pedindo para o usúario inserir os valores
a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o terceiro número: '))

#verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')