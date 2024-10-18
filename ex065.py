'''Desenvolva um programa que leia as informações de 5 funcionários, coletando os seguintes dados:
Nome, Idade, Salário
Cargo (Analista, Gerente, ou Estagiário)
No final do programa, exiba:

A média de idade dos funcionários.
O nome do funcionário mais velho.
O total de funcionários que têm um salário superior a R$ 3.000,00.
O número de Estagiários cadastrados.'''
estagCadastrados = 0
somasalario = 0
funcVelho = 0
nomeFuncVelho = ''
funcComMais3k = 0
somaIdade = 0

for info in range(1, 6):
    print('-=' * 20)
    nome = str(input(f'Insira o {info}º nome: ')).strip()
    idade = int(input('Insira a idade: '))
    salario = float(input('Insira o seu salário: '))
    cargo = str(input('Insira qual dos 3 é o seu cargo (Analista, Gerente ou Estagiário): ')).strip().lower()

    somasalario += salario
    somaIdade += idade

    # Verifica se essa pessoa é a mais velha
    if idade > funcVelho:
        funcVelho = idade  # Atualiza a maior idade
        nomeFuncVelho = nome  # Atualiza o nome da pessoa mais velha

    # Verifica se o salário é maior que 3000
    if salario > 3000:
        funcComMais3k += 1  # Incrementa o contador

    # Verifica se o cargo é estagiário
    if cargo == 'estagiário':  # Comparação em minúsculas
        estagCadastrados += 1  # Incrementa o contador

    # Valida o cargo
    elif cargo not in ['analista', 'gerente', 'estagiário']:
        print('Cargo inválido. Por favor, insira novamente.')

# Calcula a média de salário e idade
mediaSalario = somasalario / 5
mediaIdade = somaIdade / 5

# Exibe os resultados
print(f'Temos {estagCadastrados} estagiários.')
print(f'A média dos salários é R$ {mediaSalario:.2f}')
print(f'{funcComMais3k} funcionários recebem mais de R$ 3.000')
print(f'A média de idade é {mediaIdade:.2f} anos')
print(f'O funcionário mais velho é {nomeFuncVelho}, com {funcVelho} anos')

