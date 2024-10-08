''' INTRODUÇÃO AS CONDIÇOES IF ELSE'''

# Solicita ao usuário que insira a primeira nota
n1 = float(input('Digite a primeira nota: '))

# Solicita ao usuário que insira a segunda nota
n2 = float(input('Digite a segunda nota: '))

# Calcula a média das duas notas
m = (n1 + n2) / 2

# Mostra a média calculada, com uma casa decimal
print(f'A sua média foi {m:.1f}.')

# Verifica se a média é maior ou igual a 6
if m >= 6:
    # Se for maior ou igual a 6, exibe uma mensagem de parabéns
    print('Parabéns sua média é maior que 6.')
else:
    # Caso contrário, exibe uma mensagem motivando a estudar mais
    print('Sua média está baixa! Estude mais!')
