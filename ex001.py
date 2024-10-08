#TIPOS PRIMITIVOS OS 4 FUNDAMENTAIS int: 7, -4, 0 etc, float: 4.5, 0.075, -15.225, 7.0, bool: true or false e str:'olá', '7.5'
#n1 = input ('Digite um numero: ')
#n2 = input ('Digite outro numero: ')
#soma = n1 + n2
#print('a soma vale ', soma) #forma errada de ser somado, pois está sendo considerado como string

#FORMA CORRETA - devo informar o tipo da variável q vou inserir

n4 = int(input('Digite um número: '))
n5 = int(input('Digite outro número: '))
soma = n4 + n5

print(f'A soma dos números {n4} e {n5} é {soma}')